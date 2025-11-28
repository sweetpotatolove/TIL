import psycopg2
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken

load_dotenv()

# 텍스트 변환 함수들 (키워드 추출, 임베딩 생성, 카테고리 분류)
def preprocess_content(content):
    """
    데이터 전처리 - 텍스트 길이 제한  
    토큰 수를 제한하여 처리 효율성 확보
    """
    if not content:
        return ""
        
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(content)
    
    if len(tokens) > 5000:
        truncated_tokens = tokens[:5000]
        return encoding.decode(truncated_tokens)
    
    return content

def transform_to_embedding(text: str) -> list[float]:
    """  
    텍스트 데이터 변환 - 벡터 임베딩  
    텍스트를 수치형 벡터로 변환하는 변환 로직
    (자체 모델 학습 시켜 대체 가능)
    """
    text = preprocess_content(text)

    client = OpenAI()
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return response.data[0].embedding

def get_recommended_articles(user_pref_vector):
    """
    사용자 벡터 기반으로 추천 기사 조회
    """
    # PostgreSQL 연결
    conn = psycopg2.connect(
        dbname='news',
        user='ssafyuser',
        password='ssafy',
        host='localhost',
        port=5432
    )
    cur = conn.cursor()

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

    # 연결 종료
    cur.close()
    conn.close()

    return results

def main():
    """
    메인 함수
    """
    # 기사 텍스트 예시
    article = """
    2025년 11월 25일, 서울 - 세계 경제는 빠르게 변화하고 있으며, 글로벌 공급망에 대한 의존도가 증가하고 있습니다. 이에 따라 각국 정부는 경제 회복을 위해 다양한 정책을 시행하고 있습니다. 한국은 최근 발표한 '디지털 경제 혁신 전략'에 따라, AI와 빅데이터 기술을 적극적으로 활용하여 경제 성장 동력을 확보할 계획입니다. 이 정책은 특히 중소기업 지원과 새로운 산업 분야 창출을 목표로 하고 있습니다.
    """

    # 텍스트를 벡터로 변환
    processed_article = preprocess_content(article)
    user_pref_vector = transform_to_embedding(processed_article)

    # 추천 기사 조회
    recommended_articles = get_recommended_articles(user_pref_vector)

    # 추천 기사 출력
    print("추천 기사:")
    for row in recommended_articles:
        print(f"- {row[0]}: {row[1]}")

if __name__ == "__main__":
    main()
