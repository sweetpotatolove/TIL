from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example5").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([1, 2, 3], 2)

# 파티션 번호와 해당 파티션의 합계를 튜플로 반환
def f(partitionIndex, iterator):
    yield (partitionIndex, sum(iterator))

y = x.mapPartitionsWithIndex(f)

print(x.glom().collect())  # 파티션별 데이터
print(y.glom().collect())  # (파티션 번호, 합계)
