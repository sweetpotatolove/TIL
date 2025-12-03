from elasticsearch import Elasticsearch, NotFoundError, helpers
import json

# Elasticsearch 클라이언트 생성
es = Elasticsearch("http://localhost:9200")

# ----------------------------------------------
# 1. 기존 'products' 인덱스 삭제 (초기화)
# ----------------------------------------------
try:
    es.indices.delete(index="products")
    print("1. 'products' 인덱스 삭제 완료")
except NotFoundError:
    print("1. 삭제할 인덱스가 없음 (이미 삭제된 상태)")

# ----------------------------------------------
# Bulk Insert 실행
# ----------------------------------------------
bulk_insert_data = [
    {"_index": "products", "_id": "1", "_source": {
        "product_name": "Samsung Galaxy S25", "brand": "Samsung", "release_date": "2025-02-07", "price": 799}},
    {"_index": "products", "_id": "2", "_source": {
        "product_name": "iPhone 15 Pro", "brand": "Apple", "release_date": "2024-10-13", "price": 1199}},
    {"_index": "products", "_id": "3", "_source": {
        "product_name": "Google Pixel 8", "brand": "Google", "release_date": "2023-10-12", "price": 260}},
]

helpers.bulk(es, bulk_insert_data)
# 강제로 색인 refresh
es.indices.refresh(index="products")

print("3Bulk 문서 삽입 완료")

# ----------------------------------------------
# 삽입된 문서 확인
# ----------------------------------------------
print("삽입된 문서:")
res = es.search(index="products", query={"match_all": {}})
for hit in res["hits"]["hits"]:
    print(hit["_source"])