# Elasticsearch Search & Aggregation

## 챕터의 포인트
- Elasticsearch의 검색 방법
- Aggregation

# Elasticsearch의 검색 방법

## Elasticsearch의 검색
- 클라이언트가 클러스터 내 아무 노드에 검색 요청(GET) 전송
- 해당 노드는 Coordinate Node로 동작
- 쿼리를 모든 관련 샤드(Primary 또는 Replica 중 하나)에 전달
- 샤드별로 검색 실행 → 결과를 Coordinate Node에 다시 전달
- Coordinate Node는 결과를 취합, 정렬, 필터링 등 후처리
- 최종 결과를 클라이언트에게 응답

## URI 검색
- 간단한 검색을 수행할 때 URI 검색(URI Query String Search)을 사용
- "key=value" 형식으로 전달
- URL에 검색할 컬럼과 검색어를 지정 가능하며 검색 조건을 추가할 수 있음
- Request Body 검색 대비 단순하고 사용이 편리하지만 복잡한 쿼리를 수행할 수 없다는 한계

예시
```
GET /products/_search?q=brand:Samsung&default_operator=AND
```

## URI 검색 파라미터
- 이 밖에도 다양한 파라미터 존재

| 파라미터 | 기본값 | 설명 |
|---------|-------|-----|
| q | - | 검색을 수행할 쿼리 문자열 |
| df | - | 기본값으로 검색할 필드 지정 |
| analyzer | - | 검색어에 적용할 형태소 분석기 지정 |
| analyzer_wildcard | false | 접두어/와일드 카드 검색 활성화 여부 |
| default_operator | OR | 여러 검색어에 대한 기본 연산자 설정 (AND 또는 OR) |

예시
```
GET /products/_search?q=brand:Samsung&default_operator=AND
```

## URI 검색 결과 조정 파라미터
- 이 밖에도 다양한 파라미터 존재

| 파라미터 | 기본값 | 설명 |
|---------|-------|-----|
| _source | true | 본문 필드를 전체 표시할지 여부 |
| sort | - | 검색 결과 정렬 기준 지정 |
| from | - | 검색한 문서의 시작 문서 지정 (페이징) |
| size | - | 검색 결과로 반환할 개수 지정 |

예시
```
GET /products/_search?q=brand:Samsung&sort=price:asc&size=10&from=0
```

## Query DSL
- Elasticsearch에서 검색을 수행하기 위한 JSON 기반의 질의 언어
- JSON 형식 사용
  - HTTP 요청 시 본문의 JSON 문서를 활용하여 Elasticsearch에 검색 요청
- Query Context
  - 검색어와 문서 간의 유사도 점수(_score)를 기반으로 검색 스코어링을 통해 문서의 중요도를 평가
- Filter Context
  - 문서가 검색 조건에 해당하는지 여부만 판단, _score 값을 계산하지 않음
  - 캐싱이 가능하여 성능 최적화 가능

## Query DSL 쿼리 형식

| 필드명 | 필드 설명 |
|-------|---------|
| size | 반환할 문서 개수 (기본값: 10) |
| from | 검색 결과에서 몇 번째 문서부터 표시할지 설정 (기본값: 0) |
| timeout | 검색 수행 시간 제한 (기본값 없음, 필요 시 "30s" 등 설정 가능) |
| _source | 검색 결과에서 포함할 필드 지정 (기본값: 전체 포함) |
| query | 검색 조건이 들어가는 공간 |
| aggs | 통계 및 집계 데이터 설정 공간 |
| sort | 문서 정렬 기준 설정 |

예시(JSON)
```json
{
  "size": 10,
  "from": 0,
  "timeout": "30s",
  "_source": ["field1", "field2"],
  "query": { ... },
  "aggs": { ... },
  "sort": [ ... ]
}
```

## Query DSL 쿼리 검색

### 예시 1 — match 쿼리
- 검색 결과에서 최대 5개 문서 반환
- `description` 필드에서 `"무선 마우스"`와 유사한 문서 검색

