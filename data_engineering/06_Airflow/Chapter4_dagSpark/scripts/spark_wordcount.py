# PySpark 세션 관련 모듈 및 함수 import
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import os
import shutil
import datetime

# ------------------------
# 1. SparkSession 생성
# ------------------------
spark = SparkSession.builder \
    .appName("DataFrameTest") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# ------------------------
# 2. 테스트용 데이터 생성
# ------------------------
# 학생 이름(name), 과목(subject), 점수(score)로 구성된 튜플 리스트 생성
data = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 90),
    ("Alice", "English", 78),
    ("Bob", "English", 83),
    ("Alice", "Science", 92),
    ("Bob", "Science", 87)
]

# 데이터프레임 컬럼명 정의
columns = ["name", "subject", "score"]

# 리스트 데이터를 기반으로 Spark DataFrame 생성
df = spark.createDataFrame(data, columns)

# ------------------------
# 3. 데이터 집계 (GroupBy + Aggregation)
# ------------------------
# 학생 이름(name)별로 그룹화(groupBy)하여 평균 점수(average_score) 계산
avg_scores = df.groupBy("name").agg(avg("score").alias("average_score"))

# 결과를 콘솔에 출력 (Spark UI에서도 확인 가능)
avg_scores.show()

# ------------------------
# 4. 결과를 CSV 파일로 저장
# ------------------------

# 출력 경로 설정 (file:// 프로토콜 사용 → 로컬 파일시스템 기준)
output_path = "file:///opt/shared/output"

# DataFrame을 CSV 포맷으로 저장
# - coalesce(1): 하나의 파일(part-*.csv)로 합쳐 저장
# - mode="append": 기존 파일이 있어도 덮어쓰지 않고 이어서 추가
# - header=True: 컬럼명을 CSV 첫 줄에 추가
avg_scores.coalesce(1).write.mode("append").csv(output_path, header=True)

# ------------------------
# 5. 세션 종료 및 리소스 정리
# ------------------------

# Spark의 메타데이터 캐시 초기화
spark.catalog.clearCache()

# SparkContext(실제 클러스터와 통신하는 엔진) 종료
spark.sparkContext.stop()
