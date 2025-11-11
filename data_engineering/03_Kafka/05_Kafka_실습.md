목차..



# Kafka 기초 개념 및 세팅
## 실습1
### 학습목표
Java를 설치하고 환경 변수를 설정한 뒤, Zookeeper를 설치·실행하고, Kafka를 다운로드·설치한 후 실행 테스트를 진행

### Step1: Java 설치 및 환경 변수 설정
- Java 17이 설치되어 있어야 합니다.
```bash
sudo apt update                     # 패키지 업데이트
sudo apt install openjdk-17-jdk     # Java 17 설치
```
- `java -version` 명령어를 실행하여 설치를 확인합니다.
```bash
java -version
# 정상 출력 예시:
# openjdk version "17.x.x"
```
- Java가 설치되지 않았다면, OpenJDK를 다운로드하고 설치합니다.

- Java 경로 설정 (환경 변수 등록)
```bash
# `JAVA_HOME`을 설정하면 Kafka 실행 시 Java 경로를 명확히 인식할 수 있습니다.
# `/bin/java`를 제외한 경로를 `JAVA_HOME`으로 설정합니다.
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 환경 변수 설정 확인:
echo $JAVA_HOME

# 정상 출력 예시:
/usr/lib/jvm/java-17-openjdk-amd64
```

### Step2: Kafka 다운로드 및 설치
- 공식 Apache Kafka 사이트에서 Kafka를 다운로드합니다.
```bash
# 다운로드
wget https://dlcdn.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz 

# 압축해제
tar -xvzf kafka_2.12-3.9.0.tgz

# Kafka 폴더 이동
sudo mv kafka_2.12-3.9.0 /home/ssafy/kafka
```
- 압축을 해제하고 `config/server.properties` 파일을 확인하여 설정을 조정합니다.

### Step3: Zookeeper 설치 및 실행
- Kafka에는 기본적으로 Zookeeper가 포함되어 있습니다.
- `config/zookeeper.properties` 파일을 수정하여 Zookeeper 설정을 확인합니다.
- 아래의 명령어로 Zookeeper를 실행합니다.
```bash
# Zookeeper 실행
cd /home/ssafy/kafka
./bin/zookeeper-server-start.sh config/zookeeper.properties

# 정상 로그 예시:
binding to port 0.0.0.0/0.0.0.0:2181
```

### Step4: Kafka 실행 테스트
- Zookeeper가 실행 중인 상태에서 다음 명령어를 실행하여 Kafka 브로커를 실행합니다.
- 새로운 터미널을 열어 Kafka 브로커를 실행합니다.
```bash
cd /home/ssafy/kafka
./bin/kafka-server-start.sh config/server.properties

# 정상 로그 예시:
started (kafka.server.KafkaServer)
```

## 실습2
### 학습목표
Kafka 브로커를 실행하고 상태를 확인한 뒤, 기본적인 Kafka 명령어(토픽 목록 및 브로커 정보 확인 등)를 실행하고 브로커를 종료합니다.

### Step1: Kafka 브로커 실행
- Zookeeper가 실행 중인지 확인합니다
```bash
ps -ef | grep zookeeper
```
- Kafka 브로커를 백그라운드에서 실행합니다
    - &를 사용하여 백그라운드 실행
    - 표준 출력 및 오류를 logs/kafka.log 파일에 저장
```bash
bin/kafka-server-start.sh config/server.properties > logs/kafka.log 2>&1 &
```
- 실행된 Kafka 프로세스를 확인하려면
```bash
ps -ef | grep kafka
```

### Step2: Kafka 상태 확인
- Kafka가 정상 실행 중인지 확인하기 위해 다음 명령어를 실행합니다
```bash
bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```
- 이 명령어는 현재 실행 중인 브로커의 API 버전을 출력합니다.

