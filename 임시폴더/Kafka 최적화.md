# Kafka 최적화

## 챕터의 포인트
- Kafka 성능 최적화
- 프로듀서 및 컨슈머의 성능 튜닝
- 주요 설정 파라미터 이해
- Kafka 데이터의 저장

# Kafka 성능 최적화 개론

## Kafka의 성능 최적화가 필요한 이유
- Kafka의 성능 최적화가 필요한 이유
  - 대규모 트래픽 처리: 데이터의 처리량(Throughput) 및 지연(Latency) 최적화
  - 안정성 개선: 데이터 손실에 대한 안정성(Durability)를 높임
  - 리소스의 효율적 사용: 제한된 리소스를 최대한 활용하며 자원 부하를 낮춤

- 성능 최적화 주요 지표
  - 프로듀서 컨슈머의 처리 속도
  - 브로커 및 주키퍼 설정
  - 스토리지, 네트워크 등 자원 최적화

# 프로듀서 및 컨슈머 성능 튜닝

## Producer 성능 최적화

### 직렬화 방식 선정
1. **StringSerializer**: 단순한 문자열 직렬화, 문자열을 UTF-8로 인코딩, 압축 효율 낮음  
2. **ByteArraySerializer**: 데이터를 그대로 바이트 배열로 직렬화, 다양한 형식 처리 가능, 빠른 변환 / 부족한 사용성  
3. **JsonSerializer**: JSON 형식으로 직렬화, 가독성 높지만 압축 효율 낮음  
4. **AvroSerializer**: Avro 포맷을 사용한 직렬화, 스키마 기반, 압축 효율이 좋고 빠름 (Kafka 권장 방식)

### StringSerializer
```python
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})
# 메시지 전송
producer.produce(
    topic='test-topic',
    key='my_key'.encode('utf-8'),
    value='Hello Kafka!'.encode('utf-8')
)

# 내부 전송 큐 처리
producer.poll(0)
# 메시지 전송 완료 대기
producer.flush()
```

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,      # 문자열 UTF-8 인코딩
    value_serializer=str.encode     # 문자열 UTF-8 인코딩
)

producer.send('test-topic', key='my_key', value='Hello Kafka!')
producer.flush()
```

---

### ByteArraySerializer
```python
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

producer.produce(
    topic='test-topic',
    key='my_key'.encode('utf-8') if 'my_key' else None,
    value=b'BinaryData' if isinstance(b'BinaryData', bytes) else b'BinaryData'.encode()
)

producer.poll(0)
producer.flush()
```

```python
producer = KafkaProducer(
  bootstrap_servers='localhost:9092',
  key_serializer=lambda k: k.encode() if k else None,
  value_serializer=lambda v: v if isinstance(v, bytes) else v. encode()
)

producer.send('test-topic', key='my_key', value=b'BinaryData')
```

---

### JsonSerializer
```python
import json
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

producer.produce(
    topic='test-topic',
    value=json.dumps({"name": "Alice", "age": 25}).encode('utf-8')
)

producer.poll(0)
producer.flush()
```

---

```python
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON 직렬화 후 UTF-8 인코딩
)

producer.send('test-topic', value={"name": "Alice", "age": 25})
producer.flush()
```

### Producer 성능 최적화
- 직렬화 방식 선정
  - AvroSerializer: Avro 포맷을 사용한 직렬화, 스키마 기반, 압축 효율이 좋고 빠름 (Kafka 권장 방식)

```python
from kafka import KafkaProducer
from fastavro import parse_schema, schemaless_writer
import io

# 1️. Avro 스키마 정의
avro_schema = {
    "type": "record",
    "name": "User",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"}
    ]
}
parsed_schema = parse_schema(avro_schema)

# 2️. 메시지 직렬화
record = {"name": "Alice", "age": 25}
bytes_writer = io.BytesIO()
schemaless_writer(bytes_writer, parsed_schema, record)
avro_bytes = bytes_writer.getvalue()

# 3️. Kafka Producer 생성 및 전송
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,
    value_serializer=lambda v: avro_bytes   # 이미 직렬화됨
)

producer.send('avro-topic', key='user1', value=avro_bytes)
producer.flush()
```
```python
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

