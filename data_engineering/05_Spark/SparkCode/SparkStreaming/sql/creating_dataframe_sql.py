from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# SparkSession 생성
spark = SparkSession.builder.appName("SQLViewExample").getOrCreate()

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# RDD 생성 및 전처리
parts = spark.sparkContext.parallelize([
    ("Mine", "28"),
    ("Filip", "29"),
    ("Jonathan", "30")
])
people = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))

# DataFrame 생성
df = spark.createDataFrame(people, schema)

# DataFrame을 SQL에서 사용할 수 있도록 TempView 등록
df.createOrReplaceTempView("people")

# Spark SQL로 조회
result = spark.sql("""
    SELECT name, age
    FROM people
""")

# 결과 출력
result.show()