```json
GET /products/_search
{
  "size": 5,
  "query": {
    "match": {
      "description": "무선 마우스"
    }
  }
}
```

### 예시 2 — 특정 필드 출력 + 정렬
- `name`, `price` 필드만 출력
- `category`가 `"전자기기"`인 문서 검색
- `price` 기준으로 내림차순 정렬

```json
GET /products/_search
{
  "_source": ["name", "price"],
  "query": {
    "match": {
      "category": "전자기기"
    }
  },
  "sort": [
    { "price": "desc" }
  ]
}
```

## Query DSL 쿼리 결과

```json
{
  "took": "쿼리 실행에 소요된 시간(ms)",
  "_shards": {
    "total": "검색 대상이 된 전체 샤드 개수",
    "successful": "정상적으로 검색이 수행된 샤드 개수",
    "failed": "검색 중 오류가 발생한 샤드 개수"
  },
  "hits": {
    "total": "검색된 문서의 총 개수",
    "max_score": "가장 높은 검색 점수",
    "hits": "검색된 문서 목록"
  }
}
```

## 검색 결과 정렬
- 기본 정렬 (Default Sorting)
  - `_score`: 기본적으로 검색 쿼리가 실행되면 `_score` 값(유사도 점수)에 따라 검색 결과 정렬
  - `_score` 값이 높은 문서일수록 쿼리와 더 높은 유사도를 가지므로 상위에 노출됨
  - `_score`는 TF-IDF(Term Frequency-Inverse Document Frequency) 또는 BM25 등의 알고리즘 기반으로 계산 (변경 가능)
- 특정 필드를 기준으로 정렬
  - `price(가격)` 기준 정렬: 최신 제품 또는 가격이 높은 순으로 정렬 가능
  - `name(상품명)` 기준 정렬: 이름순 정렬 가능
  - `created_at(등록일)` 기준 정렬: 최신순 또는 오래된 순 정렬 가능


## 검색 결과 정렬
- 특정 필드를 기준으로 정렬

### Request 예시 (Kibana Dev Tools)
```json
GET products/_search
{
  "sort": {
    "price": {
      "order": "desc"
    }
  }
}
```

### Python 예시
```python
response = es.search(
    index="products",
    body={
      "sort": [
        {
          "price": {
            "order": "desc"
          }
        }
      ]
    }
)
```

### Response 예시
```json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 8,
      "relation": "eq"
    },
    "max_score": null,
    "hits": [
      {
        "_index": "products",
        "_id": "2",
        "_score": null,
        "_source": {
          "name": "Samsung Galaxy Z Fold 5",
          "description": "Foldable smartphone with a large display",
          "price": 2100000
        },
        "sort": [
          2100000
        ]
      },
      {
        "_index": "products",
        "_id": "1",
        "_score": null,
        "_source": {
          "name": "Samsung Galaxy S23 Ultra",
          "description": "Samsung flagship smartphone with high-end features",
          "price": 1800000
        },
        "sort": [
          1800000
        ]
      }
    ]
  }
}
```

## 검색 결과 페이징
- 검색 결과 보여주기
  - from: 페이지를 가져올 때의 시작점
  - size: 검색 결과를 가져올 양

```http
GET products/_search
{
  "from" : 0,
  "size": 5
}
```

# Elasticsearch의 검색방법

## 멀티테넌시
- 다중 인덱스 검색의 형태
- 스키마가 달라도 검색이 가능하지만 주로 유사한 경우 사용
- products 인덱스와 services 인덱스를 대상으로 동시에 검색 가능
- _source 필드에서 "name", "category" 필드를 대상으로 검색

```http
GET products,services/_search
{
  "_source": ["name", "category"],
  "query": {
    "match_all": {}
  },
  "sort": [
    {
      "price": {
        "order": "desc"
      }
    }
  ]
}
```

```python
response = es.search(
    index="products,services",
    body={
        "_source": ["name", "category"],
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "price": {
                    "order": "desc"
                }
            }
        ]
    }
)
```

