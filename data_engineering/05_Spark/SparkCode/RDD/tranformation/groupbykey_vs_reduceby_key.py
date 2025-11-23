from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GroupByKeyVsReduceByKey").getOrCreate()
sc = spark.sparkContext

# 문자열 RDD 생성
words = sc.parallelize(['one', 'two', 'two', 'three', 'three', 'three'])

# (단어, 1) 쌍으로 변환
wordPairsRdd = words.map(lambda w: (w, 1))

# groupByKey: 같은 키의 값을 그룹으로 묶고 sum으로 집계
wordCounts = wordPairsRdd.groupByKey().map(lambda pair: (pair[0], sum(pair[1])))

print(words.collect())
print(wordPairsRdd.collect())
print(wordCounts.collect())

print("-" * 50)

# reduceByKey: 키별로 값을 직접 합침
wordCounts = wordPairsRdd.reduceByKey(lambda cnt1, cnt2: cnt1 + cnt2)

print(words.collect())
print(wordPairsRdd.collect())
print(wordCounts.collect())
