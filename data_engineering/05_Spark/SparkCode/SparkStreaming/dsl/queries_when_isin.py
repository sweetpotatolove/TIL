from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# SparkSession 생성
spark = SparkSession.builder.appName("WhenIsInExample").getOrCreate()

# 예제 데이터
data = [("A", 100), ("B", 200), ("C", 300)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# ---------------------------------------------
# [1] column2 > 100이면 1, 아니면 0 → flag 컬럼 생성
# ---------------------------------------------
print("=== when 조건 표현 ===")
df.select(
    "column1",
    when(df.column2 > 100, 1).otherwise(0).alias("flag")
).show()

# ---------------------------------------------
# [2] column1 값이 "A" 또는 "B"인 행만 필터링
# ---------------------------------------------
print("=== isin 필터링 ===")
df.filter(df.column1.isin("A", "B")).show()
