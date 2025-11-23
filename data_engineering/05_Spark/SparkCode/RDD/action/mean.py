from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MeanExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([2, 4, 1])

# 평균 계산 (action)
y = x.mean()

print(x.collect())
print(y)  # 결과: 2.333...
