from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("GroupByCountSQL").getOrCreate()

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

# SQL 실행을 위해 TempView 등록
df.createOrReplaceTempView("my_table")

# -----------------------------------------------
# [1] SQL 방식: column1 기준으로 그룹화 후 개수 집계
# -----------------------------------------------
print("=== SQL GROUP BY + COUNT ===")
spark.sql("""
    SELECT column1, COUNT(*) AS count
    FROM my_table
    GROUP BY column1
""").show()
