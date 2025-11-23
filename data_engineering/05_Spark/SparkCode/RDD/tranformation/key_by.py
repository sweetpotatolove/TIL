from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example6").getOrCreate()
sc = spark.sparkContext

x = sc.parallelize(['John', 'Fred', 'Anna', 'James'])

# 각 문자열의 첫 글자를 키로 사용
y = x.keyBy(lambda w: w[0])

print(y.collect())  # 결과: (J, 'John'), (F, 'Fred') ...