schema_registry_conf = {'url': 'http://localhost:8081'}
schema_registry_client = SchemaRegistryClient(schema_registry_conf)

avro_schema = """
{
  "type": "record",
  "name": "User",
  "fields": [
    {"name": "name", "type": "string"},
    {"name": "age", "type": "int"}
  ]
}
"""

avro_serializer = AvroSerializer(schema_registry_client, avro_schema)

producer = SerializingProducer({
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': str.encode,
    'value.serializer': avro_serializer
})

producer.produce(topic='test-topic', key='user1', value={"name": "Alice", "age": 25})
producer.flush()
```

# 프로듀서 및 컨슈머 성능 튜닝

## Producer 성능 최적화
### 파티셔닝 방식 선정

1. **key 기반 파티셔닝**: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. 특정 파티션 지정: 바이트 배열 그대로 전송  
3. StickyPartitioner: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
4. 커스텀 파티셔너: 본인만의 로직을 만든 파티셔너  

```python
# 1. Kafka Producer 설정
producer = SerializingProducer({
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': StringSerializer('utf_8')
})

# 2. 전송할 key 리스트
keys = ["user1", "user2", "user3", "user1", "user2"]

# 3. 메시지 전송
for i, key in enumerate(keys):
    value = f"Data {i}"
    producer.produce(topic="test-topic", key=key, value=value)
    print(f"Sent: Key={key}, Value={value}")

# 4. 전송 완료 보장
producer.flush()
```

1. **key 기반 파티셔닝**: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. 특정 파티션 지정: 바이트 배열 그대로 전송  
3. StickyPartitioner: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
4. 커스텀 파티셔너: 본인만의 로직을 만든 파티셔너  

```python
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,   # Key를 UTF-8로 변환
    value_serializer=str.encode  # Value를 UTF-8로 변환
)

for i in range(5):
    producer.send('test-topic', value=f"Fixed Partition Data {i}", partition=0)
    print(f"Sent to Partition 0: Message {i}")

producer.flush()
```

1. key 기반 파티셔닝: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. **특정 파티션 지정**: 바이트 배열 그대로 전송  
3. StickyPartitioner: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
4. 커스텀 파티셔너: 본인만의 로직을 만든 파티셔너  

```python
# 1. Kafka Producer 설정
producer = SerializingProducer({
    'bootstrap.servers': 'localhost:9092',
    'key.serializer': StringSerializer('utf_8'),
    'value.serializer': StringSerializer('utf_8')
})

# 2. 고정 파티션 0으로 메시지 전송
for i in range(5):
    value = f"Fixed Partition Data {i}"
    producer.produce(
        topic="test-topic",
        value=value,
        partition=0
    )
    print(f"Sent to Partition 0: Message {i}")

# 3. 전송 완료 보장
producer.flush()
```

1. key 기반 파티셔닝: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. 특정 파티션 지정: 바이트 배열 그대로 전송  
3. **StickyPartitioner**: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
   (같은 파티션에 여러 메시지를 모아서 보내고, 일정 조건이 되면 다른 파티션으로 바꾸는 전략)  
4. 커스텀 파티셔너: 본인만의 로직을 만든 파티셔너  

| 메시지 번호 | 파티션 예시 |
|-------------|-------------|
| message-0 | 1 |
| message-1 | 1 |
| message-2 | 1 |
| message-3 | 1 |
| message-4 | 1 |
| message-5 | 2 |
| message-6 | 2 |
| message-7 | 2 |
| message-8 | 0 |
| message-9 | 0 |

```python
# 1. Kafka Producer 설정
producer = SerializingProducer({
    'bootstrap.servers': 'localhost:9092',
    'value.serializer': StringSerializer('utf_8')  # Key 없이 Value만 설정
})

# 2. Key 없이 메시지 전송 (Sticky 파티셔너 적용됨)
for i in range(10):
    value = f"Sticky Message {i}"
    producer.produce(topic="test-topic", value=value)
    print(f"Sent Message {i}")

