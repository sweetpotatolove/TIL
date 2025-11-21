import time
import feedparser
from datetime import datetime

RSS_FEED_URL = "https://www.khan.co.kr/rss/rssdata/total_news.xml"

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

        print(f"[총 수집 기사 수] {len(seen_links)}")
        print("[60초 대기 후 재확인]\n")
        time.sleep(60)

if __name__ == "__main__":
    main()