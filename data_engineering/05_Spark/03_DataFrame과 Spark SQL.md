# Spark DataFrame과 Spark SQL

## 챕터의 포인트
- DataFrame과 Spark SQL
- DSL과 SQL을 활용한 데이터 처리
- Sqprk Streaming

# DataFrame과 Spark SQL

# RDD와 Spark SQL · DataFrame

## RDD란?
- Resilient Distributed Dataset
  - 데이터를 병렬 처리하는 핵심적인 역할을 수행하여 빠르고 안정적으로 동작하는 프로그램을 작성 가능
- but  
  - 데이터 값 자체는 표현이 가능하지만,  
  - 데이터에 대한 메타 데이터, ‘스키마’에 대해 명시적 표현 방법이 없음

# SparkSQL, DataFrame, Dataset

## RDD API의 문제점
- 스파크가 RDD API 기반의 연산, 표현식을 검사하지 못해 최적화할 방법이 없음
  - RDD API 기반 코드에서 어떤 일이 일어나는지 스파크는 알 수 없음
  - Join, filter, group by 등 여러 연산을 하더라도 스파크에서는 람다 표현식으로만 보임
  - 특히 PySpark의 경우, 연산 함수 Iterator 데이터 타입을 제대로 인식하지 못함  
    - 스파크에서는 단지 파이썬 기본 객체로만 인식

- 스파크는 어떠한 데이터 압축 테크닉도 적용하지 못함
  - 객체 안에서 어떤 타입의 컬럼에 접근하더라도 스파크는 알 수 없음
  - 결국 바이트 뭉치로 직렬화해 사용할 수밖에 없음

- → 스파크가 연산 순서를 재정렬하여 효율적인 질의 계획으로 바꿀 수 없음

# Spark SQL과 DataFrame 소개

## DataFrame
- 스키마(schema)를 가진 분산 데이터 컬렉션
- 데이터를 행(row)과 열(column)로 구성된 표 형태로 관리
- 각 열은 명확한 데이터 타입과 메타 데이터(schema)를 가지고 있음
- Spark SQL이 제공하는 구조화된 데이터 모델로서 RDD의 한계를 보완

# DataFrame API

## DataFrame API - 개요
- 구조, 포맷 등 몇몇 특정 연산 등에 있어 Pandas의 DataFrame에 영향을 많이 받음
- 이름 있는 컬럼과 스키마를 가진 분산 인메모리 테이블처럼 동작
- Spark DataFrame은 하나의 표 형태로 보임

## DataFrame API - 데이터 타입
- 기본 타입
  - Byte, Short, Integer, Long, Float, Double, String, Boolean, Decimal

- 정형화 타입
  - Binary, Timestamp, Date, Array, Map, Struct, StructField

- 실제 데이터를 위한 스키마를 정의할 때 이런 타입이 어떻게 연계되는지 이해하는 것이 중요함

- 예시 코드(원문 그대로):
  ```
  from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType
  
  schema = StructType([
      StructField("name", StringType(), True),
      StructField("scores", ArrayType(IntegerType()), True)
  ])
  ```

## DataFrame API - 스키마(Schema)
- 스파크에서의 스키마는 Dataframe을 위해 컬럼 이름과 연관된 데이터 타입을 정의한 것
- 외부 데이터 소스에서 구조화된 데이터를 읽어 들일 때 사용

- 읽을 때 스키마를 가져오는 방식과 달리, 미리 스키마를 정의하는 것은 여러 장점 존재
  - 스파크가 데이터 타입을 추측해야 되는 책임을 덜어줌
  - 스파크가 스키마를 확정하기 위해 파일의 많은 부분을 읽어 들이려 별도의 Job을 만드는 것을 방지
  - 데이터가 스키마와 맞지 않는 경우, 조기에 문제 발견 가능

# Spark SQL과 DataFrame 구조

## DataFrame의 구성
- DataFrame = RDD + schema + DSL
- Named columns with types
- Domain-Specific Language(DSL)

## DataFrame 쿼리 방식
- DataFrame은 DSL 방식과 SQL 방식 모두 지원

### DSL 수행 예시 (코드블록)
```python
# 필터링
sciDocs = data.filter(col("label") == 1)

# 결과 출력
sciDocs.show()
```

### SQL 수행 예시 (코드블록)
```python
# SQL 필터링
data_scaled = spark.sql("SELECT * FROM data WHERE label = 1")

# 결과 출력
data_scaled.show()
```

