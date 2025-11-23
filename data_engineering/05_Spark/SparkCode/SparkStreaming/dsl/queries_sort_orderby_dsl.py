from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("SortExample").getOrCreate()

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

# -----------------------------------------------
# [1] 단일 컬럼 정렬: column1 내림차순
# -----------------------------------------------
print("=== column1 DESC 정렬 ===")
df.sort(df["column1"].desc()).show()

# -----------------------------------------------
# [2] 다중 컬럼 정렬:
#     column1 오름차순, column2 내림차순
# -----------------------------------------------
print("=== column1 ASC, column2 DESC 정렬 ===")
df.orderBy(["column1", "column2"], ascending=[True, False]).show()
