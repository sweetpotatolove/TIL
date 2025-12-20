## 1. 기존의 검색 시스템

기존의 검색 시스템은 대부분 **키워드 일치 여부**를 기준으로 작동합니다.  
예를 들어, 사용자가 "환경"이라는 단어를 검색하면:

- `"환경 보호는 중요하다"` → O
- `"기후 변화에 대응해야 한다"` → X  
- `"지속 가능한 에너지 정책"` → X

즉, 의미가 매우 유사하더라도 **단어가 정확히 들어간 문장만 검색**되거나 동의어 사전을 구축해야 하는 상황이 생깁니다.  
하지만 이 세 문장은 **의미상 모두 비슷한 주제**입니다.

---

## 2. 임베딩(Embedding)이란?

키워드 기반 검색에는 한계가 있기 때문에,
우리는 문장의 의미 자체를 수치적으로 표현할 수 있는 '임베딩' 기법을 활용합니다.
**임베딩은 문장의 의미를 숫자로 표현한 것**입니다.  
각 문장은 OpenAI Embedding 같은 모델을 통해 **고차원 벡터**로 바뀝니다.

예시:

| 문장 | 임베딩 벡터 (예시 - 5차원) |
|------|----------------------------|
| 환경 보호는 중요하다 | [0.12, -0.44, 0.88, 0.01, 0.03] |
| 탄소 중립이 필요하다 | [0.15, -0.40, 0.85, 0.02, 0.04] |
| 오늘 뭐 먹지? | [0.65, 0.12, -0.33, 0.90, -0.55] |

→ 앞의 두 문장은 **유사한 방향의 벡터**  
→ 세 번째 문장은 **완전히 다른 주제를 나타냄**

---

## 3. 벡터 서치(Vector Search)란?

이제 문장을 벡터로 표현했으니, 수천 개의 문장 중에서 어떤 벡터가 가장 유사한지를 파악해야 합니다.
이때 사용하는 것이 바로 벡터 서치입니다.
벡터 서치는 **벡터 간의 거리를 기준으로 가장 가까운(유사한) 벡터를 검색**하는 방식입니다.

- "입력 문장"을 임베딩 벡터로 변환
- 데이터베이스에 저장된 수천 개의 벡터와 비교
- **가장 유사한 벡터들을 순서대로 반환**

이때 **코사인 유사도**, **유클리디안 거리**, **내적(Dot Product)** 등이 사용됩니다.  
우리는 PostgreSQL의 `pgvector`를 통해 이 유사도 계산을 SQL 수준에서 바로 처리할 수 있습니다.

---

## 4. 키워드 검색 vs 벡터 검색 비교

| 항목 | 키워드 기반 검색 | 벡터(의미 기반) 검색 |
|------|------------------|-----------------------|
| 기준 | 단어 포함 여부 | 문장의 의미 |
| 예: `"환경"` 입력 | `"환경"` 들어간 문장만 반환 | `"기후"`, `"탄소"`, `"지속 가능"`도 포함 |
| 장점 | 빠르고 단순 | 의미적 다양성 확보 |
| 단점 | 의미를 해석하지 못함 | 연산량이 많고 인덱싱 필요 |
| 활용 예 | 문서 검색, 간단한 키워드 기반 필터링 | 뉴스 추천, AI 검색, Q&A 매칭 |

---

## 5. 활용 사례

- **뉴스 추천**: "환경 관련 기사 좋아요" → `"탄소세 도입"` 기사도 추천
- **QA 챗봇**: 질문 `"연차 이월 규정은?"` → `"연차 소멸 시점"`과도 연결됨

---

## 6. 정리

- **임베딩**은 문장의 **'의미'를 수치화**한 벡터
- **벡터 서치**는 이 의미 벡터 간 **유사도를 계산해 유연한 검색/추천** 가능
- 기존 키워드 방식보다 **의미 기반 탐색이 가능한 것이 가장 큰 차이점**

---


## 7. PostgreSQL `pgvector` + 코사인 유사도 검색 예시 코드

### 테이블 생성

```sql
CREATE EXTENSION IF NOT EXISTS vector; -- 이미 구성되어있으면 생략

CREATE TABLE articles (
  id SERIAL PRIMARY KEY,
  title TEXT,
  embedding VECTOR(3) -- 3차원 벡터 만들겠다
);
```

### 데이터 삽입

```sql
INSERT INTO articles (title, embedding) VALUES
('환경 보호의 중요성', '[0.1, 0.9, 0.2]'),
('패션 트렌드 2025', '[0.7, 0.1, 0.3]'),
('기후 변화와 정책', '[0.2, 0.8, 0.25]');
```

### 유사도 검색 (코사인 유사도 기준)

```sql
SELECT id, title, embedding
FROM articles
ORDER BY embedding <=> '[0.15, 0.85, 0.2]'  -- 입력 벡터와 가장 가까운 문서 검색
LIMIT 2;
```

- `<=>`는 **코사인 거리 연산자**입니다 (작을수록 유사함).
- `[0.15, 0.85, 0.2]`는 예를 들어 사용자의 선호도를 평균낸 벡터라고 가정합니다.

