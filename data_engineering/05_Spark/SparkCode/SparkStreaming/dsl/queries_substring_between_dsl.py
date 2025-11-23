from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder.appName("SubstringAndBetweenExample").getOrCreate()

# 예제 데이터
data = [("ABCDEFG", 100), ("HIJKLMN", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# --------------------------------------------------
# [1] column1에서 2번째 문자부터 3글자 추출 → name 컬럼
# --------------------------------------------------
print("=== Substring 추출 ===")
df.select(
    df.column1.substr(2, 3).alias("name")
).show()

# --------------------------------------------------
# [2] column2 값이 50~150 사이인지 확인 (between)
# --------------------------------------------------
print("=== between(50, 150) 조건 ===")
df.select(
    col("column1"),
    col("column2"),
    col("column2").between(50, 150).alias("is_between_50_150")
).show()
