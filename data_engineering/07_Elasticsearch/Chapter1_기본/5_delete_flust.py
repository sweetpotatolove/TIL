from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 문서 삭제 (ID: 1001, 인덱스: products)
response = es.delete(index="products", id=1001)

print(response)

# 인덱스 강제 flush
response = es.indices.flush(index="products")

print(response)