from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("UnionExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([1, 2, 3], 2)
y = sc.parallelize([3, 4], 1)

# union: RDD 합치기 (파티션 정보도 병합됨)
z = x.union(y)

print(z.glom().collect())  # 파티션별로 출력
