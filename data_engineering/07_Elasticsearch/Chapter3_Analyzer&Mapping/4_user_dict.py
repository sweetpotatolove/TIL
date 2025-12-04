from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = {
    "query": {
        "match": {
            "name": {
                "query": "삼성 갤럭시",          # 사용자 사전에서 등록된 복합어
                "analyzer": "user_dic_analyzer",  # 사용자 정의 분석기 사용
                "operator": "and"
            }
        }
    }
}

res = es.search(index="products_chapter3", body=query)

print("검색 결과:")
for hit in res["hits"]["hits"]:
    print(f"- {hit['_id']}: {hit['_source']['name']}")
