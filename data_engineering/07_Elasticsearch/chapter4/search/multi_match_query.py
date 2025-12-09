from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "_source": ["product_id", "name", "brand", "description"],
    "query": {
        "multi_match": {
            "query": "Samsung",
            "fields": ["name", "description"],
            "type": "best_fields",
            "operator": "or"
        }
    }
}

res = es.search(index="products", body=query)
for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")


query = {
    "_source": ["product_id", "name", "brand", "description"],
    "query": {
        "multi_match": {
            "query": "Samsung",
            "fields": ["name", "description"],
            "type": "most_fields",
            "operator": "or"
        }
    }
}

res = es.search(index="products", body=query)
for hit in res["hits"]["hits"]:
    print(hit["_source"])
print("---------------------------------------------")


query = {
    "_source": ["product_id", "name", "brand", "description"],
    "query": {
        "multi_match": {
            "query": "Samsung Ultra",
            "fields": ["name", "description"],
            "type": "cross_fields",
            "operator": "and"
        }
    }
}

res = es.search(index="products", body=query)
for hit in res["hits"]["hits"]:
    print(hit["_source"])