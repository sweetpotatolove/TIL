
# Hadoop 클러스터 및 YARN 스케줄링 가이드

Hadoop의 분산 클러스터 구조 및 YARN 기반 리소스 스케줄링 구조를 이해하고, 실습을 통해 스케줄러를 변경하고 확인하는 과정을 정리합니다.

---

## 1. 클러스터 개요 및 구성

### 클러스터란?

- 여러 대의 서버(노드)가 하나의 시스템처럼 동작
- 대용량 데이터를 병렬 처리하기 위한 필수 구조
- Hadoop에서는 HDFS + YARN + MapReduce/Spark 등의 형태로 구성

---

## 2. Hadoop 클러스터 구성 요소

| 계층 | 구성요소 | 역할 |
|------|----------|------|
| 스토리지 | NameNode (Master) | 메타데이터 관리 |
| 스토리지 | DataNode (Worker) | 실제 데이터 저장 |
| 컴퓨팅 | ResourceManager | 작업 및 자원 스케줄링 총괄 |
| 컴퓨팅 | NodeManager | 개별 작업(Task) 실행 |
| 클라이언트 | 사용자 | 작업 제출 및 결과 수집 |

---

## 3. HDFS의 핵심 특징

- 블록 단위 저장: 기본 128MB 크기의 블록으로 쪼개어 저장
- 복제 저장: 기본 3개 복제 → 장애 복구 가능
- 데이터 무결성: 수정 불가, 병렬 처리에 적합
- 배치 최적화: 대용량 데이터를 순차적으로 처리

---

## 4. Hadoop V1 vs V2 비교

| 항목 | Hadoop V1 | Hadoop V2 (YARN) |
|------|-----------|------------------|
| 자원/작업 관리 | JobTracker 단일 처리 | ResourceManager + AppMaster 분산 처리 |
| 확장성 | 낮음 | 높음 |
| 장애 대응 | SPOF 존재 | 고가용성 구조 |
| 지원 엔진 | MapReduce | MR, Spark, Flink, Hive 등 |

---

## 5. YARN 구조 및 역할

| 용어 | 설명 |
|------|------|
| ResourceManager (RM) | 클러스터 전체 자원을 관리. 모든 ApplicationMaster를 통제 |
| NodeManager (NM) | 각 노드에 존재하며, 컨테이너 실행과 노드 자원 상태 보고를 담당 |
| Container | NM이 실행하는 작업 공간 (CPU, 메모리 포함). 하나의 Mapper, Reducer, Spark Executor 등이 실행됨 |
| ApplicationMaster (AM) | 각 Job의 전용 관리자. 작업 흐름 관리 및 컨테이너 요청 수행 |
| Client | Job을 제출하는 사용자 또는 프로그램 |

Note  
- Container ≠ Node  
- 컨테이너는 노드 위에 동적으로 생성되는 작업 실행 단위이며, 하나의 물리 노드에는 여러 컨테이너가 생성될 수 있음

---

## 6. MapReduce on YARN 실행 구조 예시

Hadoop V2부터 MapReduce는 YARN 위에서 실행되며, 아래와 같은 실행 구조

```
[사용자]
   ↓ (hadoop jar ...)
[ResourceManager] ← ApplicationMaster 실행 요청
   ↓
[NodeManager] → ApplicationMaster 실행 (Container 1)
   ↓
[ApplicationMaster] → ResourceManager에 Mapper/Reducer 실행 요청
   ↓
[여러 NodeManager들] → Mapper/Reducer 실행 (Container 2, 3, ...)
```

- ApplicationMaster는 MapReduce Job마다 하나씩 생성되며, 전체 작업 흐름(Mapper/Reducer 스케줄링)을 관리
- Mapper와 Reducer는 각각 별도의 컨테이너에서 실행
- 입력 데이터는 HDFS에서 읽고, 출력 역시 HDFS에 저장
- Shuffle 단계에서 Mapper의 출력이 네트워크를 통해 Reducer에게 전달되며, 이 과정에서 병목이 발생할 수 있음

### 특징

