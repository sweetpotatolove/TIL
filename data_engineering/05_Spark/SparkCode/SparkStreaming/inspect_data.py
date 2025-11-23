from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder.appName("DataFrameOperations").getOrCreate()

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Alice", 25),  # 중복 행
    ("David", 35)
]
columns = ["name", "age"]

# DataFrame 생성
df = spark.createDataFrame(data, columns)

# === 1. 열 이름과 데이터 유형 반환 ===
print("dtypes:", df.dtypes)

# === 2. 전체 데이터 표시 ===
print("show():")
df.show()

# === 3. 처음 n개의 행 반환 ===
print("head():", df.head())         # 기본값 n=1
print("take(2):", df.take(2))       # n=2

# === 4. 첫 번째 행 반환 ===
print("first():", df.first())

# === 5. DataFrame의 스키마 반환 ===
print("schema:", df.schema)

# === 6. 요약 통계 정보 ===
print("describe():")
df.describe().show()

# === 7. 열 이름 반환 ===
print("columns:", df.columns)

# === 8. 행 개수 계산 ===
print("count():", df.count())

# === 9. 고유 행 개수 계산 ===
print("distinct().count():", df.distinct().count())

# === 10. 스키마 출력 ===
print("printSchema():")
df.printSchema()

# === 11. 실행 계획 출력 ===
print("explain():")
df.explain()

print("explain(extended=True):")
df.explain(extended=True)

# === 12. 중복 제거 ===
df_nodup = df.dropDuplicates()
print("dropDuplicates():")
df_nodup.show()
