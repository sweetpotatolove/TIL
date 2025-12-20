# producer/rss_kafka_producer.py
import time
import json
import feedparser
from kafka import KafkaProducer
import requests
from bs4 import BeautifulSoup

# RSS 피드 URL (예: Khan 뉴스 RSS)
RSS_FEED_URL = "https://www.khan.co.kr/rss/rssdata/total_news.xml"
# Kafka 브로커 주소 (실제 환경에 맞게 수정)
# WSL에서 클라이언트로 접속하는 것이므로, 29092 사용해야함
# 로컬에서 쓸거면 9092
KAFKA_BROKER = "localhost:29092"
# 전송할 Kafka 토픽
TOPIC = "news"

# Kafka Producer 생성 (value는 JSON 직렬화)
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch_rss_feed():
    """
    RSS 피드를 파싱하여 각 뉴스 항목을 제너레이터로 반환합니다.
    """
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        # 각 항목의 필요한 정보를 추출
        news_item = {
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "published": entry.updated,
            "author": entry.author
        }
        yield news_item

def crawl_article(url: str) -> str:
    """특정 기사 URL을 크롤링해 기사 본문을 반환합니다."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # 예시: 본문 확인
        content_tag = soup.find_all("p", class_="content_text text-l")
        content_text = "\n\n".join([tag.text.strip() for tag in content_tag])

        return content_text

    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return ""

# 단순화한 RSS 피드 수집
def main():
    # 중복 전송 방지를 위해 처리한 링크를 저장하는 집합
    seen_links = set() # 메모리 쓰면서 url 계속 업데이트 되므로 규모가 커지면 사용하기 힘듦
    while True:
        try:
            for news_item in fetch_rss_feed():
                # 뉴스 링크를 기준으로 중복 체크
                if news_item["link"] not in seen_links:
                    content = crawl_article(news_item["link"])
                    news_item["content"] = content
                    seen_links.add(news_item["link"])
                    producer.send(TOPIC, news_item)     # 토픽에 메시지가 들어가기만 하는 상태. 적재XX
                    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Sent: {news_item['title']}")
            # 60초 대기 후 다시 피드 확인
            time.sleep(60)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

if __name__ == "__main__":
    main()