## RDD와 DataFrame의 차이점은 무엇인가?

| 구분 | RDD | DataFrame |
|------|------|------------|
| 데이터 표현 방식 | 값만 표현 가능, 스키마 표현 불가능 | 명확한 스키마(컬럼, 데이터 타입)를 가진 구조적 데이터 |
| 최적화 및 성능 | 최적화 어려움, 직접적 연산 필요 | Catalyst Optimizer 통한 자동 최적화 및 빠른 처리 |
| 사용 편의성 | 낮음(저수준 API) | 높음(고수준 API, SQL 활용 가능) |

- 결론  
  - DataFrame을 사용하면 데이터를 더 효율적이고 편리하게 처리 가능  
  - 메타 정보를 활용하여 더 빠르고 최적화된 분석 수행 가능

## RDD를 사용하는 경우
1. 저수준의 Transformation과 Action을 직접 제어해야 할 때  
2. 스트림 데이터(미디어나 텍스트 스트림)가 구조화되지 않은 경우  
3. 특정 도메인 표현을 위해 함수형 프로그래밍이 필요할 때  
4. 스키마 변환이 필요 없을 때  
   - 예: 열 기반 저장소를 사용하지 않는 경우  
5. DataFrame이나 Dataset에서 처리할 수 없는 성능 최적화가 필요할 때

## DataFrame를 사용하는 경우
1. 고수준의 추상화와 도메인 기반 API가 필요할 때  
2. 고수준의 표현(filter, map, agg, avg, sum SQL, columnar access) 등 복잡한 연산이 필요하거나  
   반구조적 데이터에 대한 lambda 식이 필요할 때  
3. 타입 안정성과 최적화를 위해 컴파일 시 타입 안전성을 보장하고,  
4. Catalyst 최적화 및 Tungsten의 효율적인 코드 제너레이션이 필요할 때  
5. Spark API의 일관성과 간결함을 원할 때  

## SparkSQL이란?
- Spark SQL은 구조화된 데이터를 SQL처럼 처리할 수 있도록 해주는 스파크 모듈  
- 내부적으로는 DataFrame/Dataset API와 동일한 엔진(Catalyst)을 사용하여 처리  
- DataFrame과 Dataset을 SQL처럼 다룰 수 있게 해주는 분산 SQL 쿼리 엔진  
- Spark SQL은 RDD보다 더 높은 수준의 추상화와 자동 최적화를 제공  

→ DataFrame이 중심이고, Spark SQL은 그것을 SQL 방식으로 접근하게 해주는 방법 중 하나

## SparkSQL의 역할
- SQL 같은 질의 수행  
- 스파크 컴포넌트들을 통합하고, Dataframe, Dataset가 java, scala, python, R 등 여러 프로그래밍 언어로  
  정형화 데이터 관련 작업을 단순화할 수 있도록 추상화  
- 정형화된 파일 포맷(JSON, CSV, txt, avro, parquet, orc 등)에서 스키마와 정형화 데이터를 읽고 쓰며,  
  데이터를 임시 테이블로 변환  
- 빠른 데이터 탐색을 할 수 있도록 대화형 스파크 SQL 셀을 제공  
- 표준 데이터베이스 JDBC/ODBC 커넥터를 통해, 외부의 도구들과 연결할 수 있는 중간 역할 제공  
- 최종 실행을 위해 최적화된 질의 계획과 JVM을 위한 최적화된 코드를 생성 

## Spark SQL

| UserID   | Name            | Age | Location   | Pet       |
|----------|-----------------|-----|------------|-----------|
| 28492942 | John Galt       | 32  | New York   | Sea Horse |
| 95829324 | Winston Smith   | 41  | Oceania    | Ant       |
| 92871761 | Tom Sawyer      | 17  | Mississippi| Raccoon   |
| 37584932 | Carlos Hinojosa | 33  | Orlando    | Cat       |
| 73648274 | Luis Rodriguez  | 34  | Orlando    | Dogs      |

## SparkSQL의 역할
- JDBC  
- Console  
- User Programs (Java, Scala, Python)  
  ↓  
- Spark SQL / DataFrame API  
  ↓  
- Catalyst Optimizer  
  ↓  
- Spark  
  ↓  
- Resilient Distributed Datasets  

