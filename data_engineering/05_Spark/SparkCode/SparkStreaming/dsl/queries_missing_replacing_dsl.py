from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# SparkSession 생성
spark = SparkSession.builder.appName("MissingValueHandling").getOrCreate()

# 예제 데이터 (NULL 포함)
data = [
    ("A", 100),
    ("B", None),
    (None, 300),
    ("A", None),
    (None, None)
]
schema = StructType([
    StructField("column1", StringType(), True),
    StructField("column2", IntegerType(), True)
])
df = spark.createDataFrame(data, schema)

# -----------------------------------------------
# [1] NULL 값 채우기: column1 → "Unknown", column2 → 0
# -----------------------------------------------
print("=== NULL 값 채우기 ===")
df.na.fill({"column1": "Unknown", "column2": 0}).show()

# -----------------------------------------------
# [2] NULL 값이 하나라도 있는 행 제거
# -----------------------------------------------
print("=== NULL 포함 행 제거 ===")
df.na.drop().show()

# -----------------------------------------------
# [3] 문자열 값 치환: "A" → "Alpha", "B" → "Beta"
# -----------------------------------------------
print("=== 문자열 값 치환 ===")
df.na.replace({"A": "Alpha", "B": "Beta"}).show()
