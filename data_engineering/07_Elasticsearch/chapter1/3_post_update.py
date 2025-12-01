from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 업데이트할 필드 정의
update_body = {
    "doc": {
        "price": 1099
    }
}

# 문서 업데이트 요청 (ID: 1001)
response = es.update(index="products", id=1001, body=update_body)

# 결과 출력
print(response)
