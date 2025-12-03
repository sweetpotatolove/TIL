from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# 0. 기존 인덱스 삭제
for idx in ["products", "products_v2"]:
    if es.indices.exists(index=idx):
        es.indices.delete(index=idx)
        print(f"기존 인덱스 '{idx}' 삭제 완료")

# 1. 구버전 인덱스 생성 (products)
es.indices.create(
    index="products",
    body={
        "aliases": {
            "products_alias": {
                "is_write_index": False  # 읽기 전용 alias로 명시
            }
        }
    }
)
print("구버전 인덱스 'products' 생성 완료 (읽기 전용 별칭 'products_alias' 부여)")

# 2. 신버전 인덱스 생성 (products_v2)
es.indices.create(
    index="products_v2",
    body={
        "aliases": {
            "products_alias": {
                "is_write_index": True   # 쓰기 전용 alias로 명시
            },
            "products_write": {}         # 추가 별칭 예시
        },
        "mappings": {
            "properties": {
                "name": {"type": "text"},
                "brand": {"type": "keyword"},
                "price": {"type": "float"},
                "category": {"type": "keyword"},
                "rating": {"type": "float"}
            }
        }
    }
)
print("신버전 인덱스 'products_v2' 생성 완료 (쓰기 전용 별칭 'products_alias' 부여)")

# 3. 구버전(products)에 문서 삽입
es.index(index="products", id=1, document={
    "name": "Galaxy S10",
    "brand": "Samsung",
    "price": 599.0,
    "category": "smartphone",
    "rating": 4.2
    }, refresh=True
)
print("구버전 인덱스 'products'에 문서 삽입 → Galaxy S10")

# 4. 신버전(products_v2)에 alias를 통해 문서 삽입
es.index(index="products_alias", document={
    "name": "Galaxy S25",
    "brand": "Samsung",
    "price": 1199.0,
    "category": "smartphone",
    "rating": 4.7
    }, refresh=True
    )
print("쓰기 전용 alias 'products_alias'를 통해 문서 삽입 → 실제 저장 위치는 'products_v2' (Galaxy S25)")

# 5. alias 검색 (두 인덱스 모두 조회)
resp = es.search(index="products_alias", query={"match_all": {}})
print("\n=== [검색 결과: products_alias 별칭으로 조회] ===")
for hit in resp["hits"]["hits"]:
    print(f"문서가 저장된 인덱스: {hit['_index']}, 내용: {hit['_source']}")

# 6. alias 상태 확인 (_cat/aliases API 호출)
aliases = es.cat.aliases(format="json")
print("\n=== [현재 alias 연결 상태] ===")
for a in aliases:
    print(f"별칭(alias): {a['alias']} → 인덱스(index): {a['index']} (is_write_index={a.get('is_write_index')})")

# 7. alias 재설정 (remove + add)
# 이제부터는 products_v2만 사용하고 products는 alias에서 제거
es.indices.update_aliases(
    body={
        "actions": [
            {"remove": {"index": "products", "alias": "products_alias"}},
            {"add": {"index": "products_v2", "alias": "products_alias"}}
        ]
    }
)
print("\n=== [alias 재설정 완료] ===")
print("기존 'products' 인덱스는 alias에서 제거되고,")
print("'products_v2'만 'products_alias'로 접근 가능")

# 8. alias 검색 (제거 후 → products_v2만 조회됨)
resp = es.search(index="products_alias", query={"match_all": {}})
print("\n=== [검색 결과: products_alias 조회 (제거 후)] ===")
for hit in resp["hits"]["hits"]:
    print(f"문서가 저장된 인덱스: {hit['_index']}, 내용: {hit['_source']}")

# 9. alias 상태 확인 (제거 후)
aliases = es.cat.aliases(format="json")
print("\n=== [현재 alias 연결 상태 (제거 후)] ===")
for a in aliases:
    print(f"별칭(alias): {a['alias']} → 인덱스(index): {a['index']} (is_write_index={a.get('is_write_index')})")