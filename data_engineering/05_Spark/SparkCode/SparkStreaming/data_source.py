from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("ReadVariousFormats").getOrCreate()

# JSON 파일 읽기
df_json_1 = spark.read.json("filename.json")
df_json_2 = spark.read.load("filename.json", format="json")

print("=== JSON 1 (read.json) ===")
df_json_1.show()

print("=== JSON 2 (read.load with format=json) ===")
df_json_2.show()

# Parquet 파일 읽기
df_parquet = spark.read.parquet("filename.parquet")
# 또는
# df_parquet = spark.read.load("filename.parquet")

print("=== Parquet ===")
df_parquet.show()

# 텍스트 파일 읽기
df_txt = spark.read.text("filename.txt")

print("=== Text File ===")
df_txt.show()