# 3. 전송 완료 보장
producer.flush()
```

1. key 기반 파티셔닝: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. 특정 파티션 지정: 바이트 배열 그대로 전송  
3. **StickyPartitioner**: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
   (같은 파티션에 여러 메시지를 모아서 보내고, 일정 조건이 되면 다른 파티션으로 바꾸는 전략)  
4. 커스텀 파티셔너: 본인만의 로직을 만든 파티셔너  

```python
from kafka import KafkaProducer
from kafka.partitioner.default import DefaultPartitioner

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=str.encode,     # UTF-8 인코딩
    # partitioner=DefaultPartitioner() # 기본 해싱 파티셔너 (라운드로빈 방식)
)

# Key 없이 메시지를 전송하면 Sticky Partitioner가 자동 적용됨
for i in range(10):
    producer.send('test-topic', value=f"Sticky Message {i}")
    print(f"Sent Message {i}")

producer.flush()
```

1. key 기반 파티셔닝: 해시 기반, 같은 key를 가진 값들끼리 같은 파티션 배치  
2. 특정 파티션 지정: 바이트 배열 그대로 전송  
3. StickyPartitioner: 정수 값을 바이너리 데이터로 변환, Batch를 최대한 활용하여 RoundRobin보다 효율적  
4. **커스텀 파티셔너**: 본인만의 로직을 만든 파티셔너 (kafka-python 라이브러리 사용)  
> (confluent-kafka-python은 내부적으로 C 라이브러리인 `librdkafka`를 감싸서 구현되어 있기 때문에 불가능)

```python
from kafka import KafkaProducer, partitioner

class CustomPartitioner:
    def __call__(self, key, all_partitions, available_partitions):
        key_int = int(key.decode())  # Key를 정수로 변환
        return key_int % len(all_partitions)  # 해시 계산: 짝수는 0번, 홀수는 1번 파티션

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=str.encode,
    value_serializer=str.encode,
    partitioner=CustomPartitioner()  # 사용자 지정 파티셔너 적용
)

for i in range(10):
    producer.send('test-topic', key=str(i), value=f"Message {i}")
    print(f"Sent Key={i}, Value=Message {i}")

producer.flush()
```

### Batching 설정 최적화
1. **buffer.memory**: 프로듀서 내부에서 저장할 수 있는 RA 버퍼의 최대 크기, 기본값 32MB  
   (confluent-kafka에는 해당 옵션 없음)  
2. **batch.size**: 한 batch의 크기, 해당 크기가 다 차면 전송 준비. 기본값 16KB  
3. **linger.ms**: Batch가 만들어지는 최대 대기 시간. 해당 시간이 지나면 다 안 차도 전송 준비. 기본값 없음  

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=str.encode,
    buffer_memory=33554432,  # 32MB (기본값)
    batch_size=32768,        # 32KB (기본값: 16KB보다 크게 설정해 배칭 효율 증가)
    linger_ms=5              # 5ms 동안 배치를 기다렸다가 전송 (기본값: 0)
)

for i in range(100):
    producer.send('test-topic', value=f"Batching Message {i}")

producer.flush()
```

## Producer 성능 최적화
### Compression 방식 결정
1. Gzip: 높은 압축률, 느린 처리속도, 높은 CPU 사용량 → 확실한 압축  
2. LZ4: 적당한 압축률, 준수한 처리속도, 중간 정도의 CPU 사용량 → 균형잡힌 압축과 CPU 사용  
3. Snappy: 낮은 압축률, 빠른 처리속도, 낮은 CPU 사용량 → 빠른 압축과 CPU 절약  

| Metrics | Uncompressed | Gzip | Snappy | LZ4 |
|----------|---------------|------|---------|-----|
| Avg latency (ms) | 65 | 10.41 | 10.1 | 9.26 |
| Disk space (MB) | 10 | 0.92 | 2.18 | 2.83 |
| Effective compression ratio | 1 | 0.09 | 0.21 | 0.28 |
| Process CPU usage (%) | 2.35 | 11.46 | 7.25 | 5.89 |

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    compression_type='gzip',  # Gzip 압축 적용, 'snappy', 'lz4' 가능
    value_serializer=str.encode
)

for i in range(10):
    producer.send('test-topic', value=f"Gzip Message {i}")
    print(f"Sent Gzip Message {i}")

