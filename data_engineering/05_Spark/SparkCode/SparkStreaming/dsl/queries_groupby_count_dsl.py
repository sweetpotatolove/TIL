from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("GroupByCountExample").getOrCreate()

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

# -----------------------------------------
# [1] column1 기준으로 그룹화하고 각 그룹의 개수 계산
# -----------------------------------------
print("=== GroupBy column1 + Count ===")
df.groupBy("column1").count().show()
