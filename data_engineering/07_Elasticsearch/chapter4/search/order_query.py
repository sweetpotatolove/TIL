from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")


response = es.search(
    index="products",
    body={
        "sort": [
            {
                "price": {
                    "order": "desc"
                }
            }
        ]
    }
)

print("[products 인덱스 - price 내림차순 정렬 결과]")
for hit in response["hits"]["hits"]:
    print(hit["_source"])
