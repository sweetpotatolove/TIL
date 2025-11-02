
# 관통 PJT에 AI 적용하기
- AI를 사용하기 위한 구조
- FastAPI 소개
- FastAPI 테스트
- Post 요청 해보기
- 허깅페이스 Local 테스트
- Fast API로 챗봇 만들기

# AI를 사용하기 위한 구조

## 추론 서버를 포함한 아키텍처
### AI를 사용하기 위한 기본 구조
- 추론서버 : AI 추론용 서버를 두고 REST API로 추론
- 백엔드에서 추론 서버를 호출

# FastAPI 소개

## FastAPI를 ML에서 가장 많이 사용되는 Web Framework 입니다.
- REST API 서버 용도로 사용됩니다.
````
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/lunch")
def get_lunch():

  # 이곳에 코드를 넣습니다.

  return {"lunch": "Big-mac"}

# 서버 실행
# uvicorn main:app --reload
````

# FastAPI 테스트

## PyCharm 환경에서 Fast API를 테스트합니다.
- SW역량평가 환경이므로, 모든 PC에 설치되어 있습니다.

# Post 요청 해보기

## FastAPI에서 Post 요청
- Post 요청시 응답을 받아 출력하는 코드를 작성해 봅니다.
  - HTML 파일에서 접근을 위한 CORS 설정이 필요합니다.
  - 우측 Front는 ChatGPT로 생성합니다.

# 허깅페이스 Local 테스트

## 허깅페이스의 Transformer Library 사용
- Qwen3-0.6B 모델을 사용합니다.
- CPU 환경에서 추론이 잘 되는지 테스트합니다.
````
while True:
  prompt = input("입력 : ")
  result = incoke(prompt)
  print(f"AI : {result}\n")
````

# Fast API로 챗봇 만들기

## Fast API로 간단한 챗봇을 만들어봅니다.
- Front
  - ChatGPT로 html 파일을 생성합니다.
  - 전송 버튼을 누를때마다 POST 요청을 합니다.
- Back
  - Fast API로 Local LLM을 동작시킵니다.

# 끝으로
- 관통 PJT 활용 아이디어
- 앞으로의 학습 방향

# 관통 PJT 활용 아이디어 1

## Image to TEXT
- 손글씨, 인쇄된 종이 문서 등 사진으로 부터 Text를 추출해주는 Application 제작

# 관통 PJT 활용 아이디어 2

## Image to Text + Voice to Text
- 영화 이미지와 음성을 Text로 출력해주는 서비스

# 관통 PJT 활용 아이디어 3

## Image to Image
- 이미지와 Mask를 넣어, 다른 이미지로 변경해주는 서비스 제작
- InstantX/Qwen-Image-ControlNet-Inpainting

# 관통 PJT 활용 아이디어 4

## Text to Image
- 나만의 이미지를 생성해주는 Web Application
- https://huggingface.co/stabilityai/stable-diffusion-sl-refiner-1.0

# 관통 PJT 활용 아이디어 5

## Text to Voice
- 텍스트를 음성으로 출력해주는 TTS 서비스
- https://huggingface.co/hexgrad/Kokoro-82M

## 허깅페이스에서 다양한 아이디어를 얻자

## 허깅페이스 모델과 데이터셋
- 다양한 AI Application을 제작할 수 있습니다.

# 앞으로의 학습 방향

## 앞으로의 학습 방향은?

## 이제부터는 프로젝트로 기술을 통합하고, Hugging Face 중심으로 포트폴리오를 만들어야 합니다.

## 추천 학습 방향
- 모달별 모델 사용해서 데모 서비스 만들기
- 모달별 파인튜닝 노하우 습득하기
- 파인튜닝과 RAG 서비스 운영하기
- Local LLM으로 지속적인 학습하기
- 나만의 모델서버 / 추론서버 운영