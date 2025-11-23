from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PartitionByExample").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize([('J', 'James'), ('F', 'Fred'), ('A', 'Anna'), ('J', 'James')], 3)

# key 기준으로 파티션 분기: 'H'보다 작으면 파티션 0, 그 외는 파티션 1
y = x.partitionBy(2, lambda w: 0 if w[0] < 'H' else 1)

print(x.glom().collect())  # 원래 파티션
print(y.glom().collect())  # 새 파티션 구조 확인