## Spark SQL의 내부 동작
- SQL 쿼리를 실행하는 역할  
  +  
  사용자가 입력한 쿼리나 DataFrame의 명령을 가장 빠르고 효율적인 방식으로 처리
- Spark SQL이 내부에서 데이터를 효율적으로 처리하는 핵심적인 엔진이 Catalyst Optimizer

## Spark SQL의 내부는 어떻게 작동할까?
### Catalyst Optimizer의 최적화 과정
1. SQL Parser & DataFrame API 해석 단계  
2. Logical Plan (논리적 계획) 생성  
3. Optimized Logical Plan (최적화된 논리 계획) 생성  
4. Physical Plan (물리적 실행 계획) 생성  

-> Catalyst Optimizer가 내부적으로 복잡한 최적화 과정을 자동으로 처리

## Spark SQL과 DataFrame API의 관계
- Spark SQL과 DataFrame API는 서로 완전히 독립된 별개의 것이 아님  
- 동일한 최적화 엔진(Catalyst Optimizer)을 공유하고, 내부적으로 통합된 구조를 가짐  

=> Spark에서는 DataFrame API를 이용해 작성된 데이터 처리 명령을 내부적으로 Spark SQL의 엔진으로 최적화해 실행

# Dataset API

## Dataset API
- 스파크 2.0에서, 개발자들이 한 종류의 API만 알면 되도록, Dataframe, Dataset API를 하나로 합침.  
- Dataset은 정적 타입(typed) API와 동적 타입(untyped) API의 두 특성을 모두 가짐.  
- Java, Scala(타입 안전을 보장하는 언어)에서만 사용이 가능하고,  
  Python, R(타입 안전을 보장하지 않는 언어)에서는 사용이 불가능, DataFrame API만 사용 가능.

# SparkSQL, Dataframe, Dataset 이란?

## DataFrame vs Dataset
- 가장 큰 차이점은 오류가 발견되는 시점

| 구분 | SQL | DataFrames | Datasets |
|------|------|-------------|-----------|
| Syntax Errors | Runtime | Compile Time | Compile Time |
| Analysis Errors | Runtime | Runtime | Compile Time |

# DataFrame과 Spark SQL

## View 등록 및 SQL 실행

```python
# DataFrame을 뷰로 등록하기
df.createTempView("viewName")
df.createGlobalTempView("viewName")
df.createOrReplaceTempView("viewName")

# 뷰에 SQL 쿼리 실행하기
spark.sql("SELECT * FROM viewName ").show()
spark.sql("SELECT * FROM global_temp.viewName").show()
```

## DataFrame 구조 변환

```python
# DataFrame → RDD (분산 처리용 RDD로 변환)
rdd1 = df.rdd

# DataFrame → JSON 문자열 → 첫 번째 항목 확인
df.toJSON().first()

# DataFrame → Pandas DataFrame
pandas_df = df.toPandas()
print(pandas_df)
```

# DSL과 SQL을 활용한 데이터 처리

## SQL쿼리 기본 문법
- 데이터 조회 : SELECT, WHERE  
- 정렬 : ORDER BY  
- 중복 제거 : DISTINCT  
- 데이터 집계 : GROUP BY, HAVING, 집계 함수(COUNT, AVG, SUM)  
- 데이터 결합 : JOIN  

## Creating DataFrames(DSL 코드)

```python
# SparkSession 생성
spark = SparkSession.builder.appName("ExampleApp").getOrCreate()

# 스키마 정의
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

# 데이터 전처리 및 DataFrame 생성
parts = spark.sparkContext.parallelize([("Mine", "28"), ("Filip", "29"), ("Jonathan", "30")])
people = parts.map(lambda p: Row(name=p[0], age=int(p[1].strip())))
df = spark.createDataFrame(people, schema)

# 결과 출력
df.show()
```

## Creating DataFrames(SQL 코드)

```python
# DataFrame을 SQL에서 사용할 수 있도록 TempView 등록
df.createOrReplaceTempView("people")

# Spark SQL을 이용한 동일 조회
result = spark.sql("""
    SELECT name, age
    FROM people
""")

result.show()
```

## Creating DataFrames From File(DSL 코드)

```python
# DataFrame을 직접 생성
people_df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt") \
    .toDF("name", "age")

# 결과 출력
peopledf.show()
```

## Creating DataFrames From File(SQL 코드)

