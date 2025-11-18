# PySpark 설치 및 실습 가이드

## 1. Spark 다운로드 및 설치

```bash
cd /home/ssafy

# Spark 3.5.4 다운로드
wget https://archive.apache.org/dist/spark/spark-3.5.4/spark-3.5.4-bin-hadoop3.tgz

# 압축 해제
tar -xvzf spark-3.5.4-bin-hadoop3.tgz

# /home/ssafy/spark 로 이동
sudo mv spark-3.5.4-bin-hadoop3 /home/ssafy/spark
```

---

## 2. Spark 환경변수 등록

```bash
vi ~/.bashrc
```

파일 마지막에 아래 내용 추가:
```bash
export SPARK_HOME=/home/ssafy/spark
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
```

변경 사항 적용:
```bash
source ~/.bashrc
```

환경변수 설정 확인:
```bash
echo $SPARK_HOME
# 출력: /home/ssafy/spark
```

---

## 3. Spark 실행 확인

```bash
spark-shell
```

정상 실행되면 `Ctrl + D`로 종료.

---

## 4. PySpark 설치

```bash
pip install pyspark==3.5.4
```

---

## 5. PySpark 기본 예제

```python
from pyspark.sql import SparkSession

# Spark 세션 생성
spark = SparkSession.builder.appName("App").getOrCreate()

# Spark 버전 출력
print("Spark Version:", spark.version)

# 간단한 연산
a = 5
b = 10
print("a + b =", a + b)
print("a * b =", a * b)

# Spark 세션 종료
spark.stop()
```

---

## 6. sc.textFile() 활용

### 6.1 테스트 파일 생성
```bash
echo "Hello Spark Apache Spark is powerful Big Data Processing" > test.txt
```

---

### 6.2 파일 읽기
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TextFileExample").getOrCreate()
sc = spark.sparkContext

# 파일 읽기
rdd = sc.textFile("test.txt")
```

---

### 6.3 현재 파티션 개수 확인
```python
print("파티션 개수:", rdd.getNumPartitions())
```

---

### 6.4 파티션 수를 1개로 변경
```python
rdd_single = rdd.repartition(1)
print("변경된 파티션 개수:", rdd_single.getNumPartitions())
```

---

## 7. RDD 액션 & 트랜스포메이션 예제

### 7.1 collect() — 전체 데이터 조회
```python
print(rdd.collect())
```
> 모든 데이터를 배열 형태로 반환 (Action 연산)  
> **주의:** 대규모 데이터에서는 사용 지양.

---

### 7.2 count() — 줄 개수 세기
```python
print("줄 개수:", rdd.count())
```

---

### 7.3 filter() — 특정 단어 포함 줄만 필터링
```python
filtered = rdd.filter(lambda line: "Spark" in line)
print(filtered.collect())
```
> 조건을 만족하는 요소만 포함하는 새로운 RDD 생성 (Transformation 연산).

---

### 7.4 map() — 모든 단어를 소문자로 변환
```python
lower = rdd.map(lambda line: line.lower())
print(lower.collect())
```
> RDD의 각 요소를 변환하여 새로운 RDD 생성 (Transformation 연산).

---

## 8. Spark 세션 종료
```python
spark.stop()
```
