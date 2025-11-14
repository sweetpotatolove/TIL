# 실시간 뉴스 분석 및 개인화 대시보드 서비스

## 1. 개요
- 실시간으로 수집되는 뉴스 데이터 기반 서비스 제공 플랫폼
  - 최신 뉴스 분석 및 개인화 피드
  - 키워드 검색 및 요약 기능
  - AI 챗봇 기반 뉴스 Q&A 서비스

- Kafka–Flink–PostgreSQL 기반으로 데이터 파이프라인 구성
- Django REST API와 Vue.js 프론트엔드로 전체 서비스 구성
- 검색은 ElasticSearch, 챗봇은 LLM API(OpenAI 등) 기반 구현

## 2. 목적
- Kafka → Flink → PostgreSQL 파이프라인으로 뉴스 실시간 반영
- ElasticSearch 기반 뉴스 검색
- 뉴스 내용 기반 질의응답, 요약, 트렌드 설명
- 개인화 서비스:	좋아요/조회 로그 기반 추천
- 시각화: 사용자 활동, 관심 카테고리 그래프 제공

## 3. 시스템 아키텍처
```
[뉴스 API or 크롤러]
   ↓
[Kafka Producer]
   ↓
[Flink Consumer] ─ (ETL & Sentiment)
   ↓
[PostgreSQL] ←→ [ElasticSearch Indexer]
   ↓
[Django REST API] ←→ [LLM Chatbot API(OpenAI/Local)]
   ↓
[Vue.js Frontend]
```

## 4. 주요 기능
- 뉴스 서비스

  - 실시간 뉴스 목록/상세/좋아요/조회 기록
  - 카테고리 기반 필터링

- 검색 기능 (ElasticSearch 연동)

  - 제목, 본문, 키워드 기반 뉴스 검색
  - 연관 키워드 추천

- 뉴스 챗봇 기능
  - 사용자의 질문에 대한 뉴스 기반 답변 제공

- 사용자 대시보드

   - 좋아요/조회수 통계, 관심 카테고리 그래프
   - 개인화 추천 뉴스 리스트

## 5. 기술 스택
| 구분     | 기술                       | 역할             |
| ------ | ------------------------ | -------------- |
| 데이터 수집 | Kafka, Flink             | 실시간 뉴스 스트리밍    |
| DB     | PostgreSQL               | 영구 저장소         |
| 검색 엔진  | ElasticSearch            | 뉴스 검색 및 키워드 분석 |
| 백엔드    | Django REST Framework    | API 및 LLM 연동   |
| AI     | OpenAI API / HuggingFace | 뉴스 요약, Q&A 챗봇  |
| 프론트엔드  | Vue.js + Chart.js        | UI 및 시각화       |
| 인증     | JWT                      | 로그인 및 토큰 관리    |

## 6. ERD
![alt text](image.png)