```python
# DataFrame을 직접 생성
people_df = spark.read.option("header", "false") \
    .option("inferSchema", "true") \
    .csv("people.txt") \
    .toDF("name", "age")

# TempView 등록
people_df.createOrReplaceTempView("people")

# SQL 쿼리로 조회
result = spark.sql("""SELECT name, age FROM people""")

# 출력 확인
result.show()
```

## From Spark Data Sources

```python
# JSON
df = spark.read.json(filename.json)
df = spark.read.load("filename.json", format="json")

# Parquet files
df = spark.read.load("filename.parquet")

# TXT files
df = spark.read.txt("filename.txt")
```

## From Spark Data Sources

```python
# 열 이름과 데이터 유형 반환
df.dtypes

# 내용 표시
df.show()

# 처음 n개의 행 반환
df.head()

# 첫 번째 행 반환
df.first()
```

## Inspect Data

```python
# 처음 n개의 행 반환
df.take(n)

# DataFrame의 스키마 반환
df.schema

# 요약 통계 계산
df.describe().show()

# 열 이름 반환
df.columns
```

## Inspect Data

```python
# 행 개수 계산
df.count()

# 고유 행 개수 계산
df.distinct().count()

# 스키마 출력
df.printSchema()

# (논리 및 물리적) 실행 계획 출력
df.explain()
```

## Duplicate Values

```python
# 중복 행 제거
df = df.dropDuplicates()
```

# Queries (SELECT)

## DataFrame 생성
```python
df = spark.createDataFrame(data)
```

## DSL 방식: column1, column2 선택
```python
df.select("column1", "column2").show()
```

## SQL 사용을 위해 TempView 등록
```python
df.createOrReplaceTempView("my_table")
```

## SQL 방식: 동일한 SELECT 쿼리
```python
spark.sql("""
    SELECT column1, column2
    FROM my_table
""").show()
```

## 결과 출력 예시 (표)
| column1 | column2 |
|---------|---------|
| A       | 100     |
| B       | 200     |

# Queries (SELECT with Expressions & Filters) DSL 코드

## column1과 column2 값에 +1 결과 출력
```python
df.select(
    col("column1"),
    (col("column2") + 1).alias("column2_plus1")
).show()
```

## column1이 "A"보다 큰 값만 필터링
```python
df.filter(col("column1") > "A").show()
```

## 결과 출력 (표)
| column1 | column2_plus1 |
|---------|----------------|
| A       | 101            |
| B       | 201            |

| column1 | column2 |
|---------|----------|
| B       | 200      |

# Queries (SELECT with Expressions & Filters) SQL 코드

## SELECT with expression
```python
spark.sql("""
    SELECT column1, column2 + 1 AS column2_plus1
    FROM my_table
""").show()
```

## WHERE 조건 필터
```python
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column1 > 'A'
""").show()
```

## 결과 출력 (표)
| column1 | column2_plus1 |
|---------|----------------|
| A       | 101            |
| B       | 201            |

| column1 | column2 |
|---------|---------|
| B       | 200     |

## Queries (When, ISIN) DSL 코드

from pyspark.sql.functions import when

```
# column2가 100보다 크면 1, 아니면 0으로 표시해 새로운 컬럼 'flag' 추가
df.select(
        "column1",
        when(df.column2 > 100, 1)
        .otherwise(0)
        .alias("flag")
).show()

# column1 값이 'A' 또는 'B'인 행만 필터링
df.filter(
        df.column1.isin("A", "B")
).show()
```

# Spark SQL

## Queries (CASE WHEN, IN) SQL 코드

```
# column2가 100보다 크면 1, 아니면 0으로 표시해 새로운 컬럼 'flag' 추가
spark.sql("""
        SELECT column1,
               CASE WHEN column2 > 100 THEN 1 ELSE 0 END AS flag
        FROM my_table
""").show()

# column1 값이 'A' 또는 'B'인 행만 필터링
spark.sql("""
        SELECT *
        FROM my_table
        WHERE column1 IN ('A', 'B')
""").show()
```

# Spark SQL

## 문자열 조건 처리(Like, STARTSWITH, ENDSWITH) DSL 코드

```
# col1 값이 ‘A’로 시작하면 True, 아니면 False - 특정 문자열로 시작하는지
df.select(
        col("column1"), col("column1").startswith("A").alias("starts_with_A")
).show()

# col2이 “00”으로 끝나는 경우 - 특정 문자열로 끝나는지
df.select(
        col("column2"),
        col("column2").cast("string").endswith("00").alias("ends_with_00")
).show()

# col1이 ‘A’와 정확히 일치하는 경우
df.select(
        col("column1"), col("column1").like("A").alias("is_A")
).show()
```

