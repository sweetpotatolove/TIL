from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SampleExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([1, 2, 3, 4, 5])

# 샘플링: False = 비복원 추출, 비율 0.4, seed=42
y = x.sample(False, 0.4, 42)

print(x.collect())
print(y.collect())
