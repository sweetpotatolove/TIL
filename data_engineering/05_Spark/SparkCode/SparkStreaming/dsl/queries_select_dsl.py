from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder.appName("SelectWithExpressions").getOrCreate()

# 예제 데이터 생성
data = [("A", 100), ("B", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# ---------------------------------------------------
# [1] column1 그대로 + column2 + 1을 계산하여 출력
# ---------------------------------------------------
print("=== column2 + 1 결과 ===")
df.select(
    col("column1"),
    (col("column2") + 1).alias("column2_plus1")
).show()

# ---------------------------------------------------
# [2] column1이 "A"보다 큰 값 필터링 (문자열 기준)
# ---------------------------------------------------
print('=== column1 > "A" 조건 필터링 ===')
df.filter(col("column1") > "A").show()
