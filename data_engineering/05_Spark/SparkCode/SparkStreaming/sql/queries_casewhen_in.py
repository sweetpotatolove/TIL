from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("CaseWhenAndInSQL").getOrCreate()

# 예제 데이터
data = [("A", 100), ("B", 200), ("C", 300)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# TempView 등록 (SQL 쿼리 사용을 위해)
df.createOrReplaceTempView("my_table")

# 1. CASE WHEN: column2 > 100 → 1, else 0
print("=== SQL CASE WHEN ===")
spark.sql("""
    SELECT column1,
           CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag
    FROM my_table
""").show()

# 2. IN 조건: column1이 A 또는 B인 행 필터링
print("=== SQL IN 조건 ===")
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column1 IN ('A', 'B')
""").show()