### Step3: Kafka 기본 명령어 실행
- 토픽 목록 확인
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
- 생성된 토픽이 없으면 출력이 비어 있습니다. 이는 정상적인 동작이며, 이후 실습에서 토픽을 생성할 것입니다.

- 브로커 정보 확인
```bash
bin/kafka-topics.sh --describe --topic test-topic --bootstrap-server localhost:9092
```
- 이후 실습에서 test-topic을 직접 생성할 것이므로 현재는 오류가 발생할 수 있습니다.

### Step4: Kafka 브로커를 종료하고 로그를 확인
- Kafka 브로커를 종료하는 방법
```bash
bin/kafka-server-stop.sh
```
- `bin/kafka-server-stop.sh`를 실행하면 안전하게 브로커가 종료됩니다.
- 실행 로그를 확인하는 방법:
```bash
cat logs/kafka.log | tail -n 50
```
- `logs/kafka.log` 파일에서 마지막 50줄을 확인하여 실행 상태를 점검할 수 있습니다.

## 실습3
### 학습목표
토픽 생성, 설정, 삭제

### Step1: 새로운 토픽을 생성하세요.
- 다음 명령어를 사용하여 test-topic이라는 이름의 토픽을 생성합니다.
```bash
bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```
- `--partitions 3`: 해당 토픽을 3개의 파티션으로 생성
- `--replication-factor 1`: 복제본을 하나만 유지

### Step2: 생성된 토픽의 상세 정보를 확인하세요.
- 생성된 토픽의 설정 및 상태를 확인합니다.
```bash
bin/kafka-topics.sh --describe –topic test-topic --bootstrap-server localhost:9092
```
- 토픽의 파티션 개수, 복제본 정보, 로그 크기 등을 출력

    ![alt text](image-133.png)

### Step3: 토픽 설정을 변경하세요.
- 특정 토픽의 설정 값을 변경할 수 있습니다. 
- 예를 들어, 메시지 보존 기간을 변경하려면:
```bash
bin/kafka-configs.sh --alter --topic test-topic --bootstrap-server localhost:9092 --add-config retention.ms=600000
```
- `retention.ms=600000`: 메시지를 10분 동안 유지 (600,000 밀리초)

### Step4: 토픽을 삭제하세요.
- 불필요한 토픽을 삭제하려면 다음 명령어를 실행합니다.
```bash
bin/kafka-topics.sh --delete --topic test-topic --bootstrap-server localhost:9092
```

**※ 주의**: 기본적으로 Kafka는 토픽 삭제가 비활성화되어 있을 수 있으므로, server.properties 파일에서 `delete.topic.enable=true` 설정을 확인해야 합니다.


## 실습4
### 학습목표
Kafka 토픽을 생성하고, 프로듀서를 실행해 메시지를 전송한 뒤, 컨슈머를 실행하여 메시지를 수신하고 메시지 송수신 테스트를 수행합니다.

