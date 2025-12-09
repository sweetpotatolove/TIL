import pandas as pd
from elasticsearch import Elasticsearch, helpers
import numpy as np

# Elasticsearch 연결
es = Elasticsearch("http://localhost:9200")

index_name = "air_quality"

# 매핑 생성
mapping = {
    "mappings": {
        "properties": {
            "Unique_ID":         { "type": "keyword" },
            "Indicator_ID":      { "type": "keyword" },
            "Name":              { "type": "text" },
            "Measure":           { "type": "keyword" },
            "Measure_Info":      { "type": "text" },
            "Geo_Type_Name":     { "type": "keyword" },
            "Geo_Join_ID":       { "type": "keyword" },
            "Geo_Place_Name":    { "type": "text" },
            "Time_Period":       { "type": "keyword" },
            "Start_Date":        { "type": "date", "format": "MM/dd/yyyy" },
            "Data_Value":        { "type": "float" },
            "@timestamp":        { "type": "date" }
        }
    }
}

# 기존 인덱스 삭제 후 생성
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
es.indices.create(index=index_name, body=mapping)

# CSV 로드
df = pd.read_csv("./data/Air_Quality.csv")

# 컬럼 정리
df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# 날짜 처리: Elasticsearch 매핑 포맷에 맞춰 문자열 처리
df["Start_Date"] = pd.to_datetime(df["Start_Date"], errors="coerce").dt.strftime("%m/%d/%Y")

df["@timestamp"] = pd.to_datetime(df["Start_Date"], format="%m/%d/%Y", errors="coerce")

df["Data_Value"] = pd.to_numeric(df["Data_Value"], errors="coerce")

# 사용하지 않을 행 제거
df = df[df["Unique_ID"] != "Unique ID"]  # 중복 헤더 제거
df = df.dropna(subset=["Start_Date", "Data_Value"])  # 필수 필드 누락 제거

# Bulk용 제너레이터
def doc_generator(df):
    for _, row in df.iterrows():
        doc = row.dropna().to_dict()
        yield {
            "_index": index_name,
            "_source": doc
        }

# Bulk 적재
try:
    helpers.bulk(es, doc_generator(df))
    print(f"{len(df)}건 인덱싱 완료")
except helpers.BulkIndexError as e:
    print(f"{len(e.errors)}건 인덱싱 실패")
    for i, err in enumerate(e.errors[:5]):
        print(f"[{i+1}] 오류: {err}")
