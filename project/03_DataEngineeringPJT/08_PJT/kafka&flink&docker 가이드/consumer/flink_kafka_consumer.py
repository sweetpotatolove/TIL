# flink_kafka_consumer.py

import json
import os
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.datastream.functions import MapFunction
from pyflink.common import Configuration

import psycopg2
from dotenv import load_dotenv

from preprocessing import transform_classify_category, transform_extract_keywords, transform_to_embedding

# .env 파일에 필요한 설정이 있다면 로드합니다.
load_dotenv()

class NewsArticle(BaseModel):
    """뉴스 기사 데이터를 위한 Pydantic 모델"""
    title: str = Field(description="기사 제목")
    link: str = Field(description="기사 URL")
    published: str = Field(description="발행일")
    author: Optional[str] = Field(default=None, description="기자 이름")
    content: Optional[str] = Field(default=None, description="기사 본문")


def process_message(json_str: str) -> NewsArticle:
    """
    JSON 문자열을 파싱하여 NewsArticle 모델로 변환합니다.
    """
    try:
        data = json.loads(json_str)
        return NewsArticle(**data)
    except Exception as e:
        print(f"메시지 파싱 오류: {e}")
        # 오류 발생 시 기본값으로 빈 기사 반환
        return NewsArticle(
            title="오류 발생",
            link="",
            published="",
            author="",
            content=""
        )

class DBInsertionMapFunction(MapFunction):
    """
    DB에 뉴스 기사를 저장하는 함수.
    """
    def __init__(self):
        # lazy initialization 플래그
        self._initialized = False

    def _initialize(self):
        """
        DB 연결을 초기화합니다.
        이 메서드는 워커에서 최초 호출 시 한 번 실행됩니다.
        """
        # PostgreSQL DB 연결
        self._db_conn = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="news",              # 데이터베이스 이름
            user=os.getenv("DB_USERNAME"),            # 사용자명
            password=os.getenv("DB_PASSWORD")     # 비밀번호
        )
        self._db_conn.autocommit = True

        self._initialized = True

    def map(self, article: NewsArticle) -> NewsArticle:
        if not self._initialized:
            self._initialize()

        writer = article.author if article.author else "Unknown"
        try:
            write_date = datetime.fromisoformat(article.published)
        except Exception as e:
            write_date = datetime.now()

        content = article.content

        try:
            category = transform_classify_category(content)
        except Exception as e:
            print("Category transformation error:", e)
            category = "미분류"

        try:
            keywords = transform_extract_keywords(content)
        except Exception as e:
            print("Keywords transformation error:", e)
            keywords = []

        try:
            embedding = transform_to_embedding(content)
            embedding_str = json.dumps(embedding)
        except Exception as e:
            print("Embedding transformation error:", e)
            embedding_str = json.dumps([])

        # PostgreSQL에 기사 삽입
        cursor = self._db_conn.cursor()
        db_id = None
        try:
            cursor.execute("""
                INSERT INTO news_article (title, writer, write_date, category, content, url, keywords, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
                RETURNING id;
            """, (
                article.title,
                writer,
                write_date,
                category,
                content,
                article.link,
                json.dumps(keywords, ensure_ascii=False),
                embedding_str
            ))
            result = cursor.fetchone()
            db_id = result[0] if result else None
            print(f"Successfully saved article to Postgresql, id: {db_id}")
        except Exception as e:
            print("DB insertion error:", e)
        finally:
            cursor.close()


        return article  # 체인 연산을 위해 반환


def main():
    # Flink 스트리밍 환경 생성

    kafka_jar_path = os.path.abspath("flink-sql-connector-kafka-3.3.0-1.19.jar")
    config = Configuration()
    config.set_string("pipeline.jars", f"file://{kafka_jar_path}")
    env = StreamExecutionEnvironment.get_execution_environment(configuration=config)
    env.set_parallelism(1)

    # Kafka consumer properties 설정
    kafka_props = {
        'bootstrap.servers': 'localhost:29092',
        'group.id': 'flink_consumer_group'
    }

    # Kafka Consumer 생성 (토픽: "news")
    kafka_consumer = FlinkKafkaConsumer(
        topics="news",
        deserialization_schema=SimpleStringSchema(),  # 문자열 메시지 수신
        properties=kafka_props
    )

    # Kafka에서 메시지 읽어오기
    stream = env.add_source(kafka_consumer)

    # 메시지를 NewsArticle 모델로 변환
    processed_stream = stream.map(process_message)

    # DB 삽입 로직을 MapFunction으로 실행
    processed_stream = processed_stream.map(DBInsertionMapFunction())

    processed_stream.print()

    print("consumer is running...")
    # Flink Job 실행
    env.execute("Flink Kafka Consumer Job")


if __name__ == "__main__":
    main()
