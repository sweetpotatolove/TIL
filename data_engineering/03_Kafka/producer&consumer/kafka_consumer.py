from kafka import KafkaConsumer

# KafkaConsumer 생성
consumer = KafkaConsumer(
    'test-topic1',                                 # 구독할 토픽 이름
    bootstrap_servers='localhost:9092',           # Kafka 브로커 주소
    auto_offset_reset='earliest',                 # 처음부터 메시지를 읽음(earliest) / 최신부터는 latest
    enable_auto_commit=True,                      # 자동 오프셋 커밋 (소비한 위치 자동 저장)
    value_deserializer=lambda v: v.decode('utf-8')# 메시지를 UTF-8로 역직렬화(문자열 변환)
)

print("Listening for messages...")

# 메시지 수신 루프
for message in consumer:
    print(f"Received: {message.value}")           # 수신한 메시지 출력
