# Spark RDD

## 챕터의 포인트
- RDD의 개념과 특징 이해
- RDD 생성 및 변환 학습

# RDD의 개념과 특징 이해

## RDD란?
- 대용량 데이터를 분산 처리하고 분석하기 위한 Spark의 기본 데이터 처리 단위
- Resilient (탄력적인)
- Distributed (분산된)
- Dataset (데이터셋)


## RDD의 특징

### 1. 데이터의 추상화 (Data Abstraction)

### 2. 탄력성(Resilient) & 불변성(Immutable)
- RDD는 한 번 생성되면 변경할 수 없음
- 어떤 노드(서버)가 장애로 인해 중단되더라도, 데이터 복구 가능

### 3. 타입의 안정성 보장
- 어떠한 하나의 타입의 객체를 가질 수 있음
- 데이터 타입을 컴파일 시전에 검사
- 성능 최적화
- 코드의 가독성과 유지보수성 향상
- Pyspark를 쓸 때는 Python이 동적 타입 언어이기 때문에 타입 안정성이 적용되지는 않음

### 4. 정형(Structured) & 비정형(Unstructured) 데이터
- 비정형 데이터: 고정된 포맷이 없는 텍스트 데이터  
  → sc.textFile()을 이용해 RDD로 로딩 후 map, filter, flatMap 등으로 가공
- 정형 데이터: 컬럼이 있는 테이블 형태 데이터  
  → DataFrame 또는 RDD.map()으로 가공

### 5. 지연 평가(Lazy Evaluation)
- 중간 연산을 줄여 성능 최적화
- 실행 계획을 최적화하여 성능 향상
- 불필요한 연산 방지로 리소스 절약

## 주요 구성 요소 정리 코드
```py
from pyspark import SparkContext

sc = SparkContext("local", "LazyEvalExample")

# 1. 텍스트 데이터 로딩 → Transformation
rdd = sc.parallelize(["apple", "banana", "spark", "data"])

# 2. 대문자로 바꾸기 → Transformation
upper_rdd = rdd.map(lambda x: x.upper())

# 3. SPARK가 포함된 문자열만 필터링 → Transformation
filtered_rdd = upper_rdd.filter(lambda x: "SPARK" in x)

# 지금까지는 아무것도 실행되지 않음!

# 4. 결과 확인 (Action)
result = filtered_rdd.collect()
```

# RDD 생성 및 변환 학습

## RDD 생성

### 1. 기존의 메모리 데이터를 RDD로 변환하는 방법
- Python의 리스트(List)나 Scala의 컬렉션(Collection)을 RDD로 변환 가능
- 이 방법은 주로 테스트나 작은 데이터 셋을 다룰 때 사용

### 2. 외부파일(텍스트, CSV, JSON 등)에서 RDD를 생성하는 방법
- 실무에서는 보통 파일이나 데이터베이스에서 데이터를 불러와야 함
- sc.textFile(“파일 경로”), spark.read.format("jdbc").option(…) 형태를 사용하여 외부 데이터를 RDD로 변환할 수 있음

## RDD 생성 : 메모리 데이터 활용(parallelize())

### Parallelize()
1. 기존 메모리 데이터를 Spark의 RDD로 변환하는 역할

- RDD parallelize() 생성 코드 예제 (Python / Scala / Java 비교)

```
# Parallelize in Python
wordsRDD = sc.parallelize([“fish”, “cats”, “dogs”])

// Parallelize in Scala
val wordsRDD = sc.parallelize(List(“fish”, “cats”, “dogs”))

// Parallelize in Java
JavaRDD<String> wordsRDD = sc.parallelize(Arrays.asList(“fish”, “cats”, “dogs”))
```

2. parallelize()는 메모리에 있는 데이터를 Spark 클러스터로 보낼 때 사용
- ≫ 데이터가 클 경우 비효율적일 수 있어 소규모 데이터분석에 주로 이용

## RDD 생성 : 외부 파일에서 데이터 읽기 (sc.textFile())

