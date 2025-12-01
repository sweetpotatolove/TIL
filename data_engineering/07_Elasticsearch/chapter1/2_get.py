from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 문서 조회 (ID: 1001, 인덱스: products)
response = es.get(index="products", id=1001)

# 결과 출력
print(response)
