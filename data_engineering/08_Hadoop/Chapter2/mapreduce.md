# Hadoop MapReduce 처리

WSL 환경에서 Hadoop 기반 MapReduce 개념을 이해하고, Java 내장 예제 및 Python 기반 사용자 정의 MapReduce까지 실습하는 과정을 정리
(네트워크 이슈 방지를 위해 Local 환경을 권장)

---

## 개념 요약: Hadoop MapReduce

| 항목 | 설명 |
|------|------|
| 목적 | 대규모 데이터 병렬 처리 (Google의 분산 처리 모델 구현체) |
| 기반 구조 | Key-Value 형태의 데이터 처리 |
| 처리 단계 | Split → Map → Shuffle → Reduce |
| 실행 방식 | 1. Java 내장 예제  2.Hadoop Streaming (Python 등 외부 스크립트 지원) |

---

## MapReduce 처리 흐름 요약

```
[입력파일] → Split → Mapper (key2, value2) → Combiner (선택) → 
→ Shuffle + Sort → Reducer (key3, value3) → HDFS에 최종 저장
```

---

## 개념 정리: MapReduce 처리 요소 요약

| 요소 | 설명 |
|------|------|
| Split | 데이터를 블록 단위로 나누어 병렬처리 기초 형성 |
| Map | 입력 → (key2, value2) 형태로 변환 |
| Shuffle | 동일 key 데이터를 하나로 모음 (네트워크 통신 발생) |
| Reduce | key 기준으로 그룹핑하여 결과 생성 |
| Combiner | 중간 데이터를 Mapper 측에서 사전 집계 (선택적) |
| Partitioner | 데이터를 Reducer로 분배하는 기준 (기본: 해시 기반) |

---


## MapReduce 한계 및 확장

- 디스크 I/O 병목 (중간 결과 디스크 저장)
- 실시간 처리 부적합 (Batch 전용)
- 복잡한 개발 부담 (Java 또는 Streaming 스크립트 필요)

---

## MapReduce 처리 구조 요약 

```
[HDFS에 데이터 저장]
       ↓
[MapReduce Job 실행]
       ├─ Mapper: key-value 출력 (디스크 임시 저장)
       ├─ Shuffle & Sort: 디스크 기반 정렬/조인
       └─ Reducer: key별 처리 후 HDFS 저장
       ↓
[결과 HDFS에 저장]

```

---

## Spark 처리 구조 요약 

```
[HDFS/S3/Local에 데이터 저장]
       ↓
[Spark Job 실행 (RDD/DataFrame 기반)]
       ├─ map(), filter(), groupBy(), reduceByKey() 등 연속 처리
       └─ 메모리 기반의 연산 수행
       ↓
[최종 결과 저장 (HDFS, DB, Elasticsearch 등)]


```

---

## mapred-site.xml 필수 설정 (환경 변수 연동)

Hadoop 실행 중 오류 방지를 위해, `mapred-site.xml` 파일에 다음 설정을 반드시 추가해야 합니다.
(docker compose 파일에는 적용되어있음)

Hadoop이 `/home/my/hadoop`에 설치되어 있다면

```xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>

  <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=/home/my/hadoop</value>
  </property>

  <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=/home/my/hadoop</value>
  </property>

  <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=/home/my/hadoop</value>
  </property>
</configuration>
```

> `mapreduce` 작업이 내부적으로 참조하는 jar 파일 경로가 제대로 설정되지 않으면 실행 시 오류가 발생합니다.

---

## 데몬 재시작 (환경 설정 반영)

설정 후 반드시 모든 Hadoop 데몬을 재시작해야 반영됩니다.

```bash
# 데몬 중지
stop-yarn.sh
stop-dfs.sh

# 데몬 재시작
start-dfs.sh
start-yarn.sh
```

---

## 확인 방법

설정이 제대로 되었는지 확인하려면 다음 경로에 jar 파일이 존재하는지 체크합니다.

```bash
ls /home/my/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-client-app-*.jar
```

정상적으로 존재한다면 설정이 올바르게 반영된 것입니다.

---

## 실습 1: Hadoop 내장 WordCount 예제 실행

### 1. 입력 파일 업로드

