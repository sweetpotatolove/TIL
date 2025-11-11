
# Kafka 모니터링 가이드

---

## 실습 구성 요약

- Kafka & Zookeeper 기동  
- JMX Exporter 연동  
- Prometheus 설정  
- Grafana 대시보드 구축  
- Kafka 토픽 및 메시지 실습  
- Docker Compose 대체 방식

---

## 디렉토리 구조
```bash
/home/ssafy/
├── kafka/
│   └── jmxterm.jar 
    └── jmx_exporter/
        ├── config.yaml
        └── jmx_prometheus_javaagent-0.17.2.jar
├── kafka_exporter/
│   └── kafka_exporter
├── prometheus/
│   ├── prometheus.yml
│   └── ...
├── grafana/
│   └── bin/grafana-server
└── kafka-monitoring/
    ├── docker-compose.yml
    ├── prometheus.yml
    └── jmx_exporter/
        ├── config.yaml
        └── jmx_prometheus_javaagent-0.17.2.jar
```

---

## 1. Zookeeper & Broker 실행 
```bash
cd /home/ssafy/kafka
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

---

## 2. Kafka JMX 환경변수 설정 및 실행 


### Broker 재실행
- 브로커 종료 후 해당 터미널에서 실행

```bash
# Kafka가 JMX를 통해 메트릭을 외부로 노출하게
export KAFKA_OPTS="-Dcom.sun.management.jmxremote \
-Dcom.sun.management.jmxremote.authenticate=false \
-Dcom.sun.management.jmxremote.ssl=false \
-Dcom.sun.management.jmxremote.port=9999 \
-Dcom.sun.management.jmxremote.rmi.port=9999 \
-Djava.rmi.server.hostname=localhost"
```

```bash
cd /home/ssafy/kafka
./bin/kafka-server-start.sh config/server.properties
```

---

## 3. JMXTerm 설치 및 사용
```bash
cd /home/ssafy/kafka
wget https://github.com/jiaqi/jmxterm/releases/download/v1.0.2/jmxterm-1.0.2-uber.jar -O jmxterm.jar
```

```bash
java -jar jmxterm.jar -l localhost:9999
```

```jmxterm
$> bean java.lang:type=Memory
$> get HeapMemoryUsage
```

---

## 4-1. JMX Exporter 연동
```bash
mkdir -p /home/ssafy/kafka/jmx_exporter
cd /home/ssafy/kafka/jmx_exporter
wget https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.17.2/jmx_prometheus_javaagent-0.17.2.jar
```

```bash
vi config.yaml
```

```yaml
# /home/ssafy/kafka/jmx_exporter/config.yaml
lowercaseOutputLabelNames: true
rules:
  - pattern: ".*"
```

### Broker 재실행
- 브로커 종료 후 해당 터미널에서 실행

```bash
# KAFKA_OPTS 변경 - JMX Exporter Java Agent 설정 (JMX 메트릭을 Prometheus 형식으로 변환하여 Prometheus가 수집할 수 있게)
export KAFKA_OPTS="$KAFKA_OPTS -javaagent:/home/ssafy/kafka/jmx_exporter/jmx_prometheus_javaagent-0.17.2.jar=9094:/home/ssafy/kafka/jmx_exporter/config.yaml"
```


```bash
cd /home/ssafy/kafka
./bin/kafka-server-start.sh config/server.properties
```

---

## 4-2. Kafka Exporter 연동
- kafka_exporter는 Kafka 브로커의 여러 메트릭을 JMX를 통해 수집
- 브로커의 메시지 처리량, 레코드 지연 시간, 파티션 상태, Consumer 그룹의 오프셋 등을 모니터링할 수 있게 함

### 설치
```bash
cd /home/ssafy/
wget https://github.com/danielqsj/kafka_exporter/releases/download/v1.7.0/kafka_exporter-1.7.0.linux-amd64.tar.gz
tar -xvzf kafka_exporter-1.7.0.linux-amd64.tar.gz
mv kafka_exporter-1.7.0.linux-amd64 kafka_exporter
cd kafka_exporter
./kafka_exporter --kafka.server=localhost:9092 --web.listen-address=":9308"
```

## 5. Prometheus 설치 및 실행
```bash
cd /home/ssafy
wget https://github.com/prometheus/prometheus/releases/download/v2.47.2/prometheus-2.47.2.linux-amd64.tar.gz
tar -xvzf prometheus-2.47.2.linux-amd64.tar.gz
mv prometheus-2.47.2.linux-amd64 prometheus
cd prometheus
```

## 6. Prometheus 설정 파일 작성

```bash
vi prometheus.yml
```
```yaml
# prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "kafka" # JMX Exporter
    static_configs:
      - targets: ["localhost:9094"]

  - job_name: "kafka-exporter"
    static_configs:
      - targets: ["localhost:9308"]
