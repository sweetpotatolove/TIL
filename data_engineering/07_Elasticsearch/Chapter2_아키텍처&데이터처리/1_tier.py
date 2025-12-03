from elasticsearch import Elasticsearch
import time

es = Elasticsearch("http://localhost:9200")
index_name = "logs-000001"

print(es.cat.nodes(format="text", h="name,roles"))

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

es.indices.create(index=index_name, body={
    "settings": {
        "index.number_of_replicas": 0,
        "index.routing.allocation.include._tier_preference": "data_hot"
    }
})

print(es.cat.shards(index=index_name, format="text"))

time.sleep(60)

es.indices.put_settings(index=index_name, body={
    "index.routing.allocation.include._tier_preference": "data_warm"
})
time.sleep(10)

print(es.cat.shards(index=index_name, format="text"))

time.sleep(60)

es.indices.put_settings(index=index_name, body={
    "index.routing.allocation.include._tier_preference": "data_cold"
})
time.sleep(10)

print(es.cat.shards(index=index_name, format="text"))
