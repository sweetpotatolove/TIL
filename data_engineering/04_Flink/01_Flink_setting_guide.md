# Apache Flink 1.19 설치 및 WSL2 네트워크 설정 가이드

## 1. Flink 설치 및 권한 설정

```bash

# Flink 1.19 다운로드 및 압축 해제
cd /home/ssafy
wget https://archive.apache.org/dist/flink/flink-1.19.3/flink-1.19.3-bin-scala_2.12.tgz
tar -xvzf flink-1.19.3-bin-scala_2.12.tgz
mv flink-1.19.3 flink
```

## 2. Flink 설정 변경

```bash
cd /home/ssafy/flink
cd conf
```

다음 항목들을 추가 또는 수정(파일 제공)

```bash
vi config.yaml
```

```yaml
jobmanager.bind-host: 0.0.0.0
rest.address: 0.0.0.0
rest.bind-address: 0.0.0.0
```

## 3. 클러스터 시작 및 UI 접속

```bash
cd /home/ssafy/flink/bin
./start-cluster.sh
```

- 웹 UI 접속: [http://localhost:8081](http://localhost:8081)

> 실행 시 `localhost`가 아닌 `Desktop-xxxx`와 같은 이름으로 뜰 수 있음  

---

## 네트워크 구조

### localhost란?

- `127.0.0.1`: 내 컴퓨터 내부에서만 접근 가능한 주소
- **“이 컴퓨터에서만 들어올 수 있는 문”**

### 0.0.0.0이란?

- “이 컴퓨터가 가진 **모든 네트워크 인터페이스에 대해 열어줌**”
- 즉, `localhost`, 내부 IP, 외부 IP 모두 포함

### WSL1 vs WSL2

| 항목 | WSL1 | WSL2 |
|------|------|------|
| 네트워크 공유 | Windows와 IP 공유 | 가상 네트워크 (IP 분리) |
| localhost 공유 | 가능 | 기본 불가능 (포트포워딩 필요) |
| 해결 방법 | 기본 공유됨 | `0.0.0.0` 바인딩 필수 |

### WSL2에서 0.0.0.0을 써도 괜찮은가?

- 대부분 NAT(Network Address Translation)로 외부에서 접근 불가
- Windows에서 보안 관리하므로, WSL 내에서 포트 개방은 상대적으로 안전
- Windows 브라우저에서 WSL 서버에 접속하려면 `0.0.0.0` 필수

---


## Socket 예제 실행

```bash
# 포트 확인
nc -l 9000  # 또는 9000 등 비어 있는 포트 확인

# 예제 실행
cd /home/ssafy/flink/
./bin/flink run examples/streaming/SocketWindowWordCount.jar --hostname localhost --port 9000
```

---

## Flink 로그 실시간 확인

```bash
cd /home/ssafy/flink/
tail -f log/flink-*.out
```

### tail 옵션 설명

- `tail`: 파일 마지막 부분 출력
- `-f`: 파일 변경사항을 실시간으로 추적하며 출력
- `log/flink-*.out`: Flink 로그 파일 전체 지정 (`standalonesession`, `taskexecutor` 등 포함)

---

## Flink 클러스터 종료

```bash
./stop-cluster.sh
```

---

## Docker를 통한 Flink 띄우기

### 1. 프로젝트 구조

```
pyflink_project/
├── Dockerfile
├── docker-compose.yml
├── pyflink_job.py  ← 실행할 PyFlink 코드
```

---

### 2. Dockerfile – PyFlink 실행 환경 이미지 만들기

```dockerfile
FROM flink:1.19-scala_2.12-java17

# 2. Python & pip 설치 + PyFlink 설치
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir apache-flink==1.19.3 && \
    pip install pandas

# 3. 기본 Python3 링크 설정
RUN ln -s /usr/bin/python3 /usr/bin/python

# 4. 작업 디렉토리 설정
WORKDIR /opt/flink

```

---

### 3. docker-compose.yml – Flink 클러스터 구성

```yaml
services:
  jobmanager:
    image: pyflink
    container_name: flink_jobmanager
    hostname: jobmanager
    ports:
      - "8081:8081"
    command: jobmanager
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager

  taskmanager:
    image: pyflink
    container_name: flink_taskmanager
    depends_on:
      - jobmanager
    command: taskmanager
    environment:
      - JOB_MANAGER_RPC_ADDRESS=jobmanager
    scale: 1

```

---

### 4. PyFlink Job 예제 (pyflink_job.py)

```python
from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

data = env.from_collection([("apple", 1), ("banana", 1), ("apple", 1)])
data.print()

env.execute("PyFlink Docker Job")
```

---

### 5. 실행 순서

### (1) Docker 이미지 빌드
```bash
docker build -t pyflink .
```

### (2) 클러스터 실행
```bash
docker-compose up -d
```

### (3) PyFlink job 파일을 JobManager 컨테이너로 복사
```bash
docker cp pyflink_job.py flink_jobmanager:/opt/flink/pyflink_job.py
```

### (4) JobManager 컨테이너에서 실행
```bash
docker exec -it flink_jobmanager python /opt/flink/pyflink_job.py
```

---