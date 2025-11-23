from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("DataFrameConversion").getOrCreate()

# 샘플 데이터프레임 생성
data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)

# 1. DataFrame → RDD
rdd1 = df.rdd
print("=== RDD 출력 ===")
print(rdd1.collect())

# 2. DataFrame → JSON 문자열 → 첫 번째 항목 확인
json_string = df.toJSON().first()
print("=== JSON 문자열 첫 항목 ===")
print(json_string)

# 3. DataFrame → Pandas DataFrame
pandas_df = df.toPandas()
print("=== Pandas DataFrame ===")
print(pandas_df)
