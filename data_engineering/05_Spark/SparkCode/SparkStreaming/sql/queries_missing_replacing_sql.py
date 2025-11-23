from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# SparkSession 생성
spark = SparkSession.builder.appName("SQLMissingReplace").getOrCreate()

# 예제 데이터 생성
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

# TempView 등록
df.createOrReplaceTempView("my_table")

# --------------------------------------------------
# [1] COALESCE: NULL 처리 (column1: 'Unknown', column2: 0)
# --------------------------------------------------
print("=== COALESCE를 이용한 NULL 대체 ===")
spark.sql("""
    SELECT 
        COALESCE(column1, 'Unknown') AS column1,
        COALESCE(column2, 0) AS column2
    FROM my_table
""").show()

# --------------------------------------------------
# [2] NULL 포함 행 제거
# --------------------------------------------------
print("=== NULL이 포함된 행 제거 ===")
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column1 IS NOT NULL AND column2 IS NOT NULL
""").show()

# --------------------------------------------------
# [3] CASE WHEN으로 문자열 값 치환
# --------------------------------------------------
print("=== 문자열 값 치환: A → Alpha, B → Beta ===")
spark.sql("""
    SELECT 
        CASE 
            WHEN column1 = 'A' THEN 'Alpha'
            WHEN column1 = 'B' THEN 'Beta'
            ELSE column1
        END AS column1,
        column2
    FROM my_table
""").show()