```
> Docker 환경에서는 `localhost` 대신 각 컨테이너 이름 사용
> ex : `"localhost:9094"` -> `"kafka:9094"`
> ex : `"localhost:9098"` -> `"kafka-exporter:9098"`
> 단, prometheus는 시스템적으로 본인을 참조하기때문에 `"localhost:9090"` 그대로

### 실행
```
./prometheus --config.file=prometheus.yml
```

---

## 7. Prometheus UI 확인

브라우저에서 접속:
```
http://localhost:9090
```

- http://localhost:9090/targets 확인

---

## 8. Grafana 설치 및 실행
```bash
cd /home/ssafy/
wget https://dl.grafana.com/oss/release/grafana-10.2.2.linux-amd64.tar.gz
tar -xvzf grafana-10.2.2.linux-amd64.tar.gz
mv grafana-v10.2.2 grafana
cd grafana
./bin/grafana-server
```

---

## 9. Grafana 설정 및 시각화

- 접속: `http://localhost:3000`
- 로그인: `admin / admin` (최초 로그인 시 변경)

### 데이터 소스 추가
- Prometheus 선택
- URL: `http://localhost:9090`
- Save & Test

### 대시보드

- Dashboard ID: 예시 링크에서 복사 (721)
- `+` → `Import` → 붙여넣기 → `Load`
- Configure a new data source 클릭 후, Add data source에서 Prometheus 클릭
- Connection에서 상단의 URL 입력
- 해당 소스로 DashBoard 생성
- 대시보드에서 하단의 토픽 관련 그래프가 보이지 않으므로 2행의 3개의 그래프 쿼리 수정 필요

```prometheus
sum by(topic) (
  kafka_server_BrokerTopicMetrics_OneMinuteRate{name="MessagesInPerSec", topic!="__consumer_offsets"}
)

sum by(topic) (
  kafka_server_BrokerTopicMetrics_OneMinuteRate{name="BytesInPerSec", topic!="__consumer_offsets"}
)

sum by(topic) (
  kafka_server_BrokerTopicMetrics_OneMinuteRate{name="BytesOutPerSec", topic!="__consumer_offsets"}
)
```

---


## 10. Kafka 명령어 테스트 (동작 확인용)
```bash
cd /home/ssafy/kafka/
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092
./bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
./bin/kafka-topics.sh --describe --topic test-topic --bootstrap-server localhost:9092
ls /home/ssafy/kafka/logs
```

### 10-1. Kafka 토픽 및 메시지 테스트

```bash
./bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092
./bin/kafka-console-consumer.sh --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```

---

## 11. Docker Compose

```yaml
services:
  zookeeper:
    container_name: zookeeper
    image: confluentinc/cp-zookeeper:7.5.0
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    container_name: kafka
    image: confluentinc/cp-kafka:7.5.0
    ports:
      - "9092:9092"
      - "29092:29092"
      - "9094:9094"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092,PLAINTEXT_HOST://0.0.0.0:29092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_OPTS: >-
        -javaagent:/jmx_exporter/jmx_prometheus_javaagent-0.17.2.jar=9094:/jmx_exporter/config.yaml
    volumes:
      - ./jmx_exporter:/jmx_exporter
    depends_on:
      - zookeeper


  kafka-exporter:
    container_name: kafka-exporter
    image: danielqsj/kafka-exporter
    ports:
      - "9308:9308"
    entrypoint: /bin/sh
    command: ["-c", "sleep 20 && /bin/kafka_exporter --kafka.server=kafka:9092"]
    depends_on:
      - kafka
    restart: always

  prometheus:
    container_name: prometheus
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    container_name: grafana
    image: grafana/grafana
    ports:
      - "3000:3000"
```

## 12. Kafka 토픽 및 메시지 테스트 (Docker 환경)

### 토픽 생성
```bash
docker exec -e KAFKA_OPTS="" -it kafka kafka-topics \
  --bootstrap-server localhost:9092 \
  --create --topic test-topic --partitions 1 --replication-factor 1
```

### 메시지 전송
```bash
docker exec -e KAFKA_OPTS="" -it kafka kafka-console-producer \
  --broker-list localhost:9092 --topic test-topic
```

### 메시지 소비
```bash
docker exec -e KAFKA_OPTS="" -it kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic test-topic --from-beginning --timeout-ms 5000
```