from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("FilterExample").getOrCreate()

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

# ------------------------------------------
# column2 값이 200보다 큰 행만 필터링
# ------------------------------------------
print("=== column2 > 200 조건 필터링 ===")
df.filter(df["column2"] > 200).show()
