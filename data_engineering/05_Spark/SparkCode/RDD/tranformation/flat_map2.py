from pyspark.sql import SparkSession

# Spark 세션 생성
spark = SparkSession.builder.appName("FlatMapExample2").getOrCreate()
sc = spark.sparkContext

# RDD x 생성 - 각 요소는 튜플(또는 리스트) 3개짜리
x = sc.parallelize([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

# flatMap 적용: 각 튜플을 낱개 원소로 펼침
y = x.flatMap(lambda tup: tup)

# 결과 출력
print("원본 RDD x:", x.collect())  # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print("flatMap 적용 후 RDD y:", y.collect())  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
