# 맞춤형 서비스 데이터 파이프라인 환경 설정 관통 PJT 가이드 (예시)

## 최종 목표
```
[Extract]                   [Transform]             [Load]
Kafka Topic  →  Flink  →  데이터 처리/변환   →  PostgreSQL(DB 저장)
(JSON or RSS) (스트리밍)  (카테고리 분류)    →  Elasticsearch(검색)
                  │        (키워드 추출)      
                  │        (벡터 임베딩)
                  │
                  ↓            
                HDFS  →  Spark  →  리포트 생성  →  HDFS 아카이브
              (임시저장)  (배치)     (pdf)          (장기 보관)
```

> **목차 (원본 README의 목차와 실제 내용의 순서를 모두 반영함)**
>
> 1. PostgreSQL 설치 및 설정
> 2. 필요한 라이브러리 설치
> 3. kafka 세팅 예시

---

## 1. PostgreSQL 설치 및 설정

### 1.1. PostgreSQL 설치 (Linux - Ubuntu)

1. **PostgreSQL 설치**  

```bash
echo "deb http://apt.postgresql.org/pub/repos/apt jammy-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt install -y postgresql-16 postgresql-contrib-16 postgresql-16-pgvector
```

2. **서비스 상태 확인**  

```bash
sudo service postgresql status
```

### 1.2. PostgreSQL 데이터베이스 설정

1. **PostgreSQL 접속**  

```bash
sudo -i -u postgres
psql
```

2. **데이터베이스 생성**  

```sql
CREATE DATABASE news;
```

3. **사용자 생성 및 권한 부여**  

```sql
CREATE USER myuser WITH PASSWORD 'my';
GRANT ALL PRIVILEGES ON DATABASE news TO myuser;
```

4. **데이터베이스 접속 및 테이블 생성**

```sql
\c news
```

```sql
-- pgvector 확장 설치 (최초 1회)
CREATE EXTENSION IF NOT EXISTS vector;

-- news_article 테이블 생성
CREATE TABLE news_article (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    writer VARCHAR(255) NOT NULL,
    write_date TIMESTAMP NOT NULL,
    category VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    url VARCHAR(200) UNIQUE NOT NULL,
    keywords JSON DEFAULT '[]'::json,
    embedding VECTOR(1536) NULL
);
```

5. **권한 부여**

```sql
-- 기존 테이블 및 시퀀스 권한
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO myuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO myuser;

-- 앞으로 생성될 객체의 기본 권한
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO myuser;

-- 스키마 내 생성 권한
GRANT CREATE ON SCHEMA public TO myuser;
```

---

## 2. 필요한 라이브러리 설치

```bash
python3.10 -m venv ~/venvs/data-pjt
source ~/venvs/data-pjt/bin/activate
```

- 해당 환경에 설치
```bash
pip install -r requirements.txt
```
---

## 3. Kafka 실행 예시

### 3.1. Kafka 실행

1. **Zookeeper 실행**  
  ```bash
  $KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties
  ```
2. **Kafka Server 실행**
  ```bash
  $KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties
  ```

### Docker compose 파일로 kafka 실행

```bash
docker compose up
```

### 3.3. Kafka 관련 Python 스크립트 실행

Kafka와 연동되는 파이썬 스크립트를 통해 데이터 파이프라인을 테스트할 수 있습니다.

- **Consumer 실행**  
  Kafka로부터 메시지를 소비하는 스크립트를 실행합니다.

  ```bash
  python consumer/flink_kafka_consumer.py
  ```

- **Producer 실행**  
  RSS 피드 데이터를 Kafka로 전송하는 스크립트를 실행합니다.

  ```bash
  python producer/rss_kafka_producer.py
  ```

---
