from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "query": {
        "match": {
            "brand": "Samsung"
        }
    }
}

res = es.search(index="products", body=query)

print("[검색 결과] brand가 'Samsung'인 문서:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")


query = {
    "_source": ["name", "brand"],
    "query": {
        "terms": {
            "brand": ["Samsung", "Apple"]
        }
    }
}

res = es.search(index="products", body=query)

print("[검색 결과] Samsung 또는 Apple 브랜드:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")


query = {
    "_source": ["product_id", "name", "brand", "price"],
    "query": {
        "bool": {
            "must": [
                {
                    "terms": {
                        "brand": ["Samsung", "Sony"]
                    }
                },
                {
                    "range": {
                        "price": {
                            "gte": 2000,
                            "lte": 3000
                        }
                    }
                }
            ]
        }
    }
}

res = es.search(index="products", body=query)

print("[검색 결과] Samsung 또는 Sony 이면서 가격이 2000~3000 사이:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])
