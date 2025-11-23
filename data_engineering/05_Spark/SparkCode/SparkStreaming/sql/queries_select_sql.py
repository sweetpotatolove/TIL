from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("SQLSelectExpressions").getOrCreate()

# 예제 데이터
data = [("A", 100), ("B", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# TempView 등록 (SQL 사용을 위해)
df.createOrReplaceTempView("my_table")

# ----------------------------------------------
# [1] SELECT with expression (column2 + 1)
# ----------------------------------------------
print("=== SQL: column2 + 1 AS column2_plus1 ===")
spark.sql("""
    SELECT column1, column2 + 1 AS column2_plus1
    FROM my_table
""").show()

# ----------------------------------------------
# [2] WHERE 조건 필터링 (column1 > 'A')
# ----------------------------------------------
print("=== SQL: WHERE column1 > 'A' ===")
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column1 > 'A'
""").show()
