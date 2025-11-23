from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("ViewExample").getOrCreate()

# 예제 데이터프레임 생성
data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)

# 1. 임시 뷰 등록 (세션 내에서만 사용 가능)
df.createTempView("temp_view")
print("=== Temp View ===")
spark.sql("SELECT * FROM temp_view").show()

# 2. 전역 임시 뷰 등록 (다른 세션에서도 global_temp로 접근 가능)
df.createGlobalTempView("global_view")
print("=== Global Temp View ===")
spark.sql("SELECT * FROM global_temp.global_view").show()

# 3. 기존 temp view가 있을 경우 덮어쓰기
df.createOrReplaceTempView("temp_view")
print("=== Replaced Temp View ===")
spark.sql("SELECT * FROM temp_view").show()