producer.flush()
```

## Producer 성능 최적화
### Acknowledge 방식 결정
1. acks=0: 프로듀서가 메시지를 보내고 확인하지 않음  
2. acks=1: 리더 브로커만 받으면 성공  
3. **acks=all(-1)**: 모든 복제본이 메시지를 수신할 때까지 대기 (기본값)  
4. min.insync.replicas: 복제본 중 실제로 응답해야 하는 최소 개수, 기본값 1 (2 이상 권장)

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=str.encode,
    acks='all'  # 또는 0, 1
)

producer.send('test-topic', value='Critical Message')
producer.flush()
```

### Acknowledge 방식 결정
1. acks=0: 프로듀서가 메시지를 보내고 확인하지 않음  
2. acks=1: 리더 브로커만 받으면 성공  
3. acks=all(-1): 모든 복제본이 메시지를 수신할 때까지 대기 (기본값)  
4. **min.insync.replicas**: 복제본 중 실제로 응답해야 하는 최소 개수, 기본값 1 (2 이상 권장)

```bash
# config/server.properties 예시
75 # For anythin other than development testing, a value greater than 1 is recommended to ensure availability such as 3.
76 offsets.topic.replication.factor=1
77 transaction.state.log.replication.factor=1
78 transaction.state.log.min.isr=1
79 min.insync.replicas=2
```


## Producer 성능 최적화
### Transaction
1. `kafka-python`은 transaction 관리 기능이 없고, `confluent_kafka`는 존재  
2. Transaction이 너무 길지 않도록 관리 필요  

```python
from confluent_kafka import Producer

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
    'transactional.id': 'my-transactional-producer',  # 트랜잭션 ID
    'enable.idempotence': True,
    'acks': 'all',
    'retries': 5,
    'max.in.flight.requests.per.connection': 5
})

# 트랜잭션 초기화 (최초 1회)
producer.init_transactions()

# 트랜잭션 시작
producer.begin_transaction()

try:
    for i in range(5):
        producer.produce('tx-topic', key=f'key-{i}', value=f'value-{i}')

    # 커밋
    producer.commit_transaction()
    print("Committed successfully")
except Exception as e:
    # 롤백
    print(f"Transaction failed: {e}")
    producer.abort_transaction()
```

## Producer 성능 최적화
### Retry 관련 옵션 결정
1. retries: 몇 번까지 재시도할지 설정, 기본값 `INT_MAX`  
2. max.in.flight.requests.per.connection: Ack를 받지 않고 보낼 수 있는 동시 요청 개수 (기본값 5)  
3. enable.idempotence: 멱등성 프로듀서 설정 (중복 전송 방지), 기본값 `true`

```python
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=str.encode,
    retries=5,
    max_in_flight_requests_per_connection=1,
    enable_idempotence=True
)

for i in range(10):
    producer.send('reliable-topic', value=f"Message {i}")
    print(f"Sent message {i}")

producer.flush()
```

## Consumer 성능 최적화
### Coordinator 설정 최적화
1. heartbeat.interval.ms: heartbeat 간격, `session.timeout.ms`의 1/3 수준이 적당, 기본값 3초  
2. session.timeout.ms: heartbeat를 기다리는 시간, 이 이상이면 해당 컨슈머 제거 후 rebalance, 기본값 10초  
3. max.poll.records: 컨슈머가 한 번에 가져올 수 있는 최대 데이터 수, 기본값 500  
4. max.poll.interval.ms: polling 호출 간격. 이 이상이면 컨슈머 제거 후 rebalance, 기본값 5분  

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'coordinator-test',
    bootstrap_servers='localhost:9092',
    group_id='group-1',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    max_poll_records=100,
    session_timeout_ms=15000,
    heartbeat_interval_ms=5000,
    max_poll_interval_ms=60000,
    value_deserializer=lambda v: v.decode('utf-8')
)

for msg in consumer:
    print(f"[{msg.partition}] {msg.offset} -> {msg.value}")
    # time.sleep(10)  # simulate slow processing
