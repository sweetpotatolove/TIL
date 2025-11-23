from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("SubstringBetweenSQL").getOrCreate()

# 예제 데이터 생성
data = [("ABCDEFG", 100), ("HIJKLMN", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# SQL 쿼리 실행을 위한 TempView 등록
df.createOrReplaceTempView("my_table")

# -----------------------------------------------------
# [1] SUBSTRING(column1, 2, 3) → 2번째부터 3글자 추출
# -----------------------------------------------------
print("=== SQL: SUBSTRING(column1, 2, 3) ===")
spark.sql("""
    SELECT SUBSTRING(column1, 2, 3) AS name
    FROM my_table
""").show()

# -----------------------------------------------------
# [2] column2 값이 50~150 범위에 포함되는지 확인 (BETWEEN)
# -----------------------------------------------------
print("=== SQL: column2 BETWEEN 50 AND 150 ===")
spark.sql("""
    SELECT column1, column2,
           column2 BETWEEN 50 AND 150 AS is_between_50_150
    FROM my_table
""").show()
