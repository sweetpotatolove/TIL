from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("CSVDataFrameExample").getOrCreate()

# people.txt 파일을 읽어와 DataFrame 생성
people_df = spark.read.option("header", "false") \
                      .option("inferSchema", "true") \
                      .csv("people.txt") \
                      .toDF("name", "age")

# 결과 출력
people_df.show()
