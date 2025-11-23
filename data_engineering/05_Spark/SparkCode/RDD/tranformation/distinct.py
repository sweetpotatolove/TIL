from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DistinctExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([1, 2, 3, 3, 4])

# 중복 제거
y = x.distinct()

print(y.collect())
