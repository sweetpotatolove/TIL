from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://localhost:9200")

# ILM 상태 빠르게 감지되도록 설정
es.cluster.put_settings(body={
    "persistent": {
        "indices.lifecycle.poll_interval": "10s"
    }
})

# 1. 기존 demo-ilm-* 인덱스 삭제
try:
    indices = es.indices.get(index="demo-ilm-*")
    for idx in indices:
        es.indices.delete(index=idx)
        print(f"Deleted index: {idx}")
except Exception as e:
    print("삭제할 인덱스 없음 또는 오류:", e)

# 2. 기존 템플릿 삭제
try:
    es.indices.delete_index_template(name="demo-ilm-template")
    print("기존 템플릿 demo-ilm-template 삭제 완료")
except Exception as e:
    print("템플릿 삭제 스킵:", e)
    
try:
    es.indices.delete_index_template(name="demo-template")
    print("기존 템플릿 demo-template 삭제 완료")
except Exception as e:
    print("demo-template 삭제 스킵:", e)

# 3. ILM 정책 생성
# node.roles: [master, data, ingest]가 디폴트, role에서 hot_node가 없으면 이 data는 내부적으로는 data_content로 해석되고,
# 티어 기반 조건 (_tier_preference)을 무시하고라도 인덱스를 생성
es.ilm.put_lifecycle(name="simple-ilm-policy", body={
    "policy": {
        "phases": {
            "hot": {
                "actions": {
                    "rollover": {
                        "max_docs": 5
                    }
                }
            },
            "delete": {
                "min_age": "2m",
                "actions": {
                    "delete": {}
                }
            }
        }
    }
})
print("ILM 정책 생성 완료")

# 4. 템플릿 생성 (priority 설정)
es.indices.put_index_template(name="demo-ilm-template", body={
    "index_patterns": ["demo-ilm-*"],
    "priority": 10,
    "template": {
        "settings": {
            "index.lifecycle.name": "simple-ilm-policy",
            "index.lifecycle.rollover_alias": "demo-ilm-write"
        }
    }
})
print("템플릿 생성 완료")

# 5. 초기 인덱스 생성
es.indices.create(index="demo-ilm-000001", body={
    "aliases": {
        "demo-ilm-write": {"is_write_index": True}
    }
})
print("초기 인덱스 생성 완료")

# 6. 문서 삽입
for i in range(10):
    es.index(index="demo-ilm-write", document={"msg": f"test-{i}"})
    print(f"문서 삽입: test-{i}")
    time.sleep(1)

# 7. 인덱스 상태 출력
print("\n현재 demo-ilm-* 인덱스 목록:")
print(es.cat.indices(index="demo-ilm-*", format="text"))

# 8. ILM 상태 확인
resp = es.ilm.explain_lifecycle(index="demo-ilm-000001")
info = resp["indices"]["demo-ilm-000001"]

print("\nILM 상태 요약:")
print(f"인덱스: {info['index']}")
print(f"정책: {info['policy']}")
print(f"경과 시간: {info['age']}")
print(f"현재 단계: {info['phase']}")
print(f"rollover 조건 (max_docs): {info['phase_execution']['phase_definition']['actions']['rollover']['max_docs']}")

# 9. rollover 확인을 위한 대기 + alias 체크
print("\nrollover 발생 여부 확인 (12초 대기 중)...")
time.sleep(12)

try:
    alias_info = es.indices.get_alias(name="demo-ilm-write")
    print("\ndemo-ilm-write alias가 가리키는 인덱스들:")

    for index_name, value in alias_info.items():
        alias_props = value.get("aliases", {}).get("demo-ilm-write", {})
        is_write = alias_props.get("is_write_index", False)
        status = "쓰기 대상" if is_write else "읽기 전용"
        print(f" - {index_name} ({status})")
except Exception as e:
    print("alias 조회 실패:", e)