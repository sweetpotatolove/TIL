from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "_source": ["name", "category"],
    "query": {
        "exists": {
            "field": "description"
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과] description 필드가 존재하는 문서:")
for hit in response["hits"]["hits"]:
    print(hit["_source"])