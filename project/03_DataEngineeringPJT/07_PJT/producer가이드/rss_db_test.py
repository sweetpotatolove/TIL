import time
import requests
import feedparser
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

RSS_FEED_URL = "https://www.khan.co.kr/rss/rssdata/total_news.xml"

# PostgreSQL 연결 
#   이 함수를 호출할 때마다 새로운 DB 연결 객체를 반환한다.
#   → 매번 INSERT 후 연결을 닫기 때문에 안정적
def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="news",
        user="myuser",
        password="my"
    )

# DB INSERT
#   - article 딕셔너리를 받아 DB에 저장
#   - url 컬럼에 UNIQUE 제약이 걸려 있다고 가정
#   - ON CONFLICT (url) DO NOTHING → 중복 저장 방지
def save_article_to_db(article):

    query = """
        INSERT INTO news_article 
            (title, writer, write_date, category, content, url)
        VALUES 
            (%(title)s, %(writer)s, %(write_date)s, %(category)s, %(content)s, %(url)s)
        ON CONFLICT (url) DO NOTHING;
    """

    try:
        # DB 연결 및 커서 생성
        conn = get_connection()
        cur = conn.cursor()

        # SQL 실행
        cur.execute(query, article)

        # 변경사항 저장
        conn.commit()

        # 리소스 정리
        cur.close()
        conn.close()

        print(f"[DB 저장 완료] {article['title']}")
    except Exception as e:
        print(f"[DB 저장 오류] {e}")

# 전체 뉴스 수집 메인 로직
def main():
    # 이미 처리한 기사 URL을 저장하는 set
    # RSS 주기는 빠르고 최근 데이터가 반복될 수 있기 때문에 중복 필터링 필요
    seen_links = set()

    while True:
        print("\n[RSS 확인 중...]")

        # RSS 피드 파싱
        feed = feedparser.parse(RSS_FEED_URL)

        # RSS에 포함된 각 기사 처리
        for entry in feed.entries:
            url = entry.link

            # 중복 기사면 건너뛰기
            if url in seen_links:
                continue
            seen_links.add(url)

            # 기본 메타데이터 파싱
            title = entry.title
            writer = getattr(entry, "author", "Unknown")
            category = entry.get("category", "Unknown")
            description = getattr(entry, "description", "")
            
            # 날짜 파싱 (updated → published → 현재시간 순)
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

            # DB 저장용 데이터 구조 생성
            article = {
                "title": title,
                "writer": writer,
                "write_date": write_date,
                "category": category,
                "content": description,
                "url": url
            }

            # DB에 저장
            save_article_to_db(article)

        print(f"\n[총 수집 기사 수] {len(seen_links)}")
        print("[60초 대기 후 재확인]")
        time.sleep(60)


if __name__ == "__main__":
    main()