| 항목 | 설명 |
|------|------|
| Driver 역할 | ApplicationMaster가 수행 |
| 실행 단위 | Mapper, Reducer 각각 YARN Container로 실행 |
| 병렬성 | Mapper 개수 = 입력 스플릿 수, Reducer 개수는 사용자가 지정 가능 |
| 입출력 | 모두 HDFS 기반 |
| 통신 | Shuffle 시 네트워크 전송 발생 (Mapper → Reducer) |


## 7. 작업 간 통신 및 데이터 흐름

### Container 간 통신

- Mapper → Reducer 간 Shuffle 단계에서 네트워크 통신 발생
- 이때 Container 간 데이터가 전송되며, 디스크 I/O와 네트워크 병목의 주요 지점

### DataNode 간 통신

- 일반적으로 DataNode끼리 직접 통신하지 않음
- 모든 읽기/쓰기는 Client 또는 Application이 요청한 파일 블록을 각 DataNode로부터 병렬로 읽어오는 구조

---

## 8. YARN 작업 실행 흐름

1. 클라이언트 → ResourceManager에 Job 제출
2. NM이 ApplicationMaster 실행
3. RM이 AM에게 Container 위치 지정
4. AM이 NM에게 작업 실행 요청
5. 실행 후 상태 업데이트 및 결과 수신

---

## 9. YARN 스케줄링 필요성

- 여러 Job을 동시에 처리하려면 자원 충돌 최소화 필요
- 자원 효율성 및 응답속도 최적화를 위해 필요
- 스케줄링 없으면 자원 독점, 작업 지연, 성능 저하

---

## 10. 로그 조회 및 작업 모니터링

### 10.1 yarn-site.xml

```xml
<configuration>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>localhost</value>
  </property>
  
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>

  <!-- 추가 -->
  <property>
    <name>yarn.log-aggregation-enable</name>
    <value>true</value>
  </property>
</configuration>
```

### 10.2 yarn 기반 실행 테스트

1. HDFS에 디렉토리 생성 및 업로드
```bash
cd /home/my/my_hadoop/chapter2

# 입력 파일 생성
echo "Hello World Hello my" > test.txt

# HDFS에 디렉토리 생성 및 파일 업로드
hdfs dfs -mkdir -p /user/hadoop/input
hdfs dfs -put test.txt /user/hadoop/input/

# 업로드 확인
hdfs dfs -ls /user/hadoop/input
```

2. YARN 위에서 MapReduce 실행
```bash
hadoop jar /home/my/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.5.jar \
  wordcount /user/hadoop/input/test.txt /user/hadoop/output/map_output
```

### Application 목록 확인

```bash
yarn application -list -appStates ALL
```

### 개별 Job 로그 확인

```bash
yarn logs -applicationId <application_id>
```

로그 위치: $HADOOP_HOME/logs/

---

## 11. YARN 스케줄러 종류 및 설정

### $HADOOP_CONF_DIR 설정

```bash
vi ~/.bashrc

# 해당 내용 추가
export HADOOP_CONF_DIR=/home/my/hadoop/etc/hadoop
```

```bash
source ~/.bashrc
```

### (1) FIFO 스케줄러 (기본값)

```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fifo.FifoScheduler</value>
</property>
```

- 장점: 단순함
- 단점: 긴 작업이 자원 독점 가능

---

### (2) Capacity 스케줄러

```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler</value>
</property>
```

- 큐(Queue)별 자원을 비율로 분할

> capacity-scheduler.xml 예시

```xml
<!-- 기본 설정 (Configured Capacity): 큐에 할당된 자원 비율 -->
<property>
  <name>yarn.scheduler.capacity.root.default.capacity</name>
  <value>100</value>  <!-- 기본 자원 100% -->
</property>

<!-- 최대 설정 (Maximum Capacity): 큐가 점유할 수 있는 최대치 -->
<property>
  <name>yarn.scheduler.capacity.root.default.maximum-capacity</name>
  <value>100</value>  <!-- 최대 100%까지 확장 가능 -->
</property>
```

---

### (3) Fair 스케줄러

```xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>
```

- 자원을 사용자 간 공정하게 나눔
- 작업 독점 방지에 유리

---

## 12. 스케줄러 변경 적용 방법

```bash
# 설정 변경 후 YARN 재시작
stop-yarn.sh
start-yarn.sh
```

변경 확인

```bash
cat $HADOOP_HOME/etc/hadoop/yarn-site.xml | grep scheduler.class -A1
```

---