```

## Consumer 성능 최적화
### Fetching 방식 선정
1. fetch.min.byte: 가져올 최소 데이터 크기, 기본값 1 → Throughput과 비례, Latency 반비례  
2. fetch.max.byte: 한 번에 받을 수 있는 최대 데이터 크기, 기본값 50MB → 클수록 대량 처리 가능  
3. fetch.max.wait.ms: 데이터가 모일 때까지 기다리는 최대 시간, 기본값 500ms  
4. max.partition.fetch.bytes: 파티션 하나당 가져올 수 있는 최대 데이터, 기본값 1MB  

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'fetch-test',
    bootstrap_servers='localhost:9092',
    group_id='fetch-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: x.decode('utf-8'),
    fetch_min_bytes=1024,                         # 최소 1KB 이상 받아야 응답
    fetch_max_bytes=10 * 1024 * 1024,             # 최대 10MB 응답 허용
    fetch_max_wait_ms=1000,                       # 최대 1초 대기
    max_partition_fetch_bytes=2 * 1024 * 1024     # 파티션당 2MB
)

for msg in consumer:
    print(f"[{msg.partition}] {msg.offset} -> {msg.value}")
```

## Consumer 성능 최적화
### Partitioning 관련 설정
1. RangeAssignor: 토픽당 N개씩 연속된 파티션 분배 (기본값)  
2. RoundRobinAssignor: 컨슈머 수에 맞게 순차 배분  
3. StickyPartitionAssignor: 기존 할당을 유지하면서 변경 최소화  
4. CooperativeStickyAssignor: Sticky를 기본으로 하지만 일부 컨슈머 변경 시에도 나머지 작동

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    group_id='group-A',
    auto_offset_reset='earliest',
    partition_assignment_strategy=[
        "org.apache.kafka.clients.consumer.RoundRobinAssignor"
    ]
)
```

## Consumer 성능 최적화
### Partitioning 관련 설정
1. RangeAssignor: 토픽당 N개씩 연속된 파티션 분배 (기본값)  
2. RoundRobinAssignor: 컨슈머 수에 맞게 순차 배분 → 균등 분배  
3. StickyPartitionAssignor: 기존 할당을 유지하면서 변경 최소화 → 리밸런싱 시 파티션 유지 우선  
4. CooperativeStickyAssignor: Sticky를 기반으로 하지만 일부 컨슈머 변경 → Zero-Downtime 리밸런싱

```text
[
 "org.apache.kafka.clients.consumer.RangeAssignor",
 "org.apache.kafka.clients.consumer.RoundRobinAssignor",
 "org.apache.kafka.clients.consumer.StickyPartitionAssignor",
 "org.apache.kafka.clients.consumer.CooperativeStickyAssignor"
]
```

## Consumer 성능 최적화
### Commit 관련 설정
1. enable.auto.commit: 주기적으로 offset을 커밋, 기본값 `true`
2. auto.commit.interval.ms: 주기적으로 offset을 커밋하는 간격, 기본값 5초

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'auto-commit-topic',
    bootstrap_servers='localhost:9092',
    group_id='test-group',
    enable_auto_commit=True,             # 자동 커밋 활성화 (기본값)
    auto_commit_interval_ms=5000,        # 5초마다 오프셋 커밋
    auto_offset_reset='earliest',
    value_deserializer=lambda v: v.decode('utf-8')
)

for msg in consumer:
    print(f"Received: {msg.value} (Offset: {msg.offset})")
```
💡 메시지를 가져오면 5초마다 커밋 → 실패해도 커밋 → 데이터 유실 가능


## Consumer 성능 최적화
### Commit 관련 설정 (수동 커밋)
1. enable.auto.commit: 주기적으로 offset을 커밋, 기본값 true
2. auto.commit.interval.ms: 주기적으로 offset을 커밋하는 간격, 기본값 5초

```python
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'manual-commit-topic',
    bootstrap_servers='localhost:9092',
    group_id='test-group',
    enable_auto_commit=False,            # 수동 커밋 사용
    auto_offset_reset='earliest',
    value_deserializer=lambda v: v.decode('utf-8')
)

for msg in consumer:
    print(f"Processing: {msg.value} (Offset: {msg.offset})")

    # 정상적으로 처리 완료 후 오프셋 커밋
    consumer.commit()
    print(f"Committed offset {msg.offset}")
```

