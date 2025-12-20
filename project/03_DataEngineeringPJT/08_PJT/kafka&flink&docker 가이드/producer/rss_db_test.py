import time
import requests
import feedparser
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

RSS_FEED_URL = "https://www.khan.co.kr/rss/rssdata/total_news.xml"

# PostgreSQL 연결 
def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="news",
        user="myuser",
        password="my"
    )

# DB INSERT
def save_article_to_db(article):

    query = """
        INSERT INTO news_article 
            (title, writer, write_date, category, content, url)
        VALUES 
            (%(title)s, %(writer)s, %(write_date)s, %(category)s, %(content)s, %(url)s)
        ON CONFLICT (url) DO NOTHING;
    """

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(query, article)
        conn.commit()
        cur.close()
        conn.close()

        print(f"[DB 저장 완료] {article['title']}")
    except Exception as e:
        print(f"[DB 저장 오류] {e}")

def main():
    seen_links = set()

    while True:
        print("\n[RSS 확인 중...]")
        feed = feedparser.parse(RSS_FEED_URL)

        for entry in feed.entries:
            url = entry.link

            if url in seen_links:
                continue
            seen_links.add(url)

            title = entry.title
            writer = getattr(entry, "author", "Unknown")
            category = entry.get("category", "Unknown")
            description = getattr(entry, "description", "")
            
            # 날짜 파싱
            if hasattr(entry, "updated_parsed") and entry.updated_parsed:
                write_date = datetime(*entry.updated_parsed[:6])
            elif hasattr(entry, "published_parsed") and entry.published_parsed:
                write_date = datetime(*entry.published_parsed[:6])
            else:
                write_date = datetime.now()

            # 출력
            print(f"\n[새 기사] {title}")
            print(f"[링크] {url}")
            print(f"[기자] {writer}")
            print(f"[카테고리] {category}")
            print(f"[작성일] {write_date}")
            print(f"\n[내용]\n{description}\n")

            # DB 저장용 데이터
            article = {
                "title": title,
                "writer": writer,
                "write_date": write_date,
                "category": category,
                "content": description,
                "url": url
            }

            save_article_to_db(article)

        print(f"\n[총 수집 기사 수] {len(seen_links)}")
        print("[60초 대기 후 재확인]")
        time.sleep(60)


if __name__ == "__main__":
    main()