- 활용 가능성
  - 인덱스를 날짜별로 생성해서 사용하면 필요한 검색 범위만 최소화
  - 운영을 위한 초반 primary shard 생성에서 개수를 산정하기 애매함
    - 인덱스를 나눠서 활용하는 방식으로 활용 가능 (로그데이터를 날짜 단위로 쌓는 형태 등)

## Query Context
- Term level query
  - 텍스트 분석기를 사용하지 않고 정확한 값을 검색할 때 사용
  - 필터 되는 속도가 빠름
  - SQL에서 `=` 와 같은 역할

```http
GET products/_search
{
  "query": {
    "term": {
      "brand": "Samsung"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 0.2578291,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "category": [
        "Smartphone",
        "Electronics"
      ],
      "brand": "Samsung",
      "price": 1299.99,
      "release_date": "2024-01-25"
    }
  },
  {
    "_index": "products",
    "_id": "4",
    "_score": 0.2578291,
    "_source": {
      "product_id": 4,
      "name": "Samsung Galaxy Tab S9 Ultra",
      "description": "Powerful Android tablet with an AMOLED display and S Pen support.",
      "category": [
        "Tablet",
        "Electronics"
      ],
      "brand": "Samsung",
      "price": 1199.99,
      "release_date": "2024-06-15"
    }
  }
]
```

## Query Context
- Terms level query
  - 특정 필드에 대해 SQL의 IN 조건처럼 여러 값을 검색
  - 다중 값을 조회할 수 있음

```http
GET products/_search
{
  "_source": ["name", "brand"],
  "query": {
    "terms": {
      "brand": ["Samsung", "Apple"]
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 1,
    "_source": {
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung"
    }
  },
  {
    "_index": "products",
    "_id": "2",
    "_score": 1,
    "_source": {
      "name": "Apple iPhone 15 Pro Max",
      "brand": "Apple"
    }
  }
]
```

## Query Context
- Terms level query
  - 다중 값을 조회 할 수 있음
  - 텍스트와 다른 타입의 정보를 동시에 이용할 수 있음

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand", "price"],
  "query": {
    "bool": {
      "must": [
        {
          "terms": {
            "brand": ["Samsung", "Sony"]
          }
        },
        {
          "range": {
            "price": {
              "gte": 2000,
              "lte": 3000
            }
          }
        }
      ]
    }
  }
}
```

```json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 2,
    "hits": [
      {
        "_index": "products",
        "_id": "8",
        "_score": 2,
        "_source": {
          "product_id": 8,
          "name": "Samsung Odyssey Neo G9",
          "brand": "Samsung",
          "price": 2199.99
        }
      }
    ]
  }
}
```

## Query Context
- Terms level query
  - 다중 값을 조회 할 수 있음
  - 텍스트와 다른 타입의 정보를 동시에 이용할 수 있음

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand", "price"],
  "query": {
    "bool": {
      "must": [
        {
          "terms": {
            "brand": ["Samsung", "Sony"]
          }
        },
        {
          "range": {
            "price": {
              "gte": 2000,
              "lte": 3000
            }
          }
        }
      ]
    }
  }
}
```

```json
{
  "took": 0,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 2,
    "hits": [
      {
        "_index": "products",
        "_id": "8",
        "_score": 2,
        "_source": {
          "product_id": 8,
          "name": "Samsung Odyssey Neo G9",
          "brand": "Samsung",
          "price": 2199.99
        }
      }
    ]
  }
}
```

## Range Query
- 숫자, 가격, 크기, 날짜 등을 범위로 필터링할 때 사용
- SQL의 BETWEEN 또는 >=, <=, >, < 조건과 유사한 기능

| 파라미터 | 설명 |
|---------|------|
| gt  | A보다 큼 (> A) |
| gte | A보다 크거나 같음 (>= A) |
| lt  | A보다 작음 (< A) |
| lte | A보다 작거나 같음 (<= A) |

