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


def transform_extract_keywords(text):
    """
    (이 부분 자체 모델 학습 시켜 대체 가능)  
    텍스트 데이터 변환 - 키워드 추출  
    입력 텍스트에서 핵심 키워드를 추출하는 변환 로직
    """
    text = preprocess_content(text)

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 텍스트에서 주요 키워드를 추출하는 전문가입니다. 다음 텍스트에서 가장 중요한 5개의 키워드를 추출해주세요. 키워드는 쉼표로 구분하여 반환해주세요"},
            {"role": "user", "content": text}
        ],
        max_tokens=100
    )
    keywords = response.choices[0].message.content.strip()
    return keywords.split(',')


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


def transform_classify_category(content):
    """  
    텍스트 데이터 변환 - 카테고리 분류  
    뉴스 내용을 기반으로 적절한 카테고리로 분류하는 변환 로직
    (자체 모델 학습 시켜 대체 가능)

    """
    content = preprocess_content(content)
    client = OpenAI() # 환병변수에 연결됨
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 뉴스 기사의 카테고리를 분류하는 어시스턴트입니다. No verbose. 카테고리는 [\"IT_과학\", \"건강\", \"경제\", \"교육\", \"국제\", \"라이프스타일\", \"문화\", \"사건사고\", \"사회일반\", \"산업\", \"스포츠\", \"여성복지\", \"여행레저\", \"연예\", \"정치\", \"지역\", \"취미\"] 중 하나입니다. 이외의 카테고리는 없습니다."},
            {"role": "user", "content": content}
        ]
    )
    model_output = response.choices[0].message.content.strip()

    if "카테고리:" in model_output:
        model_output = model_output.split("카테고리:")[1].strip()
    model_output = model_output.replace('"', '').replace("'", "").strip()

    if model_output not in ["IT_과학", "건강", "경제", "교육", "국제", "라이프스타일", "문화", "사건사고", "사회일반", "산업", "스포츠", "여성복지", "여행레저", "연예", "정치", "지역", "취미"]:
        model_output = "미분류"

    return model_output

def main():
    sample_text = """
    삼성전자는 인공지능 반도체 시장에서의 주도권 확보를 위해 차세대 고성능 AI 칩을 공개했습니다.
    이번 발표는 반도체 산업의 경쟁 구도를 바꿀 것으로 기대되고 있습니다.
    """

    print("원본 텍스트:")
    print(sample_text.strip())
    print("\n키워드 추출 결과:")
    keywords = transform_extract_keywords(sample_text)
    print(keywords)

    print("\n임베딩 결과 (앞 5개 값만 출력):")
    embedding = transform_to_embedding(sample_text)
    print(embedding[:5], "...")

    print("\n카테고리 분류 결과:")
    category = transform_classify_category(sample_text)
    print(category)


if __name__ == "__main__":
    main()
