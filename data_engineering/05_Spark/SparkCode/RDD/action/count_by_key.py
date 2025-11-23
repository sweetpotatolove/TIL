from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CountByKeyExample").getOrCreate()
sc = spark.sparkContext

# Key-Value 쌍으로 구성된 RDD
x = sc.parallelize([('J', 'James'), ('F', 'Fred'), ('A', 'Anna'), ('J', 'John')])

# 각 key에 대해 몇 번 등장했는지 세기
y = x.countByKey()

print(y)  # 결과: {'J': 2, 'F': 1, 'A': 1}
