from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JoinExample").getOrCreate()
sc = spark.sparkContext

# 두 개의 (key, value) RDD 생성
x = sc.parallelize([("a", 1), ("b", 2)])
y = sc.parallelize([("a", 3), ("a", 4), ("b", 5)])

# join: 같은 키끼리 (value1, value2)로 조인
z = x.join(y)

print(z.collect())
# 결과: ('a', (1, 3)), ('a', (1, 4)), ('b', (2, 5))
