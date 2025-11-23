from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder.appName("StringConditionsExample").getOrCreate()

# 예제 데이터
data = [("A", 100), ("B", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# ----------------------------------------------------
# [1] column1이 "A"로 시작하는지 확인 (startswith)
# ----------------------------------------------------
print("=== startswith('A') ===")
df.select(
    col("column1"),
    col("column1").startswith("A").alias("starts_with_A")
).show()

# ----------------------------------------------------
# [2] column2가 "00"으로 끝나는지 확인 (endswith)
# → 정수형을 문자열로 변환 필요
# ----------------------------------------------------
print("=== endswith('00') ===")
df.select(
    col("column2"),
    col("column2").cast("string").endswith("00").alias("ends_with_00")
).show()

# ----------------------------------------------------
# [3] column1이 정확히 "A"와 일치하는지 확인 (like)
# ----------------------------------------------------
print("=== like('A') ===")
df.select(
    col("column1"),
    col("column1").like("A").alias("is_A")
).show()
