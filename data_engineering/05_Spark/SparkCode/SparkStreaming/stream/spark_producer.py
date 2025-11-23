from kafka import KafkaProducer
import json
import time
from datetime import datetime, timedelta
import random

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 기준 시간 (현재 시각 기준 -5분)
base_time = datetime.now() - timedelta(minutes=5)

# 메시지 전송
for i in range(30):
    # 0~4분 사이의 임의 시점 생성 (1분 단위 집계를 위해)
    offset_minutes = random.randint(0, 4)
    offset_seconds = random.randint(0, 59)

    msg_time = base_time + timedelta(minutes=offset_minutes, seconds=offset_seconds)
    
    message = {
        'id': i,
        'message': f'테스트 메시지 {i}',
        'timestamp': msg_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Kafka로 메시지 전송
    producer.send('test-topic', message)
    print(f'전송된 메시지: {message}')
    
    time.sleep(0.5)  # 너무 빠르게 보내지 않도록 살짝 텀 주기

producer.flush()
