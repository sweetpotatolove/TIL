from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LectureSpark").getOrCreate()
sc = spark.sparkContext

# 파일 로드
rdd = sc.textFile("test.txt")

# 원본 RDD 파티션 개수 출력
print("현재 파티션 개수:", rdd.getNumPartitions())

# 각 파티션에서 어떤 줄이 할당되었는지 확인
print("=== 원본 RDD 파티션별 데이터 ===")
rdd.mapPartitionsWithIndex(
    lambda idx, itr: [f"Partition {idx}: {list(itr)}"]
).foreach(print)

# repartition으로 파티션 수 변경
rdd_repartitioned = rdd.repartition(1)
print("변경된 파티션 수:", rdd_repartitioned.getNumPartitions())

# Repartition된 RDD 파티션별 내용 출력
print("=== repartition 후 RDD 파티션별 데이터 ===")
rdd_repartitioned.mapPartitionsWithIndex(
    lambda idx, itr: [f"Partition {idx}: {list(itr)}"]
).foreach(print)

# 전체 줄 개수 확인
line_count = rdd.count()
print("줄 개수:", line_count)

# "Spark" 포함된 줄 필터링
filtered_rdd = rdd.filter(lambda line: "Spark" in line)
print("=== 'Spark' 포함된 줄 ===")
filtered_rdd.foreach(print)

# 전체를 소문자로 변환
lower_rdd = rdd.map(lambda line: line.lower())
print("=== 소문자로 변환된 줄 ===")
lower_rdd.foreach(print)
