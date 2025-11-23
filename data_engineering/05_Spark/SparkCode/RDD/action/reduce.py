from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReduceExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([1, 2, 3, 4])

# reduce: 누적 계산 – a + b 형태로 진행됨
y = x.reduce(lambda a, b: a + b)

print(x.collect())
print(y)  # 결과: 10
