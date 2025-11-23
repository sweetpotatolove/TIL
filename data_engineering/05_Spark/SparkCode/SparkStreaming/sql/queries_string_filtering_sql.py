from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("StringSQLConditions").getOrCreate()

# 예제 데이터 생성
data = [("A", 100), ("B", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# SQL 사용을 위한 TempView 등록
df.createOrReplaceTempView("my_table")

# -----------------------------------------------
# [1] column1이 'A'로 시작하는 경우 (LIKE 'A%')
# -----------------------------------------------
print("=== STARTSWITH: column1 LIKE 'A%' ===")
spark.sql("""
    SELECT column1, column1 LIKE 'A%' AS starts_with_A
    FROM my_table
""").show()

# -----------------------------------------------------
# [2] column2가 "00"으로 끝나는 경우 (LIKE '%00')
# 숫자 컬럼이므로 CAST(column2 AS STRING) 필요
# -----------------------------------------------------
print("=== ENDSWITH: column2 LIKE '%00' ===")
spark.sql("""
    SELECT column2,
           CAST(column2 AS STRING) LIKE '%00' AS ends_with_00
    FROM my_table
""").show()

# -----------------------------------------------------
# [3] column1이 'A'와 정확히 일치하는 경우 (= 'A')
# -----------------------------------------------------
print("=== EXACT MATCH: column1 = 'A' ===")
spark.sql("""
    SELECT column1, column1 = 'A' AS is_A
    FROM my_table
""").show()
