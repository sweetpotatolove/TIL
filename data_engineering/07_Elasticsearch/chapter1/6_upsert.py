from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 업데이트할 필드 정의
update_body = {
    "doc": {
        "price": 1099,
        "stock": 150
    },
    "doc_as_upsert": True
}

# 문서 업데이트 (또는 없으면 삽입)
response = es.update(index="products", id=1001, body=update_body)

print(response)
