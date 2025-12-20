import psycopg2
import os

# PostgreSQL 연결
conn = psycopg2.connect(
    host="localhost",
    dbname="news",
    user="myuser",
    password="my"
)

# SQL 실행을 위한 커서(cursor) 생성
# 커서는 DB에서 SQL 문장을 실행하고, 결과를 가져오는 데 필요한 객체
cur = conn.cursor()

# 실행할 SQL 쿼리 작성
# 아래는 news_article 테이블의 전체 행 수를 확인하는 쿼리
# cur.execute("SELECT * FROM news_article;")        # 전체 데이터 조회
cur.execute("SELECT COUNT(*) FROM news_article;")   # 레코드 수 조회

# 쿼리 결과 가져오기
# fetchall() → 모든 결과를 리스트 형태로 반환
# COUNT(*) 사용 시 결과는 [(개수,)] 형태의 리스트로 반환됨
rows = cur.fetchall()

# 결과 출력
# row는 튜플 형태이므로 그대로 출력하면 (123,) 같은 형태
for row in rows:
    print(row)

# 사용한 커서와 연결을 닫아 리소스 정리
cur.close()
conn.close()
