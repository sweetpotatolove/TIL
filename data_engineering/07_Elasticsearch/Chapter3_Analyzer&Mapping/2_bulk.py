from elasticsearch import Elasticsearch, helpers

# Elasticsearch 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

# Bulk로 넣을 데이터 정의
documents = [
    { "_id": 1, "name": "Samsung Galaxy S25", "brand": "Samsung", "price": 1199.99, "category": "smartphone", "rating": 4.8 },
    { "_id": 2, "name": "iPhone 15 Pro", "brand": "Apple", "price": 1299.99, "category": "smartphone", "rating": 4.3 },
    { "_id": 3, "name": "Google Pixel 8", "brand": "Google", "price": 999.99, "category": "smartphone", "rating": 4.6 },
    { "_id": 4, "name": "MacBook Air M3", "brand": "Apple", "price": 1399.00, "category": "notebook", "rating": 4.7 },
    { "_id": 5, "name": "Galaxy Book3", "brand": "Samsung", "price": 1190.50, "category": "notebook", "rating": 4.5 },
    { "_id": 6, "name": "LG Gram 17", "brand": "LG", "price": 1490.00, "category": "notebook", "rating": 4.3 },
    { "_id": 7, "name": "Sony Xperia 1 V", "brand": "Sony", "price": 1099.99, "category": "smartphone", "rating": 4.4 },
    { "_id": 8, "name": "ASUS ZenBook 14", "brand": "ASUS", "price": 1090.00, "category": "notebook", "rating": 4.2 },
    { "_id": 9, "name": "Motorola Edge 40", "brand": "Motorola", "price": 899.00, "category": "mobile", "rating": 4.1 },
    { "_id": 10, "name": "Huawei MateBook X", "brand": "Huawei", "price": 999.99, "category": "laptop", "rating": 4.0 },
    { "_id": 11, "name": "삼성 갤럭시 울트라", "brand": "Samsung", "price": 1499.99, "category": "smartphone", "rating": 4.9 },
    { "_id": 12, "name": "Galaxy Ultra", "brand": "Samsung", "price": 1489.99, "category": "smartphone", "rating": 4.7 },
    { "_id": 13, "name": "삼성갤럭시 울트라 출시", "brand": "Samsung", "price": 1479.99, "category": "smartphone", "rating": 4.6 }
]


# Bulk API 요청용 구조로 변환
actions = [
    {
        "_index": "products_chapter3",
        "_id": doc["_id"],
        "_source": {k: v for k, v in doc.items() if k != "_id"}
    }
    for doc in documents
]

# Bulk 삽입 실행
helpers.bulk(es, actions)
print("Bulk insert completed.")