### sc.textFile()
1. 외부 파일에서 데이터를 직접 읽어와 RDD로 변환하는 역할
- ≫ 일반적인 텍스트 파일 (CSV, 로그 파일 등), S3 → 저장소에서 데이터 로드
  HBase, Cassandra (C* → NoSQL 데이터베이스에서 읽기 등

- RDD sc.textFile() 생성 코드 예제 (Python / Scala / Java 비교)

```
# Read a local text file in Python
linesRDD = sc.textFile(“/path/to/README.md”)

// Read a local text file in Scala
val linesRDD = sc.textFile(“/path/to/README.md”)

// Read a local text file in Java
JavaRDD<String> linesRDD = sc.textFile(“/path/to/README.md”)
```

## RDD 변환

### MAP
RDD의 각 요소에 함수 f 를 적용하여 새로운 RDD를 반환

```python
x = sc.parallelize(["b", "a", "c"])
y = x.map(lambda z: (z,1))
print (x.collect())
print (y.collect())
```

```python
x: ['b', 'a', 'c']
y: [('b',1), ('a',1), ('c',1)]
```

---

### FLATMAP
RDD의 모든 요소에 먼저 함수 f 를 적용한 뒤,  
그 결과를 평탄화(flatten)하여 새로운 RDD를 반환

```python
x = sc.parallelize([1, 2, 3])
y = x.flatMap(lambda x: (1*x, 2*x, 3*x, 100))
print(x.collect())
print(y.collect())
print(y.mean())
```

```python
x : [1, 2, 3]
y : [1, 2, 3, 100, 2, 4, 6, 100, 3, 6, 9, 100]
y.mean() : 28.0
```

---

### FILTER
filter의 조건을 만족하는 요소들만 포함하는 새로운 RDD를 반환

```python
x = sc.parallelize([1,2,3])
y = x.filter(lambda x: x%2 == 1) #keep odd value
print (x.collect())
print (y.collect())
```

```python
x: [1, 2, 3]
y: [1, 3]
```

---

### MAPPARTITIONS
RDD의 각 파티션에 함수 f 를 적용하여 새로운 RDD를 반환

```python
x = sc.parallelize([1,2,3],2)
def f(iterator):
        yield sum(iterator); yield 42

y = x.mapPartitions(f)
print(x.glom().collect())
print(y.glom().collect())
```

```python
x: [[1], [2, 3]]
y: [[1,42], [5,42]]
```

---

### MAPPARTITIONS WITH INDEX
원래 파티션의 인덱스를 추적하면서,  
RDD의 각 파티션에 함수를 적용하여 새로운 RDD를 반환

```python
x = sc.parallelize([1,2,3],2)
def f(partitionIndex, iterator):
        yield (partitionIndex, sum(iterator))

y = x.mapPartitionsWithIndex(f)
print(x.glom().collect())
print(y.glom().collect())
```

```python
x: [[1], [2, 3]]
y: [[0,1], [1,5]]
```

---

### KEYBY
원래 RDD의 각 항목에 대해 하나의 쌍(pair)을 생성하여  
Pair RDD를 만들고, 쌍의 key는 사용자 정의 함수에 의해 값으로부터 계산.

```python
x = sc.parallelize(['John', 'Fred', 'Anna', 'James'])
y = x.keyBy(lambda w: w[0])
print(y.collect())
```

```python
x: [['John', 'Fred', 'Anna', 'James']]
y: [('J', 'John'), ('F', 'Fred'), ('A', 'Anna'), ('J', 'James')]
```

---

### GROUPBY
원래 RDD의 데이터를 그룹화하기 위해,  
사용자 정의 함수의 출력값을 key로 하고  
이 key에 해당하는 모든 항목들을 value로 가지는 쌍(pair)을 생성

```python
x = sc.parallelize(['John', 'Fred', 'Anna', 'James'])
y = x.groupBy(lambda w: w[0])  # A function to generate keys
print({(t[0], [i for i in t[1]]) for t in y.collect()})
```

```python
x: ['John', 'Fred', 'Anna', 'James']
y: [('A', ['Anna']), ('J', ['John', 'James']), ('F', ['Fred'])]
```

```python
x = x.map(lambda w: (w[0], w))
y = x.groupByKey()
```

### GROUPBYKEY
원래 RDD에서 각 key에 해당하는 value들을 그룹화하고  
그룹화된 value들을 모아, 원래의 key와 함께 새로운 쌍(pair)을 생성

```python
x = sc.parallelize([('B',5),('B',4),('A',3),('A',2),('A',1)])
y = x.groupByKey()
print(x.collect())
print([(t[0],[i for i in t[1]]) for t in y.collect()])
```

```python
x: [('B',5),('B',4),('A',3),('A',2),('A',1)]
y: [('B', [5,4]), ('A', [3,2,1])]
```

### Word Counting 예시 (GROUPBYKEY)

```python
words = sc.parallelize(['one','two','two','three','three','three'])
wordPairsRdd = words.map(lambda w : (w,1))
wordCounts = wordPairsRdd.groupByKey().map(lambda pair: (pair[0], sum(pair[1])))

print(words.collect())
print(wordPairsRdd.collect())
print(wordCounts.collect())
```

```python
words: ['one', 'two', 'two', 'three', 'three', 'three']
wordPairsRDD: [('one', 1), ('two', 1), ('two', 1), ('three', 1), ('three', 1), ('three', 1)]
wordCounts: [('one', 1), ('two', 2), ('three', 3)]
```

### Word Counting 예시 (REDUCEBYKEY)

```python
words = sc.parallelize(['one','two','two','three','three','three'])
wordPairsRdd = words.map(lambda w : (w,1))
wordCounts = wordPairsRdd.reduceByKey(lambda cnt1, cnt2 : cnt1 + cnt2)

print(words.collect())
print(wordPairsRdd.collect())
print(wordCounts.collect())
```

```python
words: ['one', 'two', 'two', 'three', 'three', 'three']
wordPairsRDD: [('one', 1), ('two', 1), ('two', 1), ('three', 1), ('three', 1), ('three', 1)]
wordCounts: [('one', 1), ('two', 2), ('three', 3)]
```

### REDUCEBYKEY vs GROUPBYKEY
- 두 함수가 모두 사용 가능하다면, ReduceByKey를 사용
- ReduceByKey는 셔플 전에 행을 결합하여 셔플해야 할 행의 수를 줄일 수 있음  
  - 로컬 집계  
  - 중간 결과의 크기를 줄일 수 있음

### JOIN
join(otherRDD, numPartitions=None)  
원래 RDD들에서 같은 키를 가진 모든 요소 쌍(pair)을 포함하는 새로운 RDD를 반환

```python
x = sc.parallelize([("a",1), ("b", 2)])
y = sc.parallelize([("a",3), ("a", 4), ("b", 5)])
z = x.join(y)
print(z.collect())
```

```python
x: [("a",1), ("b", 2)]
y: [("a",3), ("a", 4), ("b", 5)]
z: [("a",(1,3)), ("a", (1,4)), ("b", (2,5))]
```

### UNION
union(otherRDD)  
두 개의 원래 RDD에서 모든 항목을 포함하는 새로운 RDD를 반환  
중복된 항목은 제거 X

```python
x = sc.parallelize([1,2,3], 2)
y = sc.parallelize([3,4], 1)
z = x.union(y)
print(z.glom().collect())
```

```python
x: [1, 2, 3]
y: [3, 4]
z: [[1], [2,3], [3,4]]
```

### DISTINCT
distinct(numPartitions=None)  
원래 RDD에서 중복을 제거한 고유한 항목들만 포함하는 새로운 RDD를 반환

```python
x = sc.parallelize([1, 2, 3, 3, 4])
y = x.distinct()
print(y.collect())
```

```python
x: [1, 2, 3, 3, 4]
y: [1, 2, 3, 4]
```

## RDD Fundamentals

### SAMPLE
- 머신 수가 많아질수록 처리 효율이 높아짐  
- Small data 추출을 통해 일부 샘플만으로도 통계적으로 의미 있는 근사치 확보

### SAMPLE
sample(withReplacement, fraction, seed=None)  
원래 RDD에서 통계적 샘플을 추출하여 구성한 새로운 RDD를 반환

```python
x = sc.parallelize([1,2,3,4,5])
y = x.sample(False, 0.4, 42)
print(x.collect())
print(y.collect())
```

```python
x: [1, 2, 3, 4, 5]
y: [1, 3]
```

## RDD 변환

### 파티셔닝 재분배 (Repartition VS Coalesce)

```python
# repartition: 파티션 수 늘리기 or 균등 재분배
df2 = df.repartition(6)
df2.rdd.getNumPartitions()

# coalesce: 파티션 수 줄이기 (shuffling 없음)
df3 = df.coalesce(2)
df3.rdd.getNumPartitions()
```

```python
>>> df.rdd.getNumPartitions()
8
>>> # repartition: 파티션 수 늘리기 or 균등 재분배
>>> df2 = df.repartition(10)
>>> df2.rdd.getNumPartitions()
10
>>> # coalesce: 파티션 수 줄이기 (shuffling 없음)
>>> df3 = df.coalesce(2)
>>> df3.rdd.getNumPartitions()
2
```

### COALESCE
coalesce(numPartitions, shuffle=False)  
파티션 수를 줄여서 구성한 새로운 RDD를 반환

```python
x = sc.parallelize([1, 2, 3, 4, 5], 3)
y = x.coalesce(2)
print(x.glom().collect())
print(y.glom().collect())
```

```python
x: [[1], [2, 3], [4, 5]]
y: [[1], [2, 3, 4, 5]]
```

# RDD 변환

## PARTITIONBY

partitionBy(numPartitions, partitioner=portable_hash)

사용자 정의 함수가 반환하는 파티션에 따라 원래 항목들을 배치하여, 지정한 개수의 파티션을 갖는 새로운 RDD를 반환

### 코드
```python
x = sc.parallelize([ ('J’, ‘James’), (‘F’, ‘Fred’), (‘A’, ‘Anna’),(‘J’, ‘James’)], 3)
y = x.partitionBy(2, lambda w: 0 if w[0] < 'H' else 1)
print(x.glom().collect())
print(y.glom().collect())
```

### 결과
```text
x: [[('J’, ‘James’)], [(‘F’, ‘Fred’), (‘A’, ‘Anna’)], [(‘J’, ‘James’)]]
y: [[(‘A’, ‘Anna’), (‘F’, ‘Fred’)], [(‘J’, ‘James’), (‘J’, ‘James’)]]
```

# RDD Action

## ACTIONS  
변환된 RDD 데이터를 메모리로 가져오거나, 저장하거나, 집계하는 연산

### collect()
| 연산 | 설명 | 예제 | 결과 |
|------|------|------|------|
| collect() | 모든 데이터를 리스트로 반환 | rdd.collect() | [1, 2, 3, 4] |
| count() | 전체 요소를 하나로 결합 | rdd.count() | 4 |
| reduce() | 전체 요소를 하나로 결합 | rdd.reduce(lambda a, b: a + b) | 10 |
| sum() | 요소의 합 반환 | rdd.sum() | 10 |
| mean() | 평균 값 반환 | rdd.mean() | 2.5 |

## COLLECT

RDD의 모든 항목을 하나의 리스트로 드라이버 프로그램으로 반환

### 코드
```python
x = sc.parallelize([1, 2, 3], 2)
y = x.collect()

print(x.glom().collect())
print(y)
```

### 결과
```text
x: [[1], [2, 3]]
y: [1, 2, 3]
```

## COUNTBYKEY

RDD에 있는 각 키의 등장 횟수를 세어 키와 그 개수로 이루어진 맵(map)을 반환

### 코드
```python
x = sc.parallelize([('J’, ‘James’), (‘F’, ‘Fred’), (‘A’,’Anna’), (‘J’,’John’)])
y = x.countByKey()
print(y)
```

### 결과
```text
x: [(‘J’, ‘James’), (‘F’, ‘Fred’), (‘A’,’Anna’), (‘J’,’John’)]
y: {‘J’ : 2, ‘F’ : 1, ‘A’ : 1}
```

## REDUCE

RDD의 모든 요소를 사용자 정의 함수를 이용해 요소와 중간 결과를 쌍(pairwise)으로 연속적으로 집계하여, 최종 결과를 드라이버 프로그램으로 반환

### 코드
```python
x = sc.parallelize([1, 2, 3, 4])
y = x.reduce(lambda a, b: a+b)

print(x.collect())
print(y)
```

### 결과
```text
x: [1, 2, 3, 4]
y: 10
```

## SUM

RDD에 있는 모든 항목의 합(sum)을 반환

### 코드
```python
x = sc.parallelize([2,4,1])
y = x.sum()

print(x.collect())
print(y)
```

### 결과
```text
x: [2, 4, 1]
y: 7
```

## MEAN

RDD에 있는 모든 항목의 평균(mean)을 반환

### 코드
```python
x = sc.parallelize([2,4,1])
y = x.mean()

print(x.collect())
print(y)
```

### 결과
```text
x: [2, 4, 1]
y: 2.3333333
```