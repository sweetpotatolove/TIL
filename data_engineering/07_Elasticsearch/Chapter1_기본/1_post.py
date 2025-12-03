from elasticsearch import Elasticsearch

# 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# 문서 삽입
doc = {
    "name": "Samsung Galaxy S24 Ultra",
    "brand": "Samsung",
    "price": 1199.99,
    "category": "smartphone",
    "rating": 4.8
}

response = es.index(index="products", id=1001, document=doc)

# 결과 출력
print(response)
