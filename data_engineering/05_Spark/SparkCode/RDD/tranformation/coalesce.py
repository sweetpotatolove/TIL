from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RepartitionCoalesce").getOrCreate()
sc = spark.sparkContext

# 3개의 파티션으로 초기 분할
x = sc.parallelize([1, 2, 3, 4, 5], 3)

# coalesce: 파티션 수 줄이기 (최대한 셔플 없이)
y = x.coalesce(2)

print(x.glom().collect())  # 기존 파티션별 값
print(y.glom().collect())  # 줄인 파티션 확인
