from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Kafka 프로듀서 설정
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 샘플 데이터 속성
user_ids = [f"user_{i}" for i in range(1, 100)]
item_ids = [f"item_{i}" for i in range(1, 200)]
categories = ["electronics", "books", "clothing", "home", "sports"]
behaviors = ["click", "view", "add_to_cart", "purchase"]

# 데이터 생성 및 전송
for _ in range(1000):  # 1000개의 이벤트 생성
    event = {
        "user_id": random.choice(user_ids),
        "item_id": random.choice(item_ids),
        "category": random.choice(categories),
        "behavior": random.choice(behaviors),
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    }
    
    producer.send('user_behaviors', event)
    print(f"Sent: {event}")
    time.sleep(0.1)  # 0.1초 간격으로 이벤트 전송

producer.flush()
print("Data generation complete!")
