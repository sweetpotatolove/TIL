from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("RenameDropSQL").getOrCreate()

# 예제 데이터 생성
data = [("ABCDEFG", 100), ("HIJKLMN", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# SQL 쿼리를 위해 TempView 등록
df.createOrReplaceTempView("my_table")

# ---------------------------------------------
# [1] 컬럼 이름 변경 (AS 사용)
# column1 → alphabet, column2 → number
# ---------------------------------------------
print("=== 컬럼 이름 변경 (AS) ===")
spark.sql("""
    SELECT column1 AS alphabet, column2 AS number
    FROM my_table
""").show()

# ---------------------------------------------
# [2] 컬럼 제거 (원하는 컬럼만 SELECT)
# column1 제거 = column2만 선택
# ---------------------------------------------
print("=== column1 제거 ===")
spark.sql("""
    SELECT column2
    FROM my_table
""").show()
