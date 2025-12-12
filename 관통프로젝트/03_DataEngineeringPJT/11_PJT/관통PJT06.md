# Elasticsearch 기반의 검색 구현

# 관통 프로젝트 안내

## 프로젝트 개요
- Elasticsearch를 이용하여 PostgreSQL에 저장된 컨텐츠를 검색하고, 검색된 결과를 대시보드로 시각화하는 것이 최종 목표입니다.
- Django REST Framework(DRF)를 통해 검색 API를 제공하고, Vue.js에서 검색 UI를 구현하여 사용자 편의성을 높입니다.
- 실시간 혹은 일정 주기로 컨텐츠 데이터를 동기화하고, 빠르고 정확한 검색 환경을 제공합니다.
- 또한, Kibana를 활용하여 주요 지표(검색 트렌드, 컨텐츠 카테고리 분포 등)를 시각적으로 확인할 수 있는 대시보드를 제작할 수 있습니다.

## 목표
- Elasticsearch와 PostgreSQL을 연동하며 데이터에 대한 검색 기능을 구축할 수 있다.
- Django REST Framework(DRF)로 검색 API를 설계 및 구현할 수 있다.
- Vue.js로 웹 검색 UI를 구성하고, 사용자 인터페이스를 직관적으로 설계할 수 있다.
- Kibana 대시보드를 활용하여 다양한 관점에서 데이터 시각화와 모니터링을 수행할 수 있다.

## 준비사항
- 사용 데이터
  - PostgreSQL에 저장된 뉴스 컨텐츠 데이터 (컨텐츠 제목, 작성자, 작성일, 내용, URL, 키워드 등)
  - Elasticsearch 색인(index)으로 사용될 전처리 과정의 데이터
- 개발언어/프로그램
  - Python (Django REST Framework, Airflow DAG, 데이터 동기화 스크립트 등)
  - Vue.js (검색 UI 구현)
  - Elasticsearch & Kibana (검색 엔진 및 시각화 대시보드)
  - PostgreSQL (컨텐츠 저장 및 관리)
  - Docker (개발 환경 및 배포 환경 구성 시 활용)

## 구현 방법

### 1) Elasticsearch 세팅
- Elasticsearch 설치 및 구성 (Docker Compose 또는 직접 설치)
- 뉴스 컨텐츠 데이터를 저장할 인덱스(news) 생성
- 검색 성능 및 매핑 설정(분석기, 토크나이저 설정 등)

### 2) DRF 검색 기능 추가
- Django REST Framework로 검색 API 엔드포인트 구현 (GET /news/search/)
- 요청 파라미터를 받아 Elasticsearch에서 컨텐츠 검색
- 검색 결과를 JSON 형태로 반환

### 3) Vue.js 검색 UI 추가
- Vue.js 프로젝트 생성 후, 검색 창과 결과 목록 UI 개발
- DRF API 연동하여 사용자 검색 요청 처리
- 결과 목록 정렬, 필터 등 추가 기능 고려

### 4) DB-Elasticsearch 동기화
- PostgreSQL과 Elasticsearch 간의 데이터 동기화 수행
  - RDB에 저장함과 동시에 별도로 Elasticsearch에 따로 적재 (트랜잭션이 성공한 경우만 Elasticsearch로 보냄)
  - 배치로 동기화: Airflow나 Logstash 기반으로 Cronjob 형태로 RDB에서 수정된 데이터를 읽어서 Elasticsearch에 일괄 동기화 (postgresql에 추가적인 컬럼 필요 – update 시간)

# 데이터 마이그레이션
- Elasticsearch는 비정형 데이터를 효율적으로 검색하고 분석하기 위한 검색 엔진
- 하지만 많은 기존 시스템에서는 관계형 데이터베이스(RDB, Relational Database)를 사용
- 둘을 혼합하여 사용하는 경우도 많음
- RDB는 정규화(Normalization) 된 구조를 가지고 있음
- Elasticsearch는 비정규화(Denormalization)된 문서 기반 데이터 저장 방식
- 이를 위해 Logstash, Airflow 등을 사용할 수 있음

## 마이그레이션을 위한 주요 테이블과 관계

- 어떤 테이블을 인덱스로 만들 것인가?
- 관계형 데이터(RDB의 JOIN)가 Elasticsearch에서도 필요한가?
- 중첩된 데이터를 사용할 것인가(Nested Type), 또는 평탄화(Flat)할 것인가?

### RDB ↔ Elasticsearch 필드 타입 매핑 표

| RDB 필드 타입 | Elasticsearch 필드 타입 |
|--------------|--------------------------|
| INT, BIGINT | long, integer |
| VARCHAR, TEXT | text, keyword |
| DATE, TIMESTAMP | date |
| BOOLEAN | boolean |
| DECIMAL, FLOAT | double, float |

