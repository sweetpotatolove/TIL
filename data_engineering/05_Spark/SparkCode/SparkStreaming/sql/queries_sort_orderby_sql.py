from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("SQLSortExample").getOrCreate()

# 예제 데이터
data = [
    ("A", 100),
    ("B", 200),
    ("A", 300),
    ("A", 400),
    ("A", 500)
]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# TempView 등록 (SQL 쿼리에서 사용 가능하도록)
df.createOrReplaceTempView("my_table")

# -------------------------------------------------------
# [1] 단일 컬럼 정렬: column1 기준 내림차순 (DESC)
# -------------------------------------------------------
print("=== SQL ORDER BY column1 DESC ===")
spark.sql("""
    SELECT *
    FROM my_table
    ORDER BY column1 DESC
""").show()

# -------------------------------------------------------
# [2] 다중 컬럼 정렬: column1 오름차순, column2 내림차순
# -------------------------------------------------------
print("=== SQL ORDER BY column1 ASC, column2 DESC ===")
spark.sql("""
    SELECT *
    FROM my_table
    ORDER BY column1 ASC, column2 DESC
""").show()
