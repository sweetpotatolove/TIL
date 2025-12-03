from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 업데이트할 내용 정의
update_body = {
    "doc": {
        "stock": 200
    }
}

# ID가 1001인 문서의 stock 필드 업데이트
response = es.update(index="products", id=1001, body=update_body)

# 결과 출력
print(response)
