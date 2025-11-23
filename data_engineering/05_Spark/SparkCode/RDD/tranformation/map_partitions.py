from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example4").getOrCreate()
sc = spark.sparkContext

# 두 개의 파티션으로 나눈 숫자
x = sc.parallelize([1, 2, 3], 2)

# 각 파티션에서 합계를 계산하고 42를 추가로 출력
def f(iterator):
    yield sum(iterator)
    yield 42

y = x.mapPartitions(f)

print(x.glom().collect())  # 파티션별 데이터 확인
print(y.glom().collect())  # 결과도 파티션별로 확인
