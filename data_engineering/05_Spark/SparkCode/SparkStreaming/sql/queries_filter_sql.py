from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("SQLFilterExample").getOrCreate()

# 예제 데이터 생성
data = [
    ("A", 100),
    ("B", 200),
    ("A", 300),
    ("A", 400),
    ("A", 500)
]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# SQL 쿼리 사용을 위한 TempView 등록
df.createOrReplaceTempView("my_table")

# -------------------------------------------
# column2 > 200 조건에 해당하는 행만 필터링
# -------------------------------------------
print("=== SQL WHERE column2 > 200 ===")
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column2 > 200
""").show()
