from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "size": 0,
    "aggs": {
        "by_brand": {
            "terms": {
                "field": "brand",
                "size": 10
            }
        }
    }
}

response = es.search(index="products", body=query)

# 결과 출력
print("[브랜드별 문서 수]")
for bucket in response["aggregations"]["by_brand"]["buckets"]:
    print(f"- {bucket['key']}: {bucket['doc_count']}건")
