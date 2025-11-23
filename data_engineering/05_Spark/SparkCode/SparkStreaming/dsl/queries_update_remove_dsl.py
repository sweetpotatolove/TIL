from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("UpdateRemoveColumns").getOrCreate()

# 예제 데이터 생성
data = [("ABCDEFG", 100), ("HIJKLMN", 200)]
columns = ["column1", "column2"]
df = spark.createDataFrame(data, columns)

# -------------------------------------------
# [1] 컬럼 이름 변경: column1 → alphabet, column2 → number
# -------------------------------------------
print("=== 컬럼 이름 변경 ===")
renamed_df = df.withColumnRenamed("column1", "alphabet") \
               .withColumnRenamed("column2", "number")

renamed_df.show()

# -------------------------------------------
# [2] 컬럼 삭제: column1 제거
# -------------------------------------------
print("=== column1 컬럼 삭제 ===")
df.drop("column1").show()
