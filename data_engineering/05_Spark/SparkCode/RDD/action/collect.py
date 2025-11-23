from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GlomCollectExample").getOrCreate()
sc = spark.sparkContext

# 2개의 파티션으로 RDD 생성
x = sc.parallelize([1, 2, 3], 2)

# 전체 파티션별 데이터 확인
print(x.glom().collect())  # 각 파티션에 있는 요소들을 리스트로 보여줌

# 전체 요소를 하나의 리스트로 수집
y = x.collect()
print(y)
