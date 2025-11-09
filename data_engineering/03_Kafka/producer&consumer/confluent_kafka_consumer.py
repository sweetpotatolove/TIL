from confluent_kafka import Consumer

# 1. Kafka Consumer 설정
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka 브로커 주소
    'group.id': 'my-group',                 # Consumer Group ID (같은 그룹은 파티션 분담 소비)
    'auto.offset.reset': 'earliest',        # 처음부터 읽기(earliest) / 최신부터는 latest
    'enable.auto.commit': True              # 자동 오프셋 커밋 여부 (True: 자동 저장)
}

# 2. Consumer 인스턴스 생성
consumer = Consumer(conf)

# 3. 구독할 토픽 지정
consumer.subscribe(['test-topic2'])

try:
    while True:
        # poll()은 브로커로부터 메시지를 가져오는 함수
        # (1.0초 동안 기다린 후 메시지가 없으면 None 반환)
        msg = consumer.poll(1.0)

        if msg is None:
            continue  # 메시지가 없으면 루프 계속

        if msg.error():
            print("Consumer error:", msg.error())  # 에러 발생 시 출력
            continue

        # 수신한 메시지 출력 (바이트 → 문자열 디코딩 필요)
        print(f"Received: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    # 종료 시 커넥션 정리
    consumer.close()
