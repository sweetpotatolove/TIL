from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

index_name = "products_chapter3"

if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

index_body = {
    "settings": {
        "analysis": {
            "tokenizer": {
                "nori_custom_tokenizer": {
                    "type": "nori_tokenizer",
                    "decompound_mode": "mixed",
                    "discard_punctuation": False,
                    "user_dictionary": "dictionary/userdict_ko.txt"
                }
            },
            "filter": {
                "my_synonym_filter": {
                    "type": "synonym",
                    "synonyms_path": "dictionary/synonyms.txt",
                    "lenient": True
                }
            },
            "analyzer": {
                "user_dic_analyzer": {
                    "type": "custom",
                    "tokenizer": "nori_custom_tokenizer",
                    "filter": [
                        "lowercase",
                        "my_synonym_filter"
                    ]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "name": {
                "type": "text",
                "analyzer": "user_dic_analyzer"
            },
            "brand": { "type": "keyword" },
            "price": { "type": "float" },
            "category": {
                "type": "text",                          
                "analyzer": "user_dic_analyzer"
            },
            "rating": { "type": "float" }
        }
    }
}

es.indices.create(index=index_name, body=index_body)
print("products_chapter3 생성 완료")