| 연산자   | 의미                 |
| ----- | ------------------ |
| `<->` | 유클리디안 거리 (작을수록 유사) |
| `<=>` | 코사인 거리 (작을수록 유사)   |
| `<#>` | 내적 (값이 클수록 유사)     |

- 참고: https://github.com/pgvector/pgvector
---

### 인덱스 생성 (데이터량이 많을 때 성능 향상용)

```sql
CREATE INDEX ON articles USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
```

- 벡터가 많아질수록 검색이 느려지므로 인덱스를 사용합니다.
- `ivfflat`은 대량 벡터 검색 시 속도를 높이기 위한 인덱싱 방식입니다.
- `vector_cosine_ops`는 **코사인 유사도 기반 인덱스**를 의미합니다.
- `lists = 100`은 벡터들을 내부적으로 100개 클러스터로 나누겠다는 뜻이며, 벡터 수가 많을수록 인덱스 성능 향상에 효과적입니다.
- 벡터가 1만 개 있다고 하면, lists = 100이면 그걸 100개의 그룹 으로 나누고, 검색할 때는 전체를 다 훑지 않고 입력 벡터와 가장 비슷한 그룹 몇 개만 탐색합니다.
- 벡터 검색에서 "정확한" 유사 벡터를 찾으려면 모든 데이터를 비교해야 합니다.
- 해당 방식은 데이터가 많아질수록 느려지기 때문에 정확도는 약간 포기하더라도 훨씬 빠르게 유사 벡터를 찾는 방식입니다.
- 그래서 양이 방대해지면 사용하는 방식입니다.

| 연산자   | 유사도 기준 | 인덱스 연산자명            | 설명                    |
| ----- | ------ | ------------------- | --------------------- |
| `<->` | L2 거리  | `vector_l2_ops`     | 유클리디안 거리 기반           |
| `<=>` | 코사인 거리 | `vector_cosine_ops` | 벡터를 정규화한 후 각도 기반      |
| `<#>` | 내적     | `vector_ip_ops`     | 정규화 없이 dot product 기준 |

---

## 8. 간단한 추천 시스템 예제 코드 (Python + psycopg2)

```python
import psycopg2

# 사용자의 선호 임베딩 (평균 LIKE 기사 벡터)
user_pref_vector = ... # 비교를 위해 선정한 벡터

# PostgreSQL 연결
conn = psycopg2.connect(
    dbname='news',
    user='myuser',
    password='my',
    host='localhost',
    port=5432
)
cur = conn.cursor()

# Python 리스트 → PostgreSQL vector literal 문자열로 변환
vector_str = "[" + ",".join(str(v) for v in user_pref_vector) + "]"

# 벡터 기반 추천 쿼리
query = '''
SELECT id, title, embedding
FROM news_article
ORDER BY embedding <=> %s::vector
LIMIT 3;
'''

# 사용자 임베딩을 기반으로 추천 기사 쿼리 실행
cur.execute(query, (user_pref_vector,))
results = cur.fetchall()

# 추천 기사 출력
print("추천 기사:")
for row in results:
    print(f"- {row[1]}")


```
- <=> 연산자는 cosine distance(코사인 거리) 계산
- 즉, 우리가 쓰고 있는 <=> 는 코사인 유사도 수식을 계산

---

### Django ORM에서 `CosineDistance` 사용 예시

```python
from pgvector.django import CosineDistance

# 사용자의 선호 임베딩 (평균 LIKE 기사 벡터)
user_pref_vector = [0.15, 0.85, 0.2]

NewsArticle.objects.order_by(CosineDistance("embedding", user_pref_vector))[:3]
'''
NewsArticle.objects → NewsArticle 테이블에서 전체 데이터를 조회
.order_by(...) → 특정 기준으로 정렬
CosineDistance(...) → embedding 필드와 user_pref_vector 간의 코사인 거리 기준 정렬
[:3] → 상위 3개 결과만 가져옴 (LIMIT 3과 동일)
'''
```

### Django ORM에서 `MaxInnerProduct` 내적 사용 예시

```python
from pgvector.django import MaxInnerProduct

# 사용자의 선호 임베딩 (평균 LIKE 기사 벡터)
user_pref_vector = [0.15, 0.85, 0.2]

# 내적 값이 큰 순서대로 유사한 뉴스 기사 추천
NewsArticle.objects.order_by(MaxInnerProduct("embedding", user_pref_vector).desc())[:3]
```


> Django ORM에서 SQL을 직접 작성하지 않고 벡터 유사도 기반 정렬이 가능합니다.

### Django에서 VectorField 사용

```python
from pgvector.django import VectorField

class NewsArticle(models.Model):
    ...
    embedding = VectorField(dimensions=1536)
```

---

### 적용 흐름

1. 사용자 행동 기록 (LIKE한 기사들) → 임베딩 평균 계산
2. 평균 벡터를 기준으로 `pgvector`에서 유사 기사 검색
3. 그 결과를 Django에서 API 형태로 제공
4. 프론트에서 사용자 맞춤형 뉴스로 렌더링