## Elasticsearch 마이그레이션
- 기존에 RDB 형태가 아래와 같다고 가정

```sql
-- testdb 데이터베이스에 연결
\c testdb;

-- ssafyuser에게 권한 부여
GRANT ALL PRIVILEGES ON DATABASE testdb TO ssafyuser;

-- 뉴스 기사 테이블 생성
CREATE TABLE IF NOT EXISTS news_article (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    writer VARCHAR(255) NOT NULL,
    write_date TIMESTAMP NOT NULL,
    category VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    url VARCHAR(200) UNIQUE NOT NULL
);
```

```sql
-- 샘플 뉴스 데이터 삽입 (여러 개 추가 가능)
INSERT INTO news_article (title, writer, write_date, category, content, url) VALUES
('Samsung Launches New Galaxy Phone', 'Jane Doe', '2025-03-10 09:28:40', 'Technology',
 'Samsung has launched its latest Galaxy phone with cutting-edge features including...',
 'https://example.com/samsung-galaxy-launch'),
('Apple Reports Record Earnings', 'John Smith', '2025-03-12 14:15:20', 'Business',
 'Apple announced record earnings for the last quarter, with significant growth in iPhone sales...',
 'https://example.com/apple-earnings-record'),
('Scientists Discover New Species in Amazon Rainforest', 'Alice Johnson', '2025-03-15 18:45:35', 'Science',
 'A team of scientists recently discovered a new species of frog in the Amazon rainforest, which could...',
 'https://example.com/amazon-rainforest-discovery'),
('Stock Market Hits All-Time High', 'Michael Lee', '2025-03-10 13:50:55', 'Finance',
 'The stock market reached an all-time high, driven by gains in major technology stocks...',
 'https://example.com/stock-market-all-time-high'),
('New Policy Aims to Address Climate Change', 'Olivia Brown', '2025-03-28 10:18:40', 'Politics',
 'The new policy focuses on reducing carbon emissions and promoting renewable energy sources...',
 'https://example.com/climate-change-policy');
```

## 데이터 추출 및 변환 (ETL)
- Logstash 활용
  - Logstash 활용 시 conf 파일을 작성해야 함
  - 기본 구조

```conf
input {
  # 데이터 소스 설정
}

filter {
  # 데이터 변환 및 가공
}

output {
  # 데이터 저장 위치
}
```

## 데이터 추출 및 변환 (ETL)
- Logstash 활용
  - Input
  - JDBC, File, Kafka 등 다양한 입력 소스를 설정

```conf
input {
  jdbc {
    jdbc_driver_library => "/usr/share/logstash/ingest_data/postgresql.jar"
    jdbc_driver_class => "org.postgresql.Driver"
    jdbc_connection_string => "jdbc:postgresql://postgres:5432/testdb"
    jdbc_user => "ssafyuser"
    jdbc_password => "ssafy"

    schedule => "* * * * *"   # 매분 실행

    last_run_metadata_path => "/usr/share/logstash/.logstash_jdbc_last_run"

    statement => "
      SELECT *
      FROM news_article
      WHERE write_date > :sql_last_value
      ORDER BY write_date ASC
    "
  }
}
```

## 데이터 추출 및 변환 (ETL)
- Logstash 활용
  - Input

| 설정 옵션               | 설명                                           |
|-------------------------|------------------------------------------------|
| jdbc_driver_library     | PostgreSQL JDBC 드라이버의 위치 지정          |
| jdbc_driver_class       | 사용할 JDBC 드라이버 클래스                    |
| jdbc_connection_string  | PostgreSQL 데이터베이스의 연결 정보           |
| jdbc_user               | PostgreSQL 사용자명                           |
| jdbc_password           | PostgreSQL 비밀번호                           |
| schedule                | * * * * * → CRON 표현식 (1분마다 실행)        |
| statement               | SQL 쿼리 실행                                  |

- Logstash 활용
  - Filter
  - 가져온 데이터를 가공하는 단계
  - order_id 필드를 복사 (Elasticsearch에서 document_id 필드로 사용)
  - @timestamp와 @version 필드를 삭제하여 Elasticsearch에 저장되지 않도록 처리

```conf
filter {
  mutate {
    rename => { "id" => "document_id" }
  }
  mutate { remove_field => ["@timestamp", "@version"] }
}

output {
  elasticsearch {
    hosts => ["http://es01:9200"]
    index => "news_articles"
    document_id => "%{document_id}"
  }
  stdout { codec => rubydebug }
}
```

- Logstash 활용
  - Output
  - 처리된 데이터를 Elasticsearch, 파일, 콘솔 등에 저장하는 단계
  - PostgreSQL에서 가져온 데이터를 news_articles와 같은 구성하고자 하는 인덱스에 저장
  - document_id를 id로 설정하여 업데이트

