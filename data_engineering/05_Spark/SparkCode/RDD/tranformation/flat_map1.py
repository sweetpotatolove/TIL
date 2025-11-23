from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example2").getOrCreate()
sc = spark.sparkContext

# 숫자 리스트 RDD
x = sc.parallelize([1, 2, 3])

# 각 숫자에 대해 곱셈 결과 + 100 포함하여 여러 값 반환
y = x.flatMap(lambda x: (1 * x, 2 * x, 3 * x, 100))

print(x.collect())   # 원본 출력
print(y.collect())   # flatMap 결과 출력
print(y.mean())      # 평균값 계산 (action)
