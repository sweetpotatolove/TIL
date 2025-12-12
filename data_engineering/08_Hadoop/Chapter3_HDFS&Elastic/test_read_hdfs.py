from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .appName("Read HDFS CSV") \
    .master("local[*]") \
    .getOrCreate()

# HDFS의 CSV 파일 읽기
df = spark.read.option("header", "true").csv("hdfs://localhost:9000/user/local/hadoop_data/transactions.csv")

# 데이터 출력 (검증용)
df.show()

# JSON 파일로 로컬 디스크에 저장
df.write.mode("overwrite").json("file:///home/my/hadoop_data/transactions")