# 문자열 조건 처리 (Like, STARTSWITH, ENDSWITH) — SQL 코드

## STARTSWITH

```
# col1 값이 ‘A’로 시작하면 True, 아니면 False - 특정 문자열로 시작하는지
spark.sql("""SELECT column1, column1 LIKE 'A%' AS starts_with_A
    FROM my_table """).show()
```

## ENDSWITH

```
# col2이 “00”으로 끝나는 경우 - 특정 문자열로 끝나는지
spark.sql("""SELECT column2,
        CAST(column2 AS STRING) LIKE '%00' AS ends_with_00
    FROM my_table""").show()
```

## 정확히 일치 여부

```
# col1이 ‘A’와 정확히 일치하는 경우
spark.sql("""SELECT column1, column1 = 'A' AS is_A
    FROM my_table""").show()
```

> 모든 조건은 문자열 비교로 True/False 결과를 반환합니다.  
> 숫자 컬럼에는 문자열 변환이 필요할 수 있습니다.

# 문자열 추출 및 범위 조건 처리 (Substring, Between) — DSL 코드

## Substring (DSL)

```
# column1에서 2번째 문자부터 3개의 문자를 추출하여 컬럼이름을 “name”으로 지정
df.select(df.column1.substr(2, 3).alias("name")).show()
```

## Between (DSL)

```
# column2의 값이 50~150 사이에 있으면 TRUE를 표시
df.select(
    col("column1"), col("column2"),
    col("column2").between(50, 150).alias("is_between_50_150")
).show()
```

# 문자열 추출 및 범위 조건 처리 (Substring, Between) — SQL 코드

## Substring

```
# column1에서 2번째 문자부터 3개의 문자를 추출하여 컬럼이름을 “name”으로 지정
spark.sql("""SELECT SUBSTRING(column1, 2, 3) AS name FROM my_table""").show()
```

## Between

```
# column2의 값이 50~150 사이에 있으면 TRUE를 표시
spark.sql("""
    SELECT column1, column2,
           column2 BETWEEN 50 AND 150 AS is_between_50_150
    FROM my_table
""").show()
```

# 컬럼 이름 변경 및 삭제 (Update & Remove Columns) — DSL 코드

## 컬럼명 변경
```
# column1 -> alphabet, column2 -> number로 컬럼명 변경
df.withColumnRenamed("column1", "alphabet") \
  .withColumnRenamed("column2", "number") \
  .show()
```

## 컬럼 삭제
```
# column1 컬럼 삭제
df.drop("column1").show()
```

# 컬럼 이름 변경 및 삭제 (Update & Remove Columns) — SQL 코드

## 컬럼명 변경
```
# column1 -> alphabet, column2 -> number로 컬럼명 변경
spark.sql("""
    SELECT column1 AS alphabet, column2 AS number
    FROM my_table
""").show()
```

## 컬럼 삭제
```
# column1 컬럼 삭제
spark.sql("SELECT column2 FROM my_table").show()
```

# 그룹별 집계 (Group By, Count) — DSL 코드

## 그룹별 Count 계산
```
# column1을 기준으로 그룹화하고 각 그룹의 개수를 계산하여 출력
df.groupBy("column1").count().show()
```

# 그룹별 집계(Group By, Count) — SQL 코드

## 그룹별 Count 계산 (SQL)
```
# column1을 기준으로 그룹화하고 각 그룹의 개수를 계산하여 출력
spark.sql("""
    SELECT column1, COUNT(*) as count
    FROM my_table
    GROUP BY column1
""").show()
```

# 조건 필터링(Filter) — DSL 코드

## column2 > 200 조건 필터링 (DSL)
```
# column2의 값이 200보다 큰 항목만 필터링하여 기록을 유지
df.filter(df["column2"] > 200).show()
```

# 조건 필터링(Filter) — SQL 코드

## column2 > 200 조건 필터링 (SQL)
```
# column2의 값이 200 보다 큰 항목만 필터링하여 기록을 유지
spark.sql("""
    SELECT *
    FROM my_table
    WHERE column2 > 200
""").show()
```

# 정렬(Sort, OrderBY) — DSL 코드

## 단일 컬럼 내림차순
```
df.sort(df["column1"].desc()).show()
```

