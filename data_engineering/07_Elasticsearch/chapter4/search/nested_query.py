from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "query": {
        "nested": {
            "path": "features",
            "query": {
                "term": {
                    "features.feature_name": "Camera"
                }
            }
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과]")
for hit in response["hits"]["hits"]:
    source = hit["_source"]
    print(f"- {source['name']} ({source['brand']})")


query = {
    "query": {
        "nested": {
            "path": "features",
            "query": {
                "bool": {
                    "must": [
                        { "term": { "features.feature_name": "RAM" }},
                        { "term": { "features.feature_value": "16GB" }}
                    ]
                }
            }
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과] RAM = 16GB")
for hit in response["hits"]["hits"]:
    doc = hit["_source"]
    print(f"- {doc['name']} ({doc['brand']})")


query = {
    "query": {
        "bool": {
            "must": [
                { "term": { "features.feature_name": "RAM" }},
                { "term": { "features.feature_value": "16GB" }}
            ]
        }
    }
}

response = es.search(index="products", body=query)

print("[검색 결과] RAM이라는 이름과 16GB라는 값이 존재하는 문서 (nested 아님)")
for hit in response["hits"]["hits"]:
    doc = hit["_source"]
    print(f"- {doc['name']} ({doc['brand']})")
