from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example1").getOrCreate()
sc = spark.sparkContext

# 문자 리스트를 RDD로 생성
x = sc.parallelize(["b", "a", "c"])

# 각 요소를 (문자, 1) 형태로 변환
y = x.map(lambda z: (z, 1))

# 원본 데이터 출력
print(x.collect())

# 매핑된 결과 출력
print(y.collect())
