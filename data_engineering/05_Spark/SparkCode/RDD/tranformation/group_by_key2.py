from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example9").getOrCreate()
sc = spark.sparkContext

# (문자, 숫자) 튜플 RDD
x = sc.parallelize([('B', 5), ('B', 4), ('A', 3), ('A', 2), ('A', 1)])

# 키를 기준으로 값들 그룹핑
y = x.groupByKey()

print(x.collect())  # 원본 확인
print([(t[0], [i for i in t[1]]) for t in y.collect()])  # 그룹별 값 확인