## Query Context
- Match query
  - Elasticsearch에서 가장 기본적인 전체 텍스트 검색(full-text search) 방식
  - 분석기(Analyzer)를 적용하여 단어를 토큰화 및 변환한 후 검색
  - SQL로 표현하면 LIKE '%검색어%' 와 비슷한 기능이지만 훨씬 효율적

```http
GET products/_search
{
  "_source": ["product_id", "name", "description"],
  "query": {
    "match": {
      "description": "AI"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 0.95181024,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "description": "Latest Samsung flagship smartphone with advanced AI features."
    }
  },
  {
    "_index": "products",
    "_id": "7",
    "_score": 0.9096533,
    "_source": {
      "product_id": 7,
      "name": "Samsung Galaxy Watch 6",
      "description": "Smartwatch with advanced health tracking and AI powered insights."
    }
  }
]
```

## Query Context
- Match query with operator
  - 검색어가 여러 개일 때 AND 또는 OR 조건을 적용할지 결정하는 옵션
```http
GET products/_search
{
  "_source": ["product_id", "name", "brand"],
  "query": {
    "match": {
      "name": {
        "query": "Samsung Ultra",
        "operator": "AND"
      }
    }
  }
}
```
  - `"Samsung"`과 `"Ultra"` 둘 다 포함된 문서만 반환

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 1.8066221,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung"
    }
  },
  {
    "_index": "products",
    "_id": "4",
    "_score": 1.647526,
    "_source": {
      "product_id": 4,
      "name": "Samsung Galaxy Tab S9 Ultra",
      "brand": "Samsung"
    }
  }
]
```

## Query Context
- Match Phrase Query
  - 단어 순서를 유지한 채 검색을 수행

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand"],
  "query": {
    "match_phrase": {
      "name": "Samsung Neo"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "5",
    "_score": 1.514183,
    "_source": {
      "product_id": 5,
      "name": "Samsung Neo QLED 8K 75-inch",
      "brand": "Samsung"
    }
  }
]
```

- "Samsung Neo QLED 8K 75-inch"는 검색됨, "Samsung Odyssey Neo G9"는 제외

## Query Context
- Match Phrase Query
  - 단어 순서를 유지한 채 검색을 수행하며 자동완성 형태로 검색 가능
  - "Samsung Neo"가 기억이 안나는 경우 "N"까지만 입력해도 활용하기 위한 방식

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand"],
  "query": {
    "match_phrase_prefix": {
      "name": "Samsung N"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "5",
    "_score": 1.514183,
    "_source": {
      "product_id": 5,
      "name": "Samsung Neo QLED 8K 75-inch",
      "brand": "Samsung"
    }
  }
]
```

## Query Context
- Multi Match Query
  - 여러 개의 필드를 동시에 검색할 때 사용하는 쿼리
  - match 쿼리와 다르게 여러 필드에서 일치하는 문서를 찾을 수 있음
  - `type`을 설정하여 검색 방식 조정 가능 (`best_fields`, `most_fields`, `cross_fields`)

## Query Context

### Multi Match Query (best_fields)
- 여러 필드에서 가장 높은 점수를 가진 필드만 반영
- `"Samsung"`이 name 또는 description 중 하나라도 포함된 문서를 반환
- score가 가장 높은 필드를 기준으로 결정

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand", "description"],
  "query": {
    "multi_match": {
      "query": "Samsung",
      "fields": ["name", "description"],
      "type": "best_fields",
      "operator": "or"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 1.5777334,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "brand": "Samsung"
    }
  },
  {
    "_index": "products",
    "_id": "10",
    "_score": 1.4439012,
    "_source": {
      "product_id": 10,
      "name": "Samsung SmartThings Hub",
      "description": "Central hub for smart home automation with Samsung SmartThings ecosystem.",
      "brand": "Samsung"
    }
  }
]
```

## Query Context