```conf
filter {
  mutate {
    rename => { "id" => "document_id" }
  }
  mutate { remove_field => ["@timestamp", "@version"] }
}

output {
  elasticsearch {
    hosts => ["http://es01:9200"]
    index => "news_articles"
    document_id => "%{document_id}"
  }
  stdout { codec => rubydebug }
}
```

## 완전한 실시간 동기화가 필요한 경우  
- 데이터가 지속적으로 변경될 경우, 실시간 동기화(Real-Time Sync)가 필요할 수 있음  
- 방법 1: Change Data Capture (CDC)  
  - MySQL의 Binlog, PostgreSQL의 Logical Replication을 활용  
  - Debezium 같은 CDC 도구 사용  
- 방법 2(대안으로써의 방법): Periodic Batch Update  
  - 일정 주기마다 배치 작업을 수행하는 방식 (예: Airflow, Logstash Cron Job 활용)  

## 구현 방법  
5) Kibana 시각화 대시보드  
  - Kibana에 Elasticsearch 인덱스를 연결  
  - 콘텐츠 카테고리, 키워드, 작성일 등을 기반으로 한 다양한 시각화 차트(파이 차트, 바 차트, 라인 차트 등) 구성  
  - 실시간 분석 모니터링 페이지 구성  

## 관통 프로젝트 가이드  
1) PJT 내용  
  - 데이터 저장(컨텐츠 DB 구축)  
    - 컨텐츠 데이터를 테이블 단위로 저장하고 관리  
  - Elasticsearch 색인  
    - Kafka Consumer에서 데이터를 DB에 저장하는 동시에 Elasticsearch 인덱스도 함께 갱신  
  - 검색 및 UI  
    - DRF를 통해 검색 API를 구현하고, Vue.js로 검색 화면을 구성해 사용자 편의성 제공  
  - 시각화  
    - Kibana를 통해 검색 트렌드, 인기 컨텐츠, 카테고리 분포 등을 대시보드로 시각화  
  - 데이터 동기화  
    - RDB에 저장함과 동시에 별도로 Elasticsearch에 따로 적재 (트랜잭션이 성공한 경우만 Elasticsearch로 보냄)  
    - 배치로 동기화 – Airflow나 Logstash 기반으로 Cronjob 형태로 RDB에서 수정된 데이터를 읽어서 Elasticsearch에 일괄 동기화 (postgresql에 추가적인 컬럼 필요 – update 시간)  

## 관통 프로젝트 가이드

## 관통 프로젝트 가이드

## 요구사항
- Elasticsearch 세팅 후 PostgreSQL과 연동하여 검색 서비스를 구축

- 기본 기능
  - 데이터 검색 및 시각화
    - Elasticsearch 인덱스 생성 및 매핑 설정
    - PostgreSQL DB에 저장된 콘텐츠 데이터 색인
    - DRF API를 통해 검색 기능 구현 (키워드, 날짜, 카테고리 등)

## 요구사항
- 요청 조건
  - RDB에 저장함과 동시에 별도로 Elasticsearch에 따로 적재 (트랜잭션이 성공한 경우에만 Elasticsearch로 보냄)
  - 배치로 동기화  
    - Airflow나 Logstash 기반 Cronjob 형태로 RDB에서 수정된 데이터를 읽어 Elasticsearch에 일괄 동기화 (PostgreSQL에 추가적인 컬럼 필요 — update 시간)
  - 콘텐츠 검색 UI를 Vue.js로 구현
- 결과
  - DB와 Elasticsearch가 연동된 색인 및 검색 기능 시연 가능
  - Vue.js 검색 화면에서 제목 검색 및 결과 리스트 확인 가능

## 요구사항 (고급 기능)
- Kibana 고급 분석 또는 추가 UI 확장 (예: 연관 키워드 추천, 자동완성 기능 등)
- 요청 조건
  - 콘텐츠 내 키워드를 기반으로 자동완성 기능 추가
  - 검색 결과 기반 연관 키워드 추천 API 구현 (Elasticsearch ngram 분석기, suggest 기능 활용)
  - Kibana로 인덱스 연결 및 간단한 대시보드 작성
  - Kibana 대시보드를 활용한 시각화 및 연관 키워드 관계(네트워크 그래프 등) 시각화
- 결과
  - 사용자 입력에 따른 실시간 자동완성 기능 제공
  - 검색 결과를 Kibana에서 다양한 차트(바 차트, 파이 차트 등)로 확인 가능
  - Kibana의 시각화 및 연관 키워드 그래프 등을 통해 분석 범위 확대

## 산출물
- GitLab 연계
  - GitLab에 올라온 de-project 코드 기반의 레포지토리 지속적 커밋
  - 이후 PJT도 해당 레포지토리에 이어 나가면서 개발