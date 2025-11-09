from confluent_kafka import Producer

# 1. Kafka 클러스터 설정
conf = {
    'bootstrap.servers': 'localhost:9092'  # Kafka 브로커 주소 (여러 개일 경우 쉼표로 구분)
}

# 2. Producer 인스턴스 생성
producer = Producer(conf)

# 3. 메시지 전송 완료 콜백 함수
def delivery_report(err, msg):
    """
    메시지 전송 후 Kafka 브로커가 응답하면 자동 호출되는 콜백 함수
    - err: 전송 실패 시 오류 정보
    - msg: 성공 시 메시지의 토픽, 파티션 등의 메타정보
    """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [partition: {msg.partition()}]")

# 4. 메시지 전송
for i in range(5):
    message = f"hello kafka {i}"  # 전송할 메시지 생성
    
    producer.produce(
        topic='test-topic2',                  # 전송할 토픽
        value=message.encode('utf-8'),       # 메시지를 UTF-8로 인코딩
        callback=delivery_report             # 전송 완료 후 콜백 함수 호출
    )
    
    # 내부 전송 큐 처리 (콜백 함수가 실행되도록 이벤트 루프를 돌림)
    producer.poll(0)

# 5. 모든 메시지 전송 완료 대기
producer.flush()  # 전송 큐에 남은 메시지를 모두 보낸 후 종료