```bash
# 새로 띄울 때 cluster ID 달라지는 이슈가 생기면 hadoop data를 저장한 디렉토리 제거 후 재실행

cd /home/my/my_hadoop/chapter2

# 입력 파일 생성
echo "Hello World Hello my" > test.txt

# HDFS에 디렉토리 생성 및 파일 업로드
hdfs dfs -mkdir -p /user/hadoop/input
hdfs dfs -put test.txt /user/hadoop/input/

# 업로드 확인
hdfs dfs -ls /user/hadoop/input
```

---

#### Step 1: Split 단계

HDFS에 업로드된 파일은 내부적으로 Split 단위로 나뉘어 Mapper에게 전달됩니다.

예상 논리 Split (단순 예시):

```text
Split 1: "Hello World"
Split 2: "Hello my"
```

---

#### Step 2: Mapper 단계

각 Split은 Mapper로 전달되어 Key-Value 쌍으로 변환됩니다.

| Split         | Mapper 출력                  |
| ------------- | -------------------------- |
| "Hello World" | ("Hello", 1), ("World", 1) |
| "Hello my" | ("Hello", 1), ("my", 1) |

총 결과:

```text
("Hello", 1), ("World", 1), ("Hello", 1), ("my", 1)
```

---

#### Step 3: Shuffle & Sort 단계

동일한 key를 기준으로 정렬 및 그룹핑하여 Reducer에게 전달합니다.

```text
("Hello", [1, 1])
("World", [1])
("my", [1])
```

---

#### Step 4: Reducer 단계

Reducer는 같은 key에 대한 value 리스트를 모두 합산합니다.

| 단어    | 합산 결과 |
| ----- | ----- |
| Hello | 2     |
| World | 1     |
| my | 1     |

최종 출력:

```text
("Hello", 2), ("World", 1), ("my", 1)
```

---

#### Step 5: Output 저장

Reducer의 결과는 OutputFormat을 통해 HDFS에 저장됩니다.

> `/user/hadoop/output/map_output` 디렉토리는 존재하면 안 됨 (기존 출력 삭제 필요 시 아래 명령어 사용)

```bash
hdfs dfs -rm -r /user/hadoop/output/wordcount_out
```

#### 실행 명령어 (Hadoop 내장 예제)

```bash
hadoop jar /home/my/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar \
    wordcount /user/hadoop/input/test.txt /user/hadoop/output/wordcount_out
```

#### 결과 확인

```bash
hadoop fs -cat /user/hadoop/output/wordcount_out/part-r-00000
```

#### 예상 출력 결과

```text
Hello   2
my   1
World   1
```

---

## 실습 2: Hadoop Streaming + Python Mapper & Reducer

### 1. Python 스크립트 작성

**mapper.py**
```python
#!/usr/bin/env python3
import sys, re

for line in sys.stdin:
    words = re.findall(r'\b[a-z]+\b', line.strip().lower())
    for word in words:
        print(f"{word}\t1")
```

**reducer.py**
```python
#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t')
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word:
    print(f"{current_word}\t{current_count}")
```

- 실행 권한 부여

```bash
cd /home/my/my_hadoop/chapter2
chmod +x mapper.py reducer.py

# 도커로 실행 시
docker cp /home/my/h_Hadoop/chapter2/mapper.py namenode:mapper.py
docker cp /home/my/h_Hadoop/chapter2/reducer.py namenode:reducer.py

```

> `mapper.py`, `reducer.py` 파일은 현재 디렉토리에 있어야 하며, Hadoop이 실행 시 전달받을 수 있도록 `-file` 옵션을 사용합니다.

### 2. Hadoop Streaming 실행

출력 디렉토리가 이미 존재하면 삭제:

```bash
hdfs dfs -rm -r -f /user/hadoop/output/custom_output
```

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar \
  -input /user/hadoop/input/test.txt \
  -output /user/hadoop/output/custom_output \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -file mapper.py \
  -file reducer.py
```
> `#!/usr/bin/env python3`는 스크립트를 실행 가능한 형태로 인식시키기 위한 선언입니다.  
> Hadoop Streaming에서는 `"python3 mapper.py"`와 같이 직접 인터프리터를 지정했기 때문에 필수는 아닙니다.

- `-mapper`: 사용할 Mapper 프로그램 (stdin에서 입력받아 stdout으로 출력)
- `-reducer`: 사용할 Reducer 프로그램
- `-file`: Hadoop 클러스터로 전달할 로컬 스크립트



### 3. 결과 확인

```bash
hdfs dfs -cat /user/hadoop/output/custom_output/part-00000
```

#### 예상 출력 결과

```text
hello   2
my   1
world   1
```

---