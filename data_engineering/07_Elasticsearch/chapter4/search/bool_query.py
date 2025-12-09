from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "_source": ["name", "brand", "description"],
    "query": {
        "bool": {
            "must": [
                { "match": { "brand": "Samsung" } },
                { "match": { "description": "AI" } }
            ]
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과] 브랜드가 'Samsung'이고 description에 'AI'가 포함된 문서:")
for hit in response["hits"]["hits"]:
    doc = hit["_source"]
    print(f"- {doc['name']} ({doc['brand']}) : {doc['description']}")



query = {
    "_source": ["name", "brand", "description"],
    "query": {
        "bool": {
            "must_not": [
                { "match": { "brand": "Apple" } }
            ]
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과] 브랜드가 'Apple'이 아닌 문서들:")
for i, hit in enumerate(response["hits"]["hits"]):
    doc = hit["_source"]
    print(f" [{i+1}]- {doc['name']} ({doc['brand']}) : {doc['description']}")
