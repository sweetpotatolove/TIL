from kafka import KafkaProducer

# KafkaProducer 생성
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',          # Kafka 브로커 주소 (기본 포트: 9092)
    value_serializer=lambda v: v.encode('utf-8') # 메시지를 UTF-8로 직렬화(바이트 변환)
)

# 5개의 메시지를 순차적으로 전송
for i in range(5):
    message = f"hello kafka {i}"                 # 전송할 메시지
    producer.send('test-topic1', message)         # 'test-topic' 토픽으로 메시지 전송
    print(f"Sent: {message}")                    # 전송 로그 출력

# 전송되지 않은 메시지를 모두 전송 후 리소스 정리
producer.flush()                                 # 버퍼에 남은 메시지를 즉시 전송
producer.close()                                 # Producer 종료
