from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SumExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([2, 4, 1])

# 전체 합 계산 (action)
y = x.sum()

print(x.collect())
print(y)  # 결과: 7.0 (float 반환)