💡 수동으로 커밋 호출 → 정상처리 확인 후 커밋 (데이터 유실 방지)

## Consumer 성능 최적화
### 수동 Commit 전략
1. Batch 단위 처리: 프로듀서의 Batch처럼 일정 데이터 모이면 처리 → 대용량 데이터 적합  
2. 주기 처리: 일정 시간마다 처리 → 시간 기반 데이터 적합 (예: 실시간 로그)  
3. 정상처리 후 커밋: 메시지 단위로 처리 확인 후 커밋 → 안전하지만 높은 부하 (예: 금융 시스템)  
4. 1+N Hybrid: N개 처리 후 마지막 메시지만 커밋 → 안정성과 효율성의 중간, Kafka 권장

```python
BATCH_SIZE = 100
messages = []
last_offset = None

for msg in consumer:
    process(msg)
    messages.append(msg)
    last_offset = msg.offset

    if len(messages) >= BATCH_SIZE:
        consumer.commit()
        print(f"Committed offset at {last_offset}")
        messages = []
```

## Consumer 성능 최적화
### auto.offset.reset 설정값
- earliest: 가장 초기의 offset 값으로 설정 → 처음부터 다시 시작해야 할 때  
- latest: 가장 마지막의 offset 값으로 설정 → 실시간 데이터 소비  
- none: 이전 offset 값을 찾지 못하면 error 발생  

```python
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    group_id='my-group',
    auto_offset_reset='latest'  # 처음부터 다시 읽기
)
```

Kafka 메시지 로그 예시

| Offset | Message | Consumer 처리 |
|--------|----------|----------------|
| 0 | Hello |  |
| 1 | World |  |
| 2 | Kafka! |  |
| 3 | Streaming... |  |
| 4 | Start | Consumer: Start |
| 5 | New | Consumer: New |
| 6 | System | Consumer: System |

# Kafka 주요 파라미터의 이해

## Topic 및 Replica 관련 설정
- num.partitions: 파티션 수 조정 (기본값 1, 거의 안 씀), 한 번 설정 후 줄일수 는 없음.  
- replication.factor: 파티션별 replica 수  
- min.sync.replicas: 정상 동작해야 하는 최소 replica 수  

```bash
kafka-topics.sh --create --topic my-topic \
  --partitions 3 --replication-factor 2 \
  --bootstrap-server localhost:9092
```

```bash
kafka-topics.sh --alter --topic my-topic \
  --partitions 6 --bootstrap-server localhost:9092   # ✅ 가능

kafka-topics.sh --alter --topic my-topic \
  --partitions 1 --bootstrap-server localhost:9092   # ❌ 불가능
```

## Topic 및 Replica 관련 설정
- num.partitions: 파티션 수 조정 (기본값 1, 거의 안 씀), 한 번 설정 후 줄일수 는 없음.  
- replication.factor: 파티션별 replica 수, 기본값 1(거의 안 씀)
- min.sync.replicas: 정상 동작해야 하는 최소 replica 수  

```bash
kafka-topics.sh --create --topic my-topic \
  --partitions 3 --replication-factor 3 \
  --bootstrap-server localhost:9092
```

```json
{
  "version": 1,
  "partitions": [
    {"topic": "my-topic", "partition": 0, "replicas": [1, 2, 3]},
    {"topic": "my-topic", "partition": 1, "replicas": [2, 3, 1]},
    {"topic": "my-topic", "partition": 2, "replicas": [3, 1, 2]}
  ]
}
```

```bash
kafka-reassign-partitions.sh --execute \
  --bootstrap-server localhost:9092 \
  --reassignment-json-file reassigned.json
```

## 네트워크 및 메모리 설정 최적화
### 네트워크 및 메모리 관련 주요 설정값
- socket.send/receive.buffer.bytes: 네트워크 버퍼 크기, 기본값 100KB, 0 설정 시 자동 조정(추천)  
- log.flush.interval.messages/ms: 로그 플러시 주기 조절, 기본값 `Long.MAX_VALUE`  
- message.max.byte: 브로커가 수용 가능한 메시지 최대 크기, 기본값 1MB, 10MB 이상 넘기지 않는것 추천 
- num.network.threads: 네트워크 요청 처리 스레드 수, 기본값 3, CPU 코어 수와 비슷하게 설정