## 다중 컬럼 정렬: column1 오름차순, column2 내림차순
```
df.orderBy(["column1", "column2"], ascending=[True, False]).show()
```

# 정렬(Sort, OrderBY) — SQL 코드

## 단일 컬럼 내림차순
```
spark.sql("""
SELECT *
FROM my_table
ORDER BY column1 DESC
""").show()
```

## 다중 컬럼 정렬: column1 오름차순, column2 내림차순
```
spark.sql("""
SELECT *
FROM my_table
ORDER BY column1 ASC, column2 DESC
""").show()
```

# 결측값 처리 및 값 치환(Missing & Replacing Values) — DSL 코드

## column1 NULL → "Unknown", column2 NULL → 0
```
# column1의 NULL → "Unknown", column2의 NULL → 0
df.na.fill({"column1": "Unknown", "column2": 0}).show()
```

## 두 컬럼 중 하나라도 NULL이 있으면 삭제
```
df.na.drop().show()
```

## 문자열 값 치환: "A" → "Alpha", "B" → "Beta"
```
df.na.replace({"A": "Alpha", "B": "Beta"}).show()
```

# 결측값 처리 및 값 치환(Missing & Replacing Values) — SQL 코드

## column1 NULL → "Unknown", column2 NULL → 0
```
spark.sql("""
SELECT
    COALESCE(column1, 'Unknown') AS column1,
    COALESCE(column2, 0) AS column2
FROM my_table
""").show()
```

## 두 컬럼 중 하나라도 NULL이면 삭제
```
spark.sql("""
SELECT * FROM my_table
WHERE column1 IS NOT NULL AND column2 IS NOT NULL
""").show()
```

## 문자열 값 치환: "A" → "Alpha", "B" → "Beta"
```
spark.sql("""
SELECT CASE
    WHEN column1 = 'A' THEN 'Alpha'
    WHEN column1 = 'B' THEN 'Beta'
    ELSE column1
END AS column1, column2
FROM my_table
""").show()
```

# Spark Streaming

# Kafka 데이터를 Spark로 처리

## Spark Streaming
- Batch Processing은 큰 데이터 셋에 대해 한 번의 연산을 수행하는 형태  
- Streaming Processing은 끊임없이 들어오는 데이터의 흐름을 연속적으로 처리  
- Batch Processing과 함께 사용하여 서로의 약점을 보완하는 형태로 많이 사용 (Ex. Lambda Architecture)

|               | Batch       | Streaming            |
|---------------|-------------|-----------------------|
| **Structured APIs** | SQL, Dataset, DataFrame | Structured Streaming |
| **Low Level APIs**  | RDD         | DStream              |

# Kafka 데이터를 Spark로 처리

## Spark Streaming
- Spark Steaming 은 DStream API (Low Level APIs) 를 기반으로 하며, Spark Structured Streaming 은 Structured API (High Level APIs) 를 기반으로 한다.  
- Spark RDD를 기반으로 처리한다. Input 도 RDD이고 처리하는 데이터도 RDD가 된다.  
- Micro Batch 모드로 동작한다.  
- 일정시간동안 새롭게 들어온 데이터를 모아서 한번에 처리하게 된다.  

# Kafka 데이터를 Spark로 처리

## Spark Structured Streaming
- RDD를 직접 다루지 않고 DataFrame, Dataset API를 사용하는 만큼 더 많은 종류의 스트리밍 최적화 기술을 사용할 수 있다.
- 데이터의 Stream을 무한하게 연속적으로 추가되는 데이터의 테이블 개념으로 간주  
- 기본은 마이크로 배치로 처리하지만, Continuous 모드도 지원(기능 제약이 있어 대부분 마이크로 배치 모드 사용)

# Kafka 데이터를 Spark로 처리

## Spark Structured Streaming
- 새로운 단어 데이터가 입력될 때마다 Input Table에 새로운 단어 배열이 append(추가)
- 실시간으로 들어오는 새로운 데이터가 기존 상태(state)에 누적되어 결과 테이블이 갱신되는 구조

# Kafka 데이터를 Spark로 처리

## 실습 목표
- Kafka 메시지를 Spark로 읽어와 타임스탬프별 메시지 개수 집계
- PySpark 설치 재확인

