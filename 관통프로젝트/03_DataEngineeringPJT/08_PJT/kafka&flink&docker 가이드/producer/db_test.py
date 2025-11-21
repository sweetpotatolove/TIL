import psycopg2
import os

# PostgreSQL 연결
conn = psycopg2.connect(
    host="localhost",
    dbname="news",
    user="myuser",
    password="my"
)

# 커서 생성 및 쿼리 실행
cur = conn.cursor()
# cur.execute("SELECT * FROM news_article;")
cur.execute("SELECT COUNT(*) FROM news_article;")
rows = cur.fetchall()

# 결과 출력
for row in rows:
    print(row)

# 정리
cur.close()
conn.close()
