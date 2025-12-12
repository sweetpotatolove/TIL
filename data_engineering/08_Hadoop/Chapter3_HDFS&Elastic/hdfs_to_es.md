# HDFS → Elasticsearch 흐름 정리리 (인덱스 매핑 및 bulk 업로드 포함)

HDFS에서 PySpark로 데이터를 읽고, JSON으로 저장한 후 Elasticsearch에 매핑 설정과 함께 bulk 업로드하는 전체 과정을 설명합니다.

---

## 디렉토리 구성 예시

```bash
/home/my/my_hadoop/chapter3/
  ├── test_read_hdfs.py        # HDFS CSV → JSON 저장
  ├── upload_to_es.py          # JSON → Elasticsearch 업로드 및 인덱스 매핑
  └── transactions.csv
```


## 1. 사전 조건

- Hadoop(HDFS) 정상 실행 중 (`hdfs dfs -ls` 등으로 확인)
- Elasticsearch 8.17 실행 중 (`http://localhost:9200`)
- PySpark 3.5.4

```bash
hadoop fs -mkdir -p /user/local/hadoop_data
hadoop fs -put transactions.csv /user/local/hadoop_data/transactions.csv
hadoop fs -ls /user/local/hadoop_data
```

---

## 2. test_read_hdfs.py (Spark로 JSON 저장)

```python
from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .appName("Read HDFS CSV") \
    .master("local[*]") \
    .getOrCreate()

# HDFS의 CSV 파일 읽기
df = spark.read.option("header", "true").csv("hdfs://localhost:9000/user/local/hadoop_data/transactions.csv")

# 데이터 출력 (검증용)
df.show()

# JSON 파일로 로컬 디스크에 저장
df.write.mode("overwrite").json("file:///home/my/hadoop_data/transactions")
```

실행:

```bash
python test_read_hdfs.py
```

### 참고

- Spark로 JSON 저장 시 기본적으로 `part-*.json` 파일들이 생성
- 해당 데이터를 읽어 Elasticsearch에 문서 형태로 저장


---

## 3. upload_to_es.py (인덱스 매핑 + bulk 업로드)

### 인덱스 생성 및 매핑 정의

```python
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
```

---

### bulk 데이터 업로드

```python
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
```

실행

```bash
python upload_to_es.py
```

---

## 4. 결과 확인

### Elasticsearch API

```bash
curl -XGET 'localhost:9200/finance-transactions/_search?pretty'
```

또는 Kibana 접속 후 아래 경로 확인:

- **Stack Management > Index Management** 에서 `finance-transactions` 존재 확인
- **Discover** 메뉴에서 데이터 탐색 가능
- **Data View** 생성 시: `finance-transactions`, `finance-transactions-*`,`transaction_date`  으로 지정

---

## 5. Kibana 시각화 예시

- 시간 흐름에 따른 거래 수 변화
- 카테고리 별 거래 비율 파악
- 금액이 300 초과인 거래 필터링 (예: `amount > 300`)
- 날짜별 거래 건수 분석

---

## 6. 확장 가능 요소

- Airflow DAG 구성하여 ETL 자동화
- Spark Dataframe or SQL 기반 데이터 전처리 적용
- Kafka 연계 실시간 적재 구조

---

