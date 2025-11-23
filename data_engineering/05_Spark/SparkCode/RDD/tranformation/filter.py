from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example3").getOrCreate()
sc = spark.sparkContext

# 1~3 숫자 리스트
x = sc.parallelize([1, 2, 3])

# 홀수만 유지하는 필터
y = x.filter(lambda x: x % 2 == 1)

print(x.collect())  # 전체
print(y.collect())  # 필터링 결과