### Step1: Kafka 토픽 생성
- 이전 실습에서 토픽이 삭제되었으므로 새롭게 new-topic을 생성합니다.
```bash
bin/kafka-topics.sh --create --topic new-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
- `--partitions 1`: 1개의 파티션을 가진 토픽을 생성합니다.
- `--replication-factor 1`: 복제본을 하나만 유지합니다.

- 생성된 토픽을 확인
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
![alt text](image-134.png)

### Step2: Kafka 프로듀서를 실행하여 메시지 전송
- Kafka 프로듀서를 실행하여 new-topic에 메시지를 보냅니다.
```bash
bin/kafka-console-producer.sh --topic new-topic --bootstrap-server localhost:9092
```
- 실행 후 메시지를 입력하면 new-topic으로 전송됩니다. 
- 예를 들어:
```bash
Hello Kafka!
This is a test message.
```
- 입력한 메시지는 Kafka 브로커를 통해 new-topic에 저장됩니다.

### Step3: Kafka 컨슈머를 실행하여 메시지 수신
- Kafka 컨슈머를 실행하여 new-topic의 메시지를 읽습니다.
```bash
bin/kafka-console-consumer.sh --topic new-topic --from-beginning --bootstrap-server localhost:9092
```
- `--from-beginning` 옵션을 사용하면 해당 토픽의 모든 메시지를 처음부터 읽을 수 있습니다.
- 컨슈머 실행 후 프로듀서에서 보낸 메시지가 출력되는지 확인합니다.

    ![alt text](image-135.png)

### Step4: 메시지 송수신 테스트 수행하세요.
- 프로듀서에서 추가적으로 메시지를 입력하고, 컨슈머에서 해당 메시지가 정상적으로 출력되는지 확인합니다.
- 컨슈머 실행 창에서 추가로 입력한 메시지가 출력되어야 합니다.
- 컨슈머가 메시지를 정상적으로 받지 못하면 Kafka 브로커가 실행 중인지 확인해야 합니다.


## 실습5
### 학습목표
세 개의 Kafka 브로커를 실행하고, replication-factor 3이 적용된 토픽을 생성하여 상태를 확인한 뒤, 메시지 송수신 테스트를 수행하고 한 브로커를 중단한 후 데이터 복구를 확인합니다

### Step1: 세 개의 Kafka 브로커 실행
- 브로커 설정 파일 생성 및 수정
- 기존 server.properties 파일을 복사하여 추가 브로커 설정 파일을 생성합니다.
```bash
cp config/server.properties config/server-1.properties
cp config/server.properties config/server-2.properties
```
- 각 설정 파일을 수정합니다.
```properties
# config/server-1.properties
broker.id=1
listeners=PLAINTEXT://localhost:9093
log.dirs=/tmp/kafka-logs-1
```
```properties
# config/server-2.properties○
broker.id=2
listeners=PLAINTEXT://localhost:9094
log.dirs=/tmp/kafka-logs-2
```
- 세 개의 브로커 실행 
```bash
bin/kafka-server-start.sh config/server.properties &
bin/kafka-server-start.sh config/server-1.properties &
bin/kafka-server-start.sh config/server-2.properties &
```
- 브로커가 정상적으로 동작하는지 확인
```bash
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
bin/kafka-topics.sh --list --bootstrap-server localhost:9093
bin/kafka-topics.sh --list --bootstrap-server localhost:9094
```
![alt text](image-136.png)

### Step2: 토픽을 생성하고 상태 확인
- 아래 명령어로 토픽 생성
```bash
bin/kafka-topics.sh --create --topic replicated-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 3
```
- `--partitions 1`: 하나의 파티션만 생성하여 실습을 단순화함
- `--replication-factor 3`: 세 개의 브로커에서 복제본 유지
- 생성된 토픽 상태 확인
```bash
bin/kafka-topics.sh --describe --topic replicated-topic --bootstrap-server localhost:9092
```

### Step3: 메시지 송수신 테스트 수행  
- 프로듀서 실행
```bash
bin/kafka-console-producer.sh --topic replicated-topic --bootstrap-server localhost:9092
```
- 메시지를 입력
```bash
Message from replicated cluster
Another message○
```
- 컨슈머 실행
```bash
bin/kafka-console-consumer.sh --topic replicated-topic --from-beginning --bootstrap-server localhost:9092
```

### Step4: 하나의 브로커 중단 후 데이터 복구를 확인
- 실행 중인 브로커 중 하나를 종료합니다.
```bash
# 실행 중인 Kafka 프로세스 확인
ps -ef | grep kafka
kill -9 $(ps -ef | grep 'kafka.Kafka' | grep server-2.properties | awk '{print $2}') # 9094 브로커 종료
```
- 컨슈머를 실행하여 메시지가 정상적으로 소비되는지 확인합니다.
```bash
bin/kafka-console-consumer.sh --topic replicated-topic --bootstrap-server localhost:9093 --from-beginning
```