```
ssafy@LAPTOP-MM9415QV:~$ pyspark
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
25/03/29 00:06:41 WARN Utils: Your hostname, LAPTOP-MM9415QV resolves to a loopback address: 127.0.1.1...
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.4
      /_/
Using Python version 3.12.3...
Spark context available as 'sc'.
SparkSession available as 'spark'.
>>>
```

# Kafka 데이터를 Spark로 처리

## 실습

### 실습 전 체크 리스트
- Kafka 실행 중인지 확인 (test-topic 존재)
  ```
  kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
  ```

- Spark 3.5.4 설치

- PySpark 환경 설정 완료
  ```
  pip install pyspark==3.5.4
  pip install findspark==2.0.1
  ```

- 필요한 패키지 자동 다운로드됨 (실습 코드에서 `spark.jars.packages` 옵션 사용)

# Kafka 데이터를 Spark로 처리

## 실습
- spark_producer.py
- Kafka 프로듀서로 다양한 시간대의 타임스탬프를 포함한 메시지들을 생성해서 보내기

```python
# 메시지 전송
for i in range(30):
    # 0~4분 사이의 임의 시점 생성 (1분 단위 집계를 위해)
    offset_minutes = random.randint(0, 4)
    offset_seconds = random.randint(0, 59)

    msg_time = base_time + timedelta(minutes=offset_minutes, seconds=offset_seconds)

    message = {
        'id': i,
        'message': f'테스트 메시지 {i}',
        'timestamp': msg_time.strftime('%Y-%m-%d %H:%M:%S')
    }

    # Kafka로 메시지 전송
    producer.send('test-topic', message)
    print(f'전송된 메시지: {message}')

    time.sleep(0.5)  # 너무 빠르게 보내지 않도록 살짝 텀 주기
```

# Kafka 데이터를 Spark로 처리

## 실습
- spark_kafka_example.py
  - Spark 로 타임스탬프 별 집계 처리

```python
def process_kafka_stream():
    # 메세지 값을 문자열로 변환
    value_df = df.selectExpr("CAST(value AS STRING)")

    # 스키마 정의 (예: JSON 데이터 가정)
    schema = StructType([
        StructField("timestamp", TimestampType(), True),
        StructField("message", StringType(), True),
    ])

    # JSON 파싱
    parsed_df = value_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

    # 간단한 처리: 타임스탬프별 메세지 수 집계
    result_df = parsed_df \
        .withWatermark("timestamp", "1 minute") \
        .groupBy(window("timestamp", "1 minute")) \
        .count()
```

# Kafka 데이터를 Spark로 처리

## 실습
- 실습 순서
  - spark_producer.py 실행
  - spark_kafka_example.py 실행
    - 프린트 되는 집계 결과 확인

- test-topic 에 타임스탬프 잘 생성되어 들어오는지 확인
  /home/ssafy/kafka$ bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092 --from-beginning

# Kafka 데이터를 Spark로 처리

## 실습
- 결과 예시
  - spark_kafka_example.py 실행

Batch: 2
+--------------------+-----+
|              window|count|
+--------------------+-----+
|{2025-04-13 10:42...|    1|
|{2025-04-13 10:39...|    1|
|{2025-04-13 10:41...|    1|
|{2025-04-13 10:40...|    2|
|{2025-04-13 10:38...|    2|
|{2025-04-13 10:43...|    1|
+--------------------+-----+

Batch: 3
--------------------------------------
+--------------------+-----+
|              window|count|
+--------------------+-----+
|{2025-04-13 10:42...|    3|
|{2025-04-13 10:39...|    2|
|{2025-04-13 10:41...|    2|
|{2025-04-13 10:40...|    3|
+--------------------+-----+

# Kafka 데이터를 Spark로 처리

## • 실습
- 결과 예시
  - test-topic 에 타임스탬프 잘 생성되어 들어오는지 확인

{"id": 0, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 0", "timestamp": 1744459808.833915}
{"id": 1, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 1", "timestamp": 1744459809.836374}
{"id": 2, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 2", "timestamp": 1744459810.8384926}
{"id": 3, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 3", "timestamp": 1744459811.8401027}
{"id": 4, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 4", "timestamp": 1744459812.842712}
{"id": 5, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 5", "timestamp": 1744459813.8440083}
{"id": 6, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 6", "timestamp": 1744459814.8453846}
{"id": 7, "message": "\ud14c\uc2a4\ud2b8 \uba54\uc2dc\uc9c0 7", "timestamp": 1744459815.8469102}