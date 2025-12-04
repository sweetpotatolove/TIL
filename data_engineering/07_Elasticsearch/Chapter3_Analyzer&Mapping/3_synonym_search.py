from elasticsearch import Elasticsearch

# Elasticsearch 연결
es = Elasticsearch("http://localhost:9200")

# 검색 쿼리 정의 (예: '모바일' 검색 시 synonym 매칭)
query = {
    "query": {
        "match": {
            "category": "모바일"
        }
    }
}

# 검색 실행
res = es.search(index="products_chapter3", body=query)

# 결과 출력
print("검색 결과:")
for hit in res["hits"]["hits"]:
    print(f"- _id: {hit['_id']}, name: {hit['_source']['name']}")