📄 config/server.properties
```properties
# 1. 네트워크 최적화
socket.send.buffer.bytes=512000
socket.receive.buffer.bytes=512000
num.network.threads=8

# 2. 메시지 크기 최적화 (최대 5MB 허용)
message.max.bytes=5242880

# 3. 로그 플러시 주기 최적화
log.flush.interval.messages=10000
log.flush.interval.ms=1000
```

## 브로커 리소스 최적화

### 기타 브로커 리소스 설정값
- KAFKA_HEAP_OPTS: 카프카가 사용할 JVM 힙 메모리 크기, 기본값 1GB, 4~8GB 추천
- num.io.threads: Disk I/O 스레드 수, 기본값 8, CPU 코어에 맞춰 높이기  
- replica.fetch.min.bytes: 팔로워가 리더로부터 받는 데이터 크기,기본값 1 Byte, 1MB 정도 추천

📄 terminal
```bash
export KAFKA_HEAP_OPTS="-Xmx8G -Xms8G"  # 8GB 메모리 사용
```
> 너무 커지면 (16GB 이상) JAVA GC를 고려해야 함 

📄 config/server.properties
```properties
num.io.threads=16                      # I/O 스레드 개수 증가
replica.fetch.min.bytes=1048576        # 1MB 이상 모아서 복제
```
> HDD일때는 CPU 코어보다 적게, NVMe 같은 고성능 장치는 그 이상
> 클수록 네트워크 효율이 오르지만 지연 시간이 길어짐

## Zookeeper 관련 설정
### Zookeeper 관련 최적화 값
- maxClientCnxns: 주키퍼 최대 연결 수, 기본값 60, 브로커 1개당 20 정도 필요  
- syncLimit: 리더-팔로워 최대 지연 시간, 기본값 10초  
- autopurge.snapRetainCount: 저장 중인 스냅샷 수, 기본값 3  
- autopurge.purgeInterval: 저장된 로그 삭제 주기, 기본값 24시간  

📄 단독 설치 시  
`zookeeper/conf/zoo.cfg`  

OR

📄 카프카 내장 주키퍼 사용 시  
`config/zookeeper.properties`  

```properties
syncLimit=5
maxClientCnxns=200
autopurge.snapRetainCount=3
autopurge.purgeInterval=24
```

# Kafka 데이터의 저장

## Log 저장 방식 최적화
### Segment 저장 관련 설정값

- log.retention.ms: 로그 보관 시간 (기본 7일), 장기 보관 시 별도의 저장장치로 백업 추천
- log.segment.bytes: 세그먼트 크기 설정, 기본값 1GB  
- log.cleanup.policy: 오래된 데이터 삭제(`delete`)할지 또는 압축(`compact`)할지 결정, 기본값은 'delete', 동시에 설정도 가능  
- log.cleaner.enable: 데이터 정리 시 키별 최신 로그만 남길지 여부, 기본값 false

📄 config/server.properties
```properties
# 1. 로그 보관 최적화 (7일 유지)
log.retention.ms=604800000

# 2. 세그먼트 크기 최적화 (1GB)
log.segment.bytes=1073741824

# 3. 불필요한 로그 정리 활성화
log.cleaner.enable=true

# 4. 로그 정리 정책 (삭제 또는 압축)
log.cleanup.policy=delete,compact
```

## Log 저장 방식 최적화
### Segment 압축하기
- 앞서 나왔던 메시지의 압축과는 다름  
- 동일한 key 값의 최신 데이터만 남게 하는 것이 목표  

| offset | key | value |
|--------|------|--------|
| 0 | user123 | 로그인 성공 |
| 1 | user456 | 결제 완료 |
| 2 | user123 | 로그아웃 |
| 3 | user456 | 상품 조회 |
| 4 | user123 | 회원 탈퇴 |

➡ 압축 후
| offset | key | value |
|--------|------|--------|
| 3 | user456 | 상품 조회 |
| 4 | user123 | 회원 탈퇴 |