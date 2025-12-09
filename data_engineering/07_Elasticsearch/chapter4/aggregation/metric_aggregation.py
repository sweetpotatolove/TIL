from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "size": 0,
    "aggs": {
        "average_price": {
            "avg": {
                "field": "price"
            }
        }
    }
}

response = es.search(index="products", body=query)

# 집계 결과 추출
avg_price = response["aggregations"]["average_price"]["value"]
print(f"[평균 가격] {avg_price:.2f}")
