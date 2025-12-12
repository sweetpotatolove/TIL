from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import RequestError
import os, json

# 1. Elasticsearch 연결
es = Elasticsearch("http://localhost:9200")

# 2. JSON 파일 경로 및 인덱스 이름
data_dir = "/home/my/hadoop_data/transactions"
index_name = "finance-transactions"

# 3. 매핑 정의
index_mapping = {
    "mappings": {
        "properties": {
            "transaction_id":   { "type": "keyword" },
            "transaction_date": { "type": "date", "format": "yyyy-MM-dd||strict_date_optional_time" },
            "amount":           { "type": "float" },
            "category":         { "type": "keyword" }
        }
    }
}

# 4. 인덱스 생성 시도
try:
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=index_mapping)
        print(f"[INFO] 새 인덱스 [{index_name}] 생성 완료")
except RequestError as e:
    print(f"[ERROR] 인덱스 생성 오류: {e.info}")

# 5. JSON 파일 수집
json_files = [
    os.path.join(data_dir, f)
    for f in os.listdir(data_dir)
    if f.startswith("part-") and f.endswith(".json")
]

# 6. bulk action 구성
actions = []
for file_path in json_files:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            actions.append({
                "_index": index_name,
                "_source": doc
            })

# 7. Elasticsearch로 업로드
if actions:
    response = helpers.bulk(es, actions)
    print(f"[SUCCESS] {len(actions)} documents indexed to [{index_name}]")
else:
    print("[WARN] No documents found to index.")
