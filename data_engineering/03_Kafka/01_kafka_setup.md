# Kafka 설치 및 실행 가이드

## 0. Java 설치

Kafka는 Java 기반이므로 JDK가 필요합니다.

1) 패키지 업데이트
```bash
sudo apt update
```

2) Java 17 설치
```bash
sudo apt install openjdk-17-jdk
```

3) 설치 확인
```bash
java -version
```
정상 출력 예시:
```
openjdk version "17.x.x"
```

4) Java 경로 설정 (환경 변수 등록)

`JAVA_HOME`을 설정하면 Kafka 실행 시 Java 경로를 명확히 인식할 수 있습니다.

`/bin/java`를 제외한 경로를 `JAVA_HOME`으로 설정합니다.

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

```

> 이슈 발생 시
```bash
vi ~/.bashrc
```

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
```
```bash
source ~/.bashrc
```

환경 변수 설정 확인:
```bash
echo $JAVA_HOME
```

정상 출력 예시:
```
/usr/lib/jvm/java-17-openjdk-amd64
```

---

## 1. Kafka 다운로드 및 설치

1) Kafka 다운로드
```bash
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz
```

2) 압축 해제
```bash
tar -xvzf kafka_2.12-3.9.0.tgz
```

3) Kafka 폴더 이동 
```bash
sudo mv kafka_2.12-3.9.0 /home/ssafy/kafka
```

---

## 2. Zookeeper 실행

Kafka 실행 전에 Zookeeper가 먼저 실행되어야 합니다.

1) Zookeeper 실행
```bash
cd /home/ssafy/kafka
./bin/zookeeper-server-start.sh config/zookeeper.properties
```

정상 로그 예시:
```
binding to port 0.0.0.0/0.0.0.0:2181
```

---

## 3. Kafka 브로커 실행

새로운 터미널을 열어 Kafka 브로커를 실행합니다.

```bash
cd /home/ssafy/kafka
./bin/kafka-server-start.sh config/server.properties
```

정상 로그 예시:
```
started (kafka.server.KafkaServer)
```

---

## 4. 테스트: 토픽 생성 및 메시지 송수신

1) 토픽 생성
```bash
cd /home/ssafy/kafka

./bin/kafka-topics.sh --create \
  --topic lecture-test-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

2) 메시지 전송 (Producer)
```bash
./bin/kafka-console-producer.sh \
  --topic lecture-test-topic \
  --bootstrap-server localhost:9092
```
> 실행 후 메시지를 입력하면 전송됩니다.

3) 메시지 수신 (Consumer)
새로운 터미널을 열어 실행합니다.
```bash
./bin/kafka-console-consumer.sh \
  --topic lecture-test-topic \
  --from-beginning \
  --bootstrap-server localhost:9092
```
> Producer에서 전송한 메시지가 Consumer 터미널에 출력되면 성공입니다.

---
## 4. 토픽 삭제

1) 토픽 삭제 (해당 토픽이 안뜨면 정상, 아무것도 없으면 아무것도 안뜸)
```bash
./bin/kafka-topics.sh --delete --topic lecture-test-topic --bootstrap-server localhost:9092
```

-  확인
```bash
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```

> 메타데이터가 남아있어 삭제가 안된 형태로 나타나는 경우가 잦음
> 삭제 후 이슈가 해결이 잘 안되는 경우에는 우선 토픽명을 바꿔서 테스트하길 권장
> 데이터(메시지) 자체와 메타데이터(클러스터 상태)를 다르게 처리합니다.
> 메타데이터는 보통 Zookeeper나 Kafka의 내부 상태로 관리합니다.
> 이 메타데이터들은 데이터와는 달리 소비되거나 삭제되지 않고 계속 남아 있습니다.
> 토픽(Topic)은 일반적으로 자주 삭제되지 않으며, 대체로 지속적으로 사용되는 리소스입니다.
> 그래서 테스트를 위해 토픽명을 변경하면서 실행하는 것도 방법이 될 수 있을 것 같습니다.

2) 토픽 삭제가 안되는 경우
```bash
vi config/server.properties 
```

```bash
delete.topic.enable=true
```
---

## 5. 종료 방법

1) Zookeeper 종료  
실행 중인 터미널에서 `Ctrl + C`

2) Kafka 종료  
실행 중인 터미널에서 `Ctrl + C`

---