### Multi Match Query (most_fields)
- 여러 필드에서 모든 일치 항목의 점수를 합산
- `"Samsung"`이 name과 description 양쪽에서 검색되면 점수가 더 높아짐
- `"Samsung"`이 여러 필드에서 발견될수록 검색 결과의 점수가 증가

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand", "description"],
  "query": {
    "multi_match": {
      "query": "Samsung",
      "fields": ["name", "description"],
      "type": "most_fields",
      "operator": "or"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 1.8455216,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "brand": "Samsung"
    }
  },
  {
    "_index": "products",
    "_id": "10",
    "_score": 1.7403128,
    "_source": {
      "product_id": 10,
      "name": "Samsung SmartThings Hub",
      "description": "Central hub for smart home automation with Samsung SmartThings ecosystem.",
      "brand": "Samsung"
    }
  }
]
```

## Query Context

### Multi Match Query (cross_fields)
- 여러 필드의 텍스트를 조합한 검색
- `"Samsung"`과 `"Ultra"`가 서로 다른 필드에 있어도 검색 가능

```http
GET products/_search
{
  "_source": ["product_id", "name", "brand", "description"],
  "query": {
    "multi_match": {
      "query": "Samsung Ultra",
      "fields": ["name", "description"],
      "type": "cross_fields",
      "operator": "and"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 1.8066221,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "brand": "Samsung"
    }
  },
  {
    "_index": "products",
    "_id": "8",
    "_score": 1.7116894,
    "_source": {
      "product_id": 8,
      "name": "Samsung Odyssey Neo G9",
      "description": "Ultra-wide 49-inch gaming monitor with 240Hz refresh rate.",
      "brand": "Samsung"
    }
  }
]
```

## Query String
- Lucene Query Syntax를 사용하여 텍스트를 복합적인 쿼리 구문으로 분석하는 검색 방식
- 기본적인 텍스트 검색뿐 아니라 AND, OR, 범위 검색, 정규식 검색 등을 지원
- SQL의 LIKE, IN, BETWEEN, REGEXP 기능과 유사함

```http
GET products/_search
{
  "query": {
    "query_string": {
      "query": "name:Apple"
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "2",
    "_score": 1.8871548,
    "_source": {
      "product_id": 2,
      "name": "Apple iPhone 15 Pro Max",
      "description": "Apple's latest iPhone with an A17 Bionic chip and titanium body.",
      "category": [
        "Smartphone",
        "Electronics"
      ],
      "brand": "Apple",
      "price": 1399.99,
      "release_date": "2024-02-10"
    }
  }
]
```

## Exist Query
- 필드가 존재하는 문서만 검색
- Elasticsearch는 필드가 존재하는 문서와 존재하지 않는 문서 공존 가능

```http
GET products/_search
{
  "query": {
    "exists": {
      "field": "description"
    }
  }
}
```

## Boolean Query
- 여러 개의 조건을 조합하여 검색을 수행하는 쿼리 방식
- `must`, `must_not`, `should`, `filter` 네 가지 방식으로 조합 가능
- SQL의 AND, OR, NOT 연산과 유사함

| Boolean Query 유형 | 설명 | 예시 |
|------------------|------|------|
| must | 모든 조건을 만족하는 문서 검색 | brand = Samsung AND description = AI |
| must_not | 특정 조건을 포함하지 않는 문서 검색 | brand != Google |
| should | 하나라도 조건을 만족하면 검색 | brand = Samsung OR brand = Apple |
| filter | 빠른 검색(점수 미계산) | brand = Samsung AND description = AI |

## Boolean Query
- Brand가 Samsung이면서 AI라는 설명이 들어가는 문서 검색

```http
GET products/_search
{
  "_source": ["name", "brand", "description"],
  "query": {
    "bool": {
      "must": [
        { "match": { "brand": "Samsung" } },
        { "match": { "description": "AI" } }
      ]
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 2.3787074,
    "_source": {
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung",
      "description": "Latest Samsung flagship smartphone with advanced AI features."
    }
  },
  {
    "_index": "products",
    "_id": "9",
    "_score": 2.275957,
    "_source": {
      "name": "Samsung Neo QLED 8K 75-inch",
      "brand": "Samsung",
      "description": "Ultra-premium 8K TV with deep learning AI picture processing."
    }
  }
]
```

## Boolean Query
- Brand가 Google이 아닌 문서 검색

```http
GET products/_search
{
  "_source": ["name", "brand", "description"],
  "query": {
    "bool": {
      "must_not": [
        { "match": { "brand": "Google" } }
      ]
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 0,
    "_source": {
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung",
      "description": "Latest Samsung flagship smartphone with advanced AI features."
    }
  },
  {
    "_index": "products",
    "_id": "2",
    "_score": 0,
    "_source": {
      "name": "Apple iPhone 15 Pro Max",
      "brand": "Apple",
      "description": "Apple's latest iPhone with an A17 Bionic chip and titanium body."
    }
  }
]
```

## Nested Query
- 중첩된 객체(배열 형태의 JSON 객체)에서 특정 조건을 만족하는 문서를 검색
- 일반적으로 JSON 객체가 배열로 저장될 때 사용
- Elasticsearch는 기본적으로 문서를 평탄화(flat)하여 저장
- 따라서 중첩된 객체 내부에서 정확한 관계를 유지하려면 `nested` 타입을 사용해야 함
- `nested` 필드를 사용하지 않으면, 배열 내 다른 객체의 필드 간 관계를 유지하지 않고 검색할 수 있음

```json
"mappings": {
  "properties": {
    "product_id": { "type": "integer" },
    "name": { "type": "text" },
    "brand": { "type": "keyword" },
    "features": {
      "type": "nested",
      "properties": {
        "feature_name": { "type": "keyword" },
        "feature_value": { "type": "keyword" }
      }
    }
  }
}
```

## Nested Query

```http
GET products/_search
{
  "query": {
    "nested": {
      "path": "features",
      "query": {
        "term": {
          "features.feature_name": "Camera"
        }
      }
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 2.043074,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "features": [
        { "feature_name": "RAM", "feature_value": "16GB" },
        { "feature_name": "Storage", "feature_value": "512GB" },
        { "feature_name": "Camera", "feature_value": "200MP" }
      ]
    }
  },
  {
    "_index": "products",
    "_id": "2",
    "_score": 2.043074,
    "_source": {
      "product_id": 2,
      "name": "Apple iPhone 15 Pro Max",
      "brand": "Apple",
      "description": "Apple's latest iPhone with an A17 Bionic chip and titanium body.",
      "features": [
        { "feature_name": "RAM", "feature_value": "8GB" },
        { "feature_name": "Storage", "feature_value": "1TB" },
        { "feature_name": "Camera", "feature_value": "48MP" }
      ]
    }
  }
]
```

## Nested Query와 Object Query 차이점

- Nested query

```http
GET products/_search
{
  "query": {
    "nested": {
      "path": "features",
      "query": {
        "bool": {
          "must": [
            { "term": { "features.feature_name": "RAM" }},
            { "term": { "features.feature_value": "16GB" }}
          ]
        }
      }
    }
  }
}
```

```json
"hits": [
  {
    "_index": "products",
    "_id": "1",
    "_score": 3.9706345,
    "_source": {
      "product_id": 1,
      "name": "Samsung Galaxy S24 Ultra",
      "brand": "Samsung",
      "description": "Latest Samsung flagship smartphone with advanced AI features.",
      "features": [
        { "feature_name": "RAM", "feature_value": "16GB" },
        { "feature_name": "Storage", "feature_value": "512GB" },
        { "feature_name": "Camera", "feature_value": "200MP" }
      ]
    }
  }
]
```
  - nested 쿼리를 사용하여 같은 객체 내부에서만 `feature_name`과 `feature_value`가 일치하는지 확인하도록 검색

## Nested Query와 Object Query 차이점
- Object query

```http
GET products/_search
{
  "query": {
    "bool": {
      "must": [
        { "term": { "features.feature_name": "RAM" }},
        { "term": { "features.feature_value": "16GB" }}
      ]
    }
  }
}
```
  - `bool` + `term/match`로 nested 필드 값 검색은 가능
  - 하지만 같은 객체 내부 관계를 보장하지 못함
  - 서로 다른 배열 요소의 값이 결합되어 매칭될 수 있음 → 결과가 의도와 다를 수 있음

```json
"took": 1,
"timed_out": false,
"_shards": {
  "total": 1,
  "successful": 1,
  "skipped": 0,
  "failed": 0
},
"hits": {
  "total": { "value": 0, "relation": "eq" },
  "max_score": null,
  "hits": []
}
```

# Aggregation

## Aggregation
- Elasticsearch에서 데이터를 분석하고 통계를 계산하는 기능
- 분산된 문서에서 검색 조건에 맞는 데이터만 모아 통계 수행
- SQL의 GROUP BY, COUNT, SUM, AVG 등의 역할을 수행

- Metric Aggregations (메트릭 집계)
  - 개별 필드의 통계 값을 계산
  - sum, average, min, max, stats 등의 연산 수행
- Bucket Aggregations (버킷 집계)
  - 특정 조건에 따라 데이터를 그룹화
  - SQL의 GROUP BY와 유사
- 기타

## Aggregation
- Metric Aggregations (메트릭 집계)
  - 개별 필드의 통계 값을 계산
  - sum, average, min, max, stats 등의 연산 수행
  - 예시: 제품 가격의 평균 계산
  - `size: 0` → 문서 자체는 반환하지 않고 집계 결과만 조회

```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "average_price": {
      "avg": {
        "field": "price"
      }
    }
  }
}
```

```json
{
  "took": 30,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "average_price": {
      "value": 1409.9900177001953
    }
  }
}
```




## Bucket Aggregations (버킷 집계)
- 특정 조건에 따라 데이터를 그룹화
- SQL의 GROUP BY와 유사
- 예시: 브랜드별 제품 개수 집계
- `size: 0` → 문서 자체는 반환하지 않고 집계 결과만 조회

### Request
```http
GET products/_search
{
  "size": 0,
  "aggs": {
    "by_brand": {
      "terms": {
        "field": "brand",
        "size": 10
      }
    }
  }
}
```
- `by_brand`는 Aggregation 결과 그룹 이름 (필드명이 아님!)

### Response
```json
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 10,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "by_brand": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "Samsung",
          "doc_count": 8
        },
        {
          "key": "Apple",
          "doc_count": 1
        },
        {
          "key": "Sony",
          "doc_count": 1
        }
      ]
    }
  }
}
```

## Aggregation
- Bucket Aggregations (버킷 집계) 유형

| 유형 | 설명 |
|------|------|
| terms | 특정 필드 값으로 그룹화 (GROUP BY 역할) |
| range | 숫자 범위별로 그룹화 (예: 가격 구간별) |
| histogram | 고정 간격으로 그룹화 (예: 가격을 100 단위로 그룹화) |
| date_histogram | 날짜 단위로 그룹화 (예: 월별 판매량) |

## 집계와 필터
- 검색 결과에 대한 집계 가능
- 집계만 별도로 수행 가능

```json
GET products/_search
{
  "size": 0,
  "query": {
    "term": { "brand": "Samsung" }
  },
  "aggs": {
    "price_stats": {
      "stats": {
        "field": "price"
      }
    }
  }
}
```
- brand 필드의 Samsung이라는 keyword를 가진 경우만 price의 stats(통계적 정보)를 불러옴


```json
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 8,
      "relation": "eq"
    },
    "max_score": null,
    "hits": []
  },
  "aggregations": {
    "price_stats": {
      "count": 8,
      "min": 149.99000549316406,
      "max": 4999.990234375,
      "avg": 1537.4900245666504,
      "sum": 12299.920196533203
    }
  }
}
```