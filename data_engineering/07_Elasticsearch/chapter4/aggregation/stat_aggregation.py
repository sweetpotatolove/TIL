from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "size": 0,
    "query": {
        "term": {
            "brand": "Samsung"
        }
    },
    "aggs": {
        "price_stats": {
            "stats": {
                "field": "price"
            }
        }
    }
}

response = es.search(index="products", body=query)

# 결과 출력
stats = response["aggregations"]["price_stats"]
print("[Samsung 제품 가격 통계]")
print(f" - count : {stats['count']}")
print(f" - min   : {stats['min']}")
print(f" - max   : {stats['max']}")
print(f" - avg   : {stats['avg']:.2f}")
print(f" - sum   : {stats['sum']}")
