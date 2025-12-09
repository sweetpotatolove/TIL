from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "_source": ["name", "category"],
    "query": {
        "query_string": {
            "query": "name:Apple"
        }
    }
}

res = es.search(index="products", body=query)

print("[검색 결과] name 필드에 'Apple'이 포함된 문서:")
for hit in res["hits"]["hits"]:
    print(hit["_source"])

