from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example8").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize(['John', 'Fred', 'Anna', 'James'])

# (문자 첫글자, 전체 문자열)로 매핑
x = x.map(lambda w: (w[0], w))

# 같은 키를 가지는 값끼리 그룹핑
y = x.groupByKey()

print([(t[0], [i for i in t[1]]) for t in y.collect()])
