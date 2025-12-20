import time
import feedparser
from datetime import datetime

# RSS 피드 주소: 경향신문 전체 뉴스 RSS
RSS_FEED_URL = "https://www.khan.co.kr/rss/rssdata/total_news.xml"

def main():
    # 이미 수집한 기사 링크(URL)를 저장하는 집합
    #   → 중복 기사 출력 / DB 저장을 방지하는 용도
    seen_links = set()

    while True:
        print("\n[RSS 확인 중...]")

        # RSS 데이터 파싱
        # feed.entries 안에 기사들이 리스트로 들어 있음
        feed = feedparser.parse(RSS_FEED_URL)

        # RSS에 포함된 기사 하나씩 순회
        for entry in feed.entries:
            url = entry.link  # 기사 고유 URL

            # 이미 등록된 기사면 건너뛰기
            if url in seen_links:
                continue

            # 새 기사라면 기록
            seen_links.add(url)

            # 기사 제목
            title = entry.title

            # 기자 이름이 있을 수도 있고 없을 수도 있음 → 없으면 "Unknown"
            writer = getattr(entry, "author", "Unknown")

            # 카테고리도 없을 수 있으므로 기본값 "Unknown"
            category = entry.get("category", "Unknown")

            # 기사 내용(요약 문구)
            description = getattr(entry, "description", "")

            # 🕒 날짜 파싱
            # updated_parsed → 수정일 / published_parsed → 발행일
            # 둘 다 없다면 현재 시간을 사용
            if hasattr(entry, "updated_parsed") and entry.updated_parsed:
                write_date = datetime(*entry.updated_parsed[:6])  # 튜플 → datetime 변환
            elif hasattr(entry, "published_parsed") and entry.published_parsed:
                write_date = datetime(*entry.published_parsed[:6])
            else:
                write_date = datetime.now()

            # 새 기사 정보 출력
            print(f"\n[새 기사] {title}")
            print(f"[링크] {url}")
            print(f"[기자] {writer}")
            print(f"[카테고리] {category}")
            print(f"[작성일] {write_date}")
            print(f"\n[내용]\n{description}\n")

        # 총 몇 개 기사 수집했는지 누적 출력
        print(f"[총 수집 기사 수] {len(seen_links)}")

        # 1분마다 RSS 새로 확인
        print("[60초 대기 후 재확인]\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
