from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("CSVtoSQLView").getOrCreate()

# CSV 파일을 읽어서 DataFrame 생성
people_df = spark.read.option("header", "false") \
                      .option("inferSchema", "true") \
                      .csv("people.txt") \
                      .toDF("name", "age")

# TempView 등록
people_df.createOrReplaceTempView("people")

# SQL 쿼리로 조회
result = spark.sql("""
    SELECT name, age
    FROM people
""")

# 출력 확인
result.show()
