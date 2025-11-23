from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example7").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize(['John', 'Fred', 'Anna', 'James'])

# 첫 글자 기준으로 그룹핑 (키는 문자열 첫 글자)
y = x.groupBy(lambda w: w[0])

# 그룹핑된 값을 리스트로 변환하여 출력
print([(t[0], [i for i in t[1]]) for t in y.collect()])
