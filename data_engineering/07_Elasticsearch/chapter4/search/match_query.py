from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "_source": ["product_id", "name", "description"],
    "query": {
        "match": {
            "description": "AI"
        }
    }
}

res = es.search(index="products", body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")

query = {
    "_source": ["product_id", "name", "brand"],
    "query": {
        "match": {
            "name": {
                "query": "Samsung Neo",
                "operator": "AND"
            }
        }
    }
}

res = es.search(index="products", body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")

query = {
    "_source": ["product_id", "name", "brand"],
    "query": {
        "match_phrase": {
            "name": "Samsung Neo"
        }
    }
}

res = es.search(index="products", body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")

query = {
    "_source": ["product_id", "name", "brand"],
    "query": {
        "match_phrase_prefix": {
            "name": "Samsung N"
        }
    }
}

res = es.search(index="products", body=query)

for hit in res["hits"]["hits"]:
    print(hit["_source"])
