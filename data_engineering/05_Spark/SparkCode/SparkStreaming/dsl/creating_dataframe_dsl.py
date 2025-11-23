from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# SparkSession 생성
spark = SparkSession.builder.appName("ExampleApp").getOrCreate()

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# 문자열 기반 RDD 생성
parts = spark.sparkContext.parallelize([
    ("Mine", "28"), 
    ("Filip", "29"), 
    ("Jonathan", "30")
])

# 문자열 나이(age)를 정수형으로 변환하여 Row 객체로 매핑
people = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))

# 명시적 스키마를 사용하여 DataFrame 생성
df = spark.createDataFrame(people, schema)

# 결과 출력
df.show()
