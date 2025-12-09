from elasticsearch import Elasticsearch, helpers
import json
import os

# 1. Elasticsearch 클라이언트 연결
es = Elasticsearch("http://localhost:9200")
index_name = "products"

# 2. 인덱스 존재 시 삭제
if es.indices.exists(index=index_name):
    print(f"[0] 기존 인덱스 '{index_name}' 삭제")
    es.indices.delete(index=index_name)

# 3. 인덱스 생성 및 매핑 정의
print(f"[1] 인덱스 '{index_name}' 생성 및 매핑 설정")
mapping = {
    "mappings": {
        "properties": {
            "product_id": {"type": "integer"},
            "name": {"type": "text"},
            "brand": {"type": "keyword"},
            "description": {"type": "text"},
            "category": {"type": "keyword"},
            "price": {"type": "float"},
            "features": {
                "type": "nested",
                "properties": {
                    "feature_name": {"type": "keyword"},
                    "feature_value": {"type": "keyword"}
                }
            }
        }
    }
}
es.indices.create(index=index_name, body=mapping)

# 4. NDJSON 파일 로드
json_path = "product_list.json"
print("[2] Bulk 데이터 삽입 시작")
if not os.path.exists(json_path):
    print(f"[오류] 파일 없음: {json_path}")
    exit(1)

with open(json_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

actions = []
for i in range(0, len(lines), 2):
    action_line = json.loads(lines[i])
    doc_line = json.loads(lines[i + 1])
    
    action_type, meta = list(action_line.items())[0]
    index = meta.get("_index", index_name)
    doc_id = meta.get("_id")

    action = {
        "_op_type": action_type,
        "_index": index,
        "_source": doc_line
    }
    if doc_id:
        action["_id"] = doc_id

    actions.append(action)

# 5. Bulk 인덱싱 실행
helpers.bulk(es, actions)

print(f"[완료] {len(actions)}건 인덱싱 완료 → 인덱스: '{index_name}'")
