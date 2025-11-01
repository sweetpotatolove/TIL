# 딥러닝 및 이미지 파운데이션 모델
## “이미지 파운데이션 모델”

---

## 📘 CONTENTS
1. AI 파운데이션 모델 개념 및 대표 모델  
2. Vision-Language Model (VLM)  
3. Small VLM과 파운데이션 모델들 소개  
4. 개인화, 합성 데이터 활용 사례  

---

## 1차시  
### AI 파운데이션 모델 개념 및 대표 모델

---

## 학습 시작

- 학습데이터와 계산 리소스가 부족한 가난한 AI 서비스 회사(개발자)가  
  멋진 이미지 기반 AI 서비스를 개발하고자 합니다.  
  **어디서부터 시작하면 좋을까요?**

- 기존 이미지 AI 모델은 학습된 도메인과 유사한 데이터에서만 잘 작동했습니다.  
  그러나 실제 사용자 서비스는 전혀 예측하지 못한 데이터가 주어지는 경우도 많습니다.  
  학습하지 않은 상황에서도 동작하는 서비스를 개발하고자 할 때,  
  **어떤 특징을 갖는 이미지 AI 모델이 필요할까요?**

- **실용적인 이미지 AI 모델**을 가지고 어떤 서비스를 만들 수 있을까요?

---

## 학습 목표

- **AI 파운데이션 모델의 개념을 이해하고, 특징을 설명할 수 있다.**  
- **Pre-training, Fine-tuning, Zero/Few-shot 개념을 구분할 수 있다.**  
- **기존 머신러닝 모델과의 차이를 이해할 수 있다.**  
- **대표적 AI 파운데이션 모델 중 하나인 CLIP 모델의 개념과 역량을 알아본다.**

---

## AI 파운데이션 모델의 개념

---

## 1-1. 파운데이션 모델(Foundation model)이란?

### ▍AI 모델
- 함수 또는 프로그램  
- 입출력을 연결해주는 함수 + 데이터로 학습된 함수 +  
  **학습 때 보지 못했던 데이터에 대해서도 작동해야 하는 의무**
- 예시 : 뉴럴넷  
  - 입력 → 뉴럴넷 → 출력  

(이미지: dog/cat 분류를 수행하는 Neural Network 구조)

---

## 1-1. 파운데이션 모델(Foundation model)이란?

### ▍이상적인 AI 모델
- 만약 AI모델이 이 세상에서 발생 가능한 **모든 데이터**와  
  **각 데이터의 설명**을 모두 기억하고 있다면?

(이미지: 로봇이 데이터를 관찰하며 모든 이미지를 기억하는 모습)

### ▍이상적인 AI 모델
- 만약 AI모델이 세상의 모든 데이터와 설명을 기억하고 있다면?  
- 내가 얻고 싶은 답과 유사한 답이 이미 DB에 저장되어 있을 확률이 높음 →  
  **검색 엔진과 유사**
- 예시: 최근접 이웃 탐색 (Nearest Neighbor Search) 알고리즘  
- 그러나, 데이터 확보·저장·탐색은 매우 비용이 크고 현실적이지 않음

(이미지: Database와 Search Engine 구조 예시)

### ▍현실적인 기계학습 모델
- 학습 = AI모델에 데이터를 **패턴화**하여 **압축**  
- 이 과정에서 비슷함과 다름을 파악하게 되고,  
  패턴을 익히면서 새로운 데이터에 대한 **일반화 능력**이 생김  
- → **세상의 수많은 데이터를 최대한 기억할 수 있다면?**

(이미지: Neural Network가 여러 이미지를 압축하며 학습하는 모습)

---

# 1-1. 파운데이션 모델(Foundation model)이란?

▍파운데이션 모델이란?

• 대규모 데이터를 폭넓게 학습한 후, 다양한 문제에 빠르게 적용할 수 있는 범용 대형 AI 모델  
• 미국 스탠포드 대학 사람 중심 AI 연구소에서 2021년 출간된 보고서에서 새로운 범주로 구분을 시작  

▍파운데이션 모델  

• 기존 딥러닝 개발 패러다임 : 아기와 같이 언어, 시각, 청각, 촉각 등 기본적인 것들부터 배워 나가야 함  
• 파운데이션 모델 패러다임 : 거대 모델(커다란 뇌) + 대규모 데이터 학습 (많은 지식과 경험) 기반  
▷ 새로운 일을 처음 접해도 금방 배우고 잘할 수 있음  

▍파운데이션 모델  

• 파운데이션 모델 기반 개발 프로세스  

▍파운데이션 모델의 특징

특징 1 [대규모] : 트랜스포머 모델 + 대규모 언어 데이터 학습  
• 테스트에 상관없이 비슷한 패턴들이 등장하고 있음  
• 주로 비지도학습으로 훈련된 모델들도 많이 등장  
  - 의미하는 바 : 쉬운 데이터 수집 + 대규모 학습  

특징 2 [적응성] : 높은 파인튜닝 성능 (높은 태스크 적용 성능)  
• 믿고 쓸 수 있는 모델  

특징 3 [범용성] : 다양한 작업, 한정되지 않는 출력 지원  
• 예시 - 물체 판별  
  - 기존 : 20여개의 물체 종류 구분  
  - 파운데이션 모델 : 만 개 이상을 물체 종류 구분  
  (또는 자연어 기반의 한정되지 않은 대상에 대한 인식)  

▍파운데이션 모델에 의한 AI 모델 개발의 변화  

• 과거에는 매번 모델을 새로 학습했지만, 이제는 잘 학습된 모델들을 얼마나 잘 활용하느냐가 핵심  
• 파운데이션 모델 하나 확보하는데 투여되는 계산 리소스는 일부 대규모 인프라 이외에 불가  

---

▍적용 활용

활용 되는 기법들: 프롬프트 {엔지니어링, 튜닝}, 전이학습, 적용(Adaptation)학습, 파인튜닝  

- Zero-shot : 처음 보는 문제를 추가 학습 없이 바로 적용 (모델 자체가 가진 배경 지식 활용)  
- Few-shot : 예제 몇 개만 보여주면 바로 적용 가능  
- Fine-tuning : 처음부터 배우지 않아도, 조금만 알려주면 금방 적용  
  (모델 자체를 업데이트. 모델 가중치가 변경 됨)  

---

# 대표적 AI 파운데이션 모델  
- CLIP -

---

# AGI를 향해서

▍Human’s Intelligence (cognition) = perception ∪ higher cognitive processes  

• AI는 사람의 지능과 유사점/차이점 분석을 통해 발전  

▍Human’s Intelligence (cognition) = perception ∪ higher cognitive processes  

• 2022년 11월 이전 : 각 분야별로 지능의 매우 부분적 능력만을 개별적으로 모델링 시도  
• 2022년 11월 (ChatGPT) 이후 : 대규모 언어모델(LLM)이 높은 사고/추론 성능을 보여주기 시작  
  (다양한 인지 능력 벤치마크에서 인간 수준 근접)  

⇒ 그러나 사고 능력과 언어 능력 만으로 현실 세계를 이해하기에 충분할까?  

---

# LLM에 눈을 달아볼까? (시각언어모델)

사용자 : “누가 이 그림을 그렸어?”  
AI : “이 그림은 모나리자로 알려진 여성을 그린 레오나르도 다빈치의 유명한 그림입니다. 여성의 신비로운 미소를 보여주는 초상화로, 세계에서 가장 유명하고 상징적인 예술작품 중 하나가 되었습니다. …”  

입력: “이 이미지를 설명해줘”  
출력: “빨간 스카프를 두르고 있는 고양이 사진이에요.”  

---

# 시각언어모델 예시 - ChatGPT with GPT-4

▍GPT-4 (2023)

• 자연어 입력에 국한된 기존의 거대 언어 모델에서 더 나아가 이미지, 문서, 음성 등  
  멀티모달(multi-modal) 데이터를 처리할 수 있는 모델  
• GPT-4 API를 활용하여 다양한 도메인의 이미지 데이터와 결합한 모델이 개발됨 (예시 : 제조 AI)  

예시) GPT-4V for Generic Anomaly Detection  

유저  
왼쪽 이미지가 결함을 가지고 있는지 판단해줘. 만약 결함이 있다면, 구체적인 이유를 제공해줘.  

GPT-4  
이미지는 병이나 용기의 상단 부분으로 보이는 원형 물체 안으로 끈이나 줄이 통과하고 있는 것처럼 보입니다.  
검토 결과  
1. 원형 물체의 가장자리에 이물질이나 입자가 보입니다.  
2. 가장자리에는 굵은 자국이 보입니다.  
3. 줄에는 헤지거나 마모된 부분처럼 보이는 불규칙한 부분이 있습니다.  

# 시각언어모델 예시 - ChatGPT with GPT-4

▍GPT-4의 시각언어 멀티모달 언어모델로써의 능력 시연 [Sketch-to-web page (HTML)]

---

# 시각언어모델 예시 - Computer use, Claude

▍Claude 기반 Computer use 기능 시연 - 친구와의 여행 플랜 세우기  
• 수많은 컴퓨터 프로그램의 다양한 인터페이스를 이해하기 위해서는 시각 이해도 필요  

---

# 눈으로 어떤 것을 쓸까? CLIP(2021) by OpenAI

▍CLIP(2021) by OpenAI  

• 언어와 이미지의 유사도 학습  

• CLIP 모델 구조  

---

# 1-1. CLIP (2021)

▍CLIP: Contrastive Language-Image Pre-training, by OpenAI  

• AI가 언어와 시각을 통합해서 이해하는 방식을 보여준 패러다임 전환 제시  

• 파운데이션 모델로써의 특징  
  - 입력: 학습하지 않은 새로운 도메인의 입력 데이터에 대해서도 좋은 성능을 발휘 (제로샷 전이)  
  - 출력: 자연어를 이용해 한 번도 본 적 없는 카테고리도 텍스트 설명만으로 출력 정의 가능 (언어 인터페이스)  

▍대조 학습 기반(Contrastive Pre-training)의 언어-이미지 사전 학습  

• 인터넷 데이터를 통한 지도 학습(supervised learning)을 통해 자연어 기반 시각 개념 학습  
• 다양한 이미지-자연어 쌍으로 학습  
  - 인터넷에서 수집된 수억개의 이미지·텍스트 쌍  
  - Alt-text HTML tag, 이미지 캡션, 제목 등을 기반으로 수집  
  - 데이터 정제 과정을 거침 (중복 이미지, 해상도/품질 낮은 이미지, 짧은 텍스트 등)  

• 다양한 이미지-자연어 쌍으로 학습  
  - 텍스트 인코더 : Transformer  
  - 이미지 인코더 : ViT-B (또는 ResNet50)  

---

# 1-2. CLIP 구조 - 텍스트 인코더 (Transformer 기반 Text Encoder)

▍Remind - Transformer  

• 트랜스포머 구조 = 인코더 (Encoder) + 디코더 (Decoder)  
• CLIP에서는 Encoder only 구조 사용  

▍Remind - Transformer  

• 토큰이라는 단위의 입력  
• 입력된 토큰 간의 관계성을 집중하는 Attention 메커니즘으로 구성  
• L 길이의 입력 토큰은 D-차원 특징벡터(임베딩)의 배열로 형태로 입력 (L x D)  

• 자연어 데이터 :  
  Sub-word 단위의 임베딩  

---

# 1-3. CLIP 구조 - 이미지 인코더 (ViT: Vision Transformer, 2020)

▍Remind - Vision Transformer  

• 입력 구성  
  - 텍스트 인코더 (자연어 데이터 입력): Sub-word 단위의 임베딩  
  - 이미지 인코더 (이미지 데이터 입력): 패치 단위의 임베딩  
• ViT: 비전 분야에 트랜스포머를 (최소 수정으로) 적용한 모델  


▍Remind - Vision Transformer

• 이미지를 작은 패치(16x16x3)로 나눔  
• 각 패치를 1D로 Flatten  
• Learnable position embedding 사용  
  - 이미지 내에서 각 패치의 위치 민감 정보 추가  
  - 모델 학습 과정에서 함께 학습됨  
• Transformer encoder : 패치 처리  
• MLP Head를 통해 분류 작업 수행  
  - Head를 수정하여 다른 작업을 위한 transfer learning 활용 가능  
  - CLIP에서는 CLIP 학습법으로 학습됨  

---

# 1-4. CLIP (2021) 학습

▍대조 학습 (Contrastive learning)

• 학습 기준  
  - 목표 이미지(앵커)를 대응하는 텍스트(양성)와 가깝게  
  - 일치하지 않는 여러 텍스트(음성)와는 멀게  

▍대조 학습 (Contrastive learning)

Numpy-like pseudocode  

```
# image_encoder  - ResNet or Vision Transformer
# text_encoder   - CBOW or Text Transformer
# I[n, h, w, c]  - minibatch of aligned images
# T[n, l]        - minibatch of aligned texts
# W_i[d_i, d_e]  - learned proj of image to embed
# W_t[d_t, d_e]  - learned proj of text to embed
# t              - learned temperature parameter

# extract feature representations of each modality
I_f = image_encoder(I)  #[n, d_i]
T_f = text_encoder(T)   #[n, d_t]

# joint multimodal embedding [n, d_e]
I_e = l2_normalize(np.dot(I_f, W_i), axis=1)
T_e = l2_normalize(np.dot(T_f, W_t), axis=1)

# scaled pairwise cosine similarities [n, n]
logits = np.dot(I_e, T_e.T) * np.exp(t)

# symmetric loss function
labels = np.arange(n)
loss_i = cross_entropy_loss(logits, labels, axis=0)
loss_t = cross_entropy_loss(logits, labels, axis=1)
loss   = (loss_i + loss_t) / 2
```

▍대조 학습 (Contrastive learning)

*️⃣ 𝑠ᵢⱼ : i번째 이미지와 j번째 텍스트 임베딩 간의 코사인 유사도  

Softmax 기반 손실 계산  

---

# 1-4. CLIP 간단 응용

▍제로샷 이미지 인식기  

• 텍스트로 원하는 물체 카테고리 리스트 준비  
• 텍스트 기반 카테고리 리스트를 텍스트 임베딩으로 변환하여 Vector DB 준비  
• 쿼리 이미지와 비교해서 가장 높은 점수의 카테고리 반환  

▍생각해보기  
- 검색 시스템과 유사성은 무엇일까?  
- 카테고리 이외에 어떤 것이 가능할까?  
- 카테고리가 정말 많을 경우에 어떻게 효율화할까?  

---

# 강의 정리

▍오늘 공부한 내용 요약 및 정리

• 파운데이션 모델은 대규모 데이터로 사전학습된 범용 모델  
• 파운데이션 모델의 방대한 사전 지식을 이용해 다양한 태스크에 빠르게 적용 가능  
  - 장점: 데이터/리소스 효율적, 범용성, 확장성, 높은 성능  
• 파운데이션 모델은 대규모, 적응성, 범용성의 특징을 가짐  
• 대표 이미지 파운데이션 모델:  
  인터넷 상의 대규모 {텍스트, 이미지} 페어 데이터를 활용한 이미지-언어 연관성을 학습한  
  CLIP 파운데이션 모델과 그 제로샷 이미지 인식기 응용  

---

# 2차시  
Vision-Language Model (VLM)

---

# 학습 시작

• 주어진 이미지와 장면을 분석하고 이해하는 서비스를 만들기 위해  
  지금까지 배운 이미지 인식기, 물체 탐지 모델로 충분할까?  
  인식/탐지 태스크 출력의 제한  

• 세상에 존재하는 수많은 케이스들을 이해하고,  
  사용자의 요구에 맞춰 이미지를 분석할 수 있는 진짜 인텔리전트한 모델은 없을까?  

• 나 대신 어려운 그래프와 문서들을 이해하고 컨설팅 해주는 모델은 어떻게 만들지?  

• 나와 같은 것을 "보고" "대화"를 나눌 수 있는 AI 모델을 구축해보자!  

---

# 학습 목표

• 고도화된 CLIP 계열인 SigLIP의 등장 배경에 대해서 이해한다.  
• Vision-Language Model의 구조 및 구축 패턴에 대해서 파악한다.  
• LLaVA, Qwen-VL, InternVL 등 최신 시각-언어 파운데이션 모델들의  
  발전 동향에 대해서 설명할 수 있다.  
• (심화) 추가 학습을 요구하지 않는 CLIP계열 멀티모달 정합 모델의 심화 응용 사례를 파악한다.  

# Vision-Language Models

---

## 3-1. AGI를 향해서

▍Human’s Intelligence (cognition)
= perception ∪ higher cognitive processes

- World → Perception(CLIP) → Cognition(LLM) → Interpretation
- 인간의 지능은 인식(Perception)과 고차 인지(Cognition)의 결합으로 이해 가능

---

## 3-1. 멀티모달 언어 모델

▍이미지, 소리, 비디오 등 다양한 모달리티를 함께 이해하고 처리할 수 있는 언어 모델

• 대표적인 모델  
  - ChatGPT, Claude, LLaVA(2023), InstructBLIP, Qwen-VL, InternVL, LLaMA-Vision, smolVLM, Phi, HyperClovaX-SEED-Vision 등  

• 응용 사례  
  - 텍스트와 이미지를 결합한 대화형 AI, 이미지 설명, 문서 이해, 비디오 분석 등 다양한 분야에서 사용  

구조 예시  
```
Image → [Image Encoder] → Feature map  
→ [Linear Projection] (Soft prompt 형성) → [Text Decoder] → “A picture of a dog on a skateboard”
```
(Image Space → Text Space)

---

## 3-2. LLaVA (Large Language and Vision Assistant, 2023)

▍Vision과 Language 모델을 결합한 모델(VLM)로,  
텍스트와 이미지를 동시에 이해

• 주요 특징  
  - 이미지 인식과 텍스트 생성을 결합하여,  
    이미지 설명 생성 또는 시각적 질문 응답 작업에서 뛰어난 성능  
  - 이미지, 명령(Instruction), 답변이 주어진 데이터셋을 구축하여  
    Instruction tuning으로 학습  

• 응용 사례  
  - 이미지 기반 질문 응답(Visual QA), 이미지 설명 생성, 시각적 정보 기반 대화 등  

---

## SigLIP (2023)

▍SigLIP은 softmax 대신 sigmoid 기반 손실함수 사용

• 기존 CLIP의 Contrastive learning 한계  
  - 이미 멀리 배치된 음성 데이터까지 계속 멀게 학습 → 비효율  
• SigLIP은 **일치하지 않는 음성 데이터에만 제한된 영향**을 주는 손실함수 설계  

즉, SigCLIP은 CLIP의 softmax 기반 대조학습을 sigmoid 기반으로 대체하여,  
음성 데이터의 불필요한 분리를 완화함.

---

## SigLIP (2023) - 수식 기반 설명

손실함수:  

\[
L_{SigLIP} = -\frac{1}{N^2} \sum_{i=1}^{N} \sum_{j=1}^{N} \log \frac{1}{1 + e^{-z_{ij}(s_{ij}/τ + b)}}
\]

- \( s_{ij} \): i번째 이미지와 j번째 텍스트 임베딩 간 코사인 유사도  
- \( z_{ij} \): Label (음성 → -1, 양성 → +1)  
  - 음성: \( s \) 작을수록 좋음  
  - 양성: \( s \) 클수록 좋음  
- Sigmoid는 일정 크기 이상이면 gradient가 줄어드는 완만한 형태 → 불필요한 학습 완화

---

## SigLIP (2023) - 성능 비교

▍CLIP 대비 SigLIP은 **잡음이 많은 데이터 환경에서도 더 안정적인 성능**

- Softmax(CLIP) vs Sigmoid(SigLIP) 비교  
- 데이터에 noise가 추가될수록 Sigmoid 모델의 성능 저하가 완만함  
- 최근 SigLIP 2도 공개됨 (VLM 성능 개선 목적)

---

## 멀티모달 정합 응용 (Multi-modal Alignment)

▍서로 다른 두 가지 이상의 모달리티(예: 이미지와 텍스트) 간  
공통된 임베딩 벡터 공간을 구성하는 것

• 서로 다른 모달리티 간 임베딩 유사도(연관성) 비교 가능  

• 대표적 모델  
  - CLIP (OpenAI): 이미지-텍스트 간 Multi-modal Alignment 수행  
  - ImageBind (Meta): 소리, 텍스트, 이미지, 열화상, 깊이맵 등 다양한 모달리티 결합  

→ 멀티모달 정보 간 **공통 컨셉 공간(embedding space)** 형성

---

## 멀티모달 정합 응용 ② — ImageBind

▍ImageBIND: One Embedding Space To Bind Them All  

• 이미지, 비디오, 텍스트, 오디오, 뎁스, 열화상, IMU 데이터를  
  하나의 임베딩 공간으로 결합하여 학습  

**응용 예시**
1. Cross-modal Retrieval:  
   오디오 → 비디오/텍스트 검색  
2. Embedding-space Arithmetic:  
   “새 + 파도 소리 → 바닷가의 새 이미지”  
3. Audio to Image Generation:  
   “엔진 소리 → 트럭 이미지”  
   “빗소리 → 비 오는 장면 생성”  
4. Audio to Segmentation:  
   소리 단서로 객체 위치 파악  

---

## 멀티모달 정합 응용 ③ — VLM의 눈으로 응용

▍VLM 기반 분류

• CLIP 기반 VLM 예시  
  - **BLIP-2** : CLIP + OPT/FlanT5 결합  
  - **InstructBLIP** : BLIP-2의 instruction tuning 버전  
  - **LLaVA** : CLIP + Vicuna  
  - **MiniGPT-4** : CLIP + Vicuna 기반  
  - **mPLUG-Owl** : CLIP 기반 Alibaba VLM  

• SigLIP 기반 VLM 예시  
  - **PaLI-X** : SigLIP + PaLM 결합  
  - **SmolVLM**

→ 최근엔 CLIP, SigLIP의 성공적 구조를 기반으로  
   **Vision Encoder 고도화 모델**들이 활발히 개발되는 추세

# 3-3 최신 공개 VLM 모델들 - Qwen2.5-VL
- 확장 기능
  - 강력한 문서 파싱 기능
    - 다국어 OCR
    - 테이블, 차트, 공식, 악보 이해
    - 필기체 이해
  - 정밀한 객체 그라운딩
    - 객체 탐지, 카운팅 능력 향상
  - 장시간 비디오 이해
    - 초단위 이벤트 세그먼트 추출 가능

# 3-3 최신 공개 VLM 모델들 - Qwen2.5-Omni
- Omni: 라틴어의 접두사. 모든(all), 전부(every), 전체(whole)
- 멀티모달 언어모델 분야에서의 Omni: 읽고, 쓰고, 보고, 듣고, 말하면 Omni

# 3-3 최신 공개 VLM 모델들 - Qwen3-VL
- 25.09.23 일 공개

- 확장된 활용 사례들
  - Omni Recognition
  - Powerful Document Parsing Capabilities
  - Precise Object Grounding Across Formats
  - General OCR and Key Information Extraction
  - Video Understanding
  - Mobile Agent
  - Computer-Use Agent
  - 3D Grounding
  - Thinking with Images
  - MultiModal Coding
  - Long Document Understanding
  - Spatial Understanding

# 3-3 최신 공개 VLM 모델들 - InternVL (2024)
- 상용 VLM에 맞서는 오픈소스 VLM
  - OpenGVLab에서 개발한 멀티모달 언어모델
  - InternVL 1.0부터 시작하여 현재 InternVL 2.5까지 발전
- LLM의 대규모 용량에 맞추어 이미지 모델의 용량을 증대시킴

- 상용 VLM에 맞서는 오픈소스 VLM
- 다양한 종류의 이미지 모델과 언어 모델이 결합되어 오픈소스로 공개됨

- InternVL 전체 구조도

- InternVL 학습 전략
  - (a) 단일 모델 학습 파이프라인
  - (b) LLM을 점점 키워가면서 학습하는 파이프라인

# 3-4 VLM의 성능을 높이는 트릭
- Set of Mark (SoM)
  - 다른 물체 탐지, 세그멘테이션 파운데이션 모델을 활용한 방법
  - VLM 모델들의 부족한 시각 능력을 보완하여 비약적 성능 향상
  - Computer 작동 Agent 모델에 기본적인 비주얼 프롬프팅으로 매우 유용

# 3-4. 도메인 특화 파운데이션 모델들 - 의료
- 의료 이미지(X-Ray, MRI, CT 등)를 입력 받아, 병적 진단 및 원인 설명 등의 태스크 수행
- Contrastive learning을 통해 학습
  - BiomedCLIP 모델 구조

# 심화. CLIP 모델의 고급 응용
---

# 심화 - CLIP 응용 - 멀티모달 정합 손실함수로 활용
## 서로 다른 모달리티(예: 이미지와 텍스트) 간의 변환
- 모달리티 변환을 위한 2가지 디자인
  - 변환(Translating)
  - 정렬(Matching)

## 멀티모달 정합(Multi-modal Alignment)을 활용하는 법
- 서로 다른 두 가지 이상의 모달리티(예: 이미지와 텍스트) 간의 공통된 임베이딩 벡터 공간을 구성하는 것
- 이 연관성을 거꾸로 활용하는 방법은 없을까?
- 멀티모달 정보 간 공통 컨셉 공간(Embedding space)

## 정합(Matching)을 통한 크로스모달 변환
- 멀티모달 정합 손실 함수(Multi-modal alignment loss)
  - Multi-modal 데이터(예시: 이미지와 텍스트) 사이의 정렬된 정도를 측정
  - 대표적인 텍스트·이미지 손실함수: **CLIP loss**, **Score Distillation Sampling(SDS) loss**
- **CLIP loss [Radford21]**
  - 사전학습된 CLIP 활용
- **SDS loss [Poole23]**
  - 사전학습된 text-to-image diffusion model 활용

## CLIP loss 예시
- 텍스트-이미지 간 정렬 정도 측정 (손실함수로 사용됨)

---

# 3-4. 도메인 특화 파운데이션 모델들 - 의료
## MedCLIP (2022)
- 의료 텍스트와 이미지 임베딩을 정합시킨 의료용 CLIP 모델
- 텍스트 입력으로부터 이미지 상의 질병을 탐지하거나 특정 종류의 의료 이미지를 검색하는 방식 등으로 활용 가능

## LLaVA-Med (2023)
- LLaVA를 의료 데이터에 파인튜닝한 의료 특화 모델
- 의료 이미지를 포함한 지시문 데이터(visual instruction-following data)를 통해  
  의료 이미지 기반 챗봇 대화가 가능한 멀티모달 모델

---

# 3-4. 도메인 특화 파운데이션 모델들 - 의료 (사례)
- 입력: 흉부 X-ray 이미지
- 출력: 폐렴 진단 및 설명 예시 (LLaVA-Med 대화 기반 진단 결과)
- 실제 예시:
  - 폐렴 소견 감지
  - 삽입된 장치 유무 확인 등

---

# 3-4. 도메인 특화 파운데이션 모델들 - 제조업
## AnomalyGPT (2023)
- 제조업 환경에서 발생하는 결함이나 불량을 탐지(anomaly detection)하기 위한 모델
- 챗봇 형식으로 이미지 상 결함에 대해 텍스트로 질의응답을 주고받을 수 있음
- ImageBind의 이미지 인코더와 Vicuna를 언어 모델로 활용하여 제조업 데이터에 파인튜닝

---

# 3-4. 도메인 특화 파운데이션 모델들 - 3D 언어 모델
- 3차원 표현(예: point-cloud)과 자연어의 관계를 학습한 파운데이션 모델
- **3D LLM 모델 구조**
  - 3차원 질문-대답 생성
  - 3차원 공간 네비게이션
  - 로봇팔 동작 생성

---

# 3-4. 도메인 특화 파운데이션 모델들 - 로봇 행동 모델
- 입력: 사람의 텍스트 명령 + 로봇 시점 영상
- 출력: 로봇 행동 (위치 변화, 관절 움직임 등)
- 텍스트 명령 기반 로봇 동작 예시
- 응용 사례: **PaLM-E** (다중 모달 명령 → 로봇 행동 변환 모델)

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 정합(Matching)을 통한 크로스모달 변환
- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

“정면을 향해 걷고 있는 앨런 튜링”  
“춤추고 있는 프레디 머큐리”

Text-to-X  
(예시 : Text-to-3D)

- CLIP loss 예시  
- 단일 데이터에 대해서만 학습 = 최적화 (학습X)

### 다양한 활용 예시
- 이미지 캡셔닝  
- 텍스트 입력을 통한 이미지 스타일 변환  
- Text-to-image 생성  
- Text-to-motion 생성  
- Text-to-3D 물체 생성  
- 텍스트 입력을 통한 이미지/비디오 검색  
…  
(지난 4년 동안 약 4만편 이상 인용)

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - ZeroCLIP
- 입력: 이미지 / 출력: 캡션  
- 다양하고 구체적인 텍스트 생성, 제한된 OCR (글자인식) 능력

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - StyleCLIP
- 입력: 텍스트 명령, 원본 이미지 / 출력: 편집된 이미지

---

# 심화 - CLIP 응용 : 멀티모달 정합 손실함수로 활용

## 응용 결과 예제 - CLIP-Actor
- 입력: 텍스트 설명 / 출력: 3D 애니메이팅 아바타

---

# 강의 정리

## 오늘 공부한 내용 요약 및 정리
- CLIP의 학습 디자인 한계를 간파한 SigLIP  
- VLM = Vision-Language Encoder (예: CLIP/SigLIP) + Language Model  
  - 비전 입력은 눈에 해당하는 지각 기능,  
    언어 기반의 LLM은 뇌의 사고에 해당하는 중추 역할 수행  
- 기존 언어모델은 텍스트만, CV 모델은 이미지만 처리하기 때문에  
  이를 융합하면 수많은 문제들을 하나의 모델로 해결 가능  
  - 이미지 인식, 탐지, 카운트, Visual Q&A, 추론, 글자 인식(OCR), 번역, 추론, etc.  
  - 도메인 특화 VLM 사례들  
- 심화 CLIP 응용으로 추가 데이터 및 학습 없이  
  새로운 응용 모델을 만드는 디자인 패턴 (역전파 응용)

---

# 3차시  
## Small VLM과 파운데이션 모델들 소개

---

# 학습 시작
- VLM 모델이 유용하긴 한데, 서버는 너무 비싸다.  
  내 개인 컴퓨터나 스마트폰에서 실행되는 모델은 없을까?  
  엄청 성능이 좋을 필요는 없는데  
- 사진 속 특정 대상을 자동으로 분리하거나,  
  내가 딱 원하는 고품질 이미지를 빨리 찾고 싶은데  
  어떤 프로그램을 사용하는 게 좋을까?

---

# 학습 목표
- 경량화 VLM 모델들이 어떤 것들이 있는지 살펴보고,  
  디자인 패턴과 특징을 이해한다.  
- 한국어 VLM의 별도 개발 필요성을 이해한다.  
- Segment Anything, Grounding DINO를 비롯한  
  이미지/비디오 생성 모델, 3D 복원 모델들의 기능과 입출력, 활용을 설명할 수 있다.  
- 이미지/영상 파운데이션 모델들의 산업에 미치는 영향을 상상할 수 있다.

# Small Vision-Language Models (sVLM)

---

## 1-1. OpenVLM  
**VLM 성능 리더보드**

- OpenVLM Leaderboard (https://huggingface.co/spaces/opencompass/open_vlm_leaderboard)
- 상위권 모델의 공통점 → 너무 무겁다!
- 예시:
  - InternVL 3-78B : 78.4B 파라미터
  - InternVL 3-38B : 38.4B 파라미터
  - Ovis2-34B : 34.9B 파라미터
- 대부분 30B~70B 이상으로, 실사용에는 과도하게 큼

---

## 1-2. sVLM  
**다양한 온디바이스 모델 실경량화된 소형 VLM을 만들기 위한 시도들**

- sLLM에서 이루어진 경량화 시도들이 VLM에서도 이어지고 있음  
- VLM → sLLM → sVLM 순으로 발전 중
  1. **VLM**: 멀티모달 데이터 처리를 위한 비전언어모델 개발  
  2. **sLLM**: 대규모 언어모델을 경량화하기 위한 시도  
  3. **sVLM**: 효율적인 소형 VLM 개발  
- 목표: 성능은 유지하면서도 **cheaper/faster**  
- 예시 모델: SmolVLM, MiniCPM-V2, PaliGemma 3B, InternVL2 2B, Qwen2-VL 2B, Idefics3 8B 등

---

## 1-3. SmolVLM  
**Huggingface가 개발한 sVLM**

- Vision Encoder: **SigLIP**  
- Language Model: **Llama 3.1 8B → SmolLM2 1.7B**  
- 구조:
  - Vision Encoder → Modality Projection + Pooling → LLM
  - Hidden States를 통해 이미지 특징을 텍스트로 전달  
- 설계 목표: 효율적인 Vision-Language 연동, 낮은 메모리 사용량

---

## 1-3. SmolVLM (성능 비교)

- Inference GPU memory needs (Batch Size=1)
  | Model | 1 image (GB) | 2 images (GB) |
  |--------|---------------|---------------|
  | SmolVLM (ours) | 5.02 | 5.70 |
  | PaliGemma 3B | 6.72 | 7.76 |
  | InternVL2 2B | 10.52 | 16.51 |
  | Qwen2-VL-2B | 13.70 | 23.12 |

- → SmolVLM이 가장 가볍고 효율적임  
(출처: https://huggingface.co/blog/smolvlm)

---

## 1-4. Moondream 0.5B  
**모바일 기기나 엣지 디바이스에서의 실시간 실행을 염두에 두고 개발**

- 2억 개의 파라미터, 8비트 양자화 시 다운로드 크기 479MB  
- 실행 메모리 약 996MB 수준으로 매우 작음  
- 4비트 양자화 시에는 다운로드 375MB, 메모리 816MB까지 감소  

### 제공 기능
- Image Captioning  
- Visual Question Answering  
- Object Detection  
- Pointing (x, y)  
- Gaze Detection  
- OCR & Document Understanding  

(출처: https://moondream.ai/c/playground)

---

## 1-4. Moondream 0.5B - Demo  
- 시각 질의(Visual Query)를 입력해 이미지 기반 질의응답, 캡션, 포인팅, 탐지 수행  
- Playground 링크: https://moondream.ai/c/playground  

---

## 1-4. Moondream 0.5B - 손쉬운 사용법  

````python
pip install moondream==0.0.5

import moondream as md
from PIL import Image

# Initialize with local model path
model = md.vl(model="path/to/moondream-0_5b-int4.mf")

# Load and process image
image = Image.open("path/to/image.jpg")
encoded_image = model.encode_image(image)

# Generate caption
caption = model.caption(encoded_image)["caption"]
print("Caption:", caption)

# Ask questions
answer = model.query(encoded_image, "What's in this image?")["answer"]
print("Answer:", answer)

## 1-5. Gemini Nano  
**온 디바이스용 경량 Gemini**

- 18억 및 32.5억 개 파라미터의 두 가지 변형 (Nano-1, Nano-2)으로 구성되어  
  스마트폰 등 디바이스 내부에서 직접 실행될 수 있도록 설계

- 2024년 출시된 픽셀 9 시리즈에는 이 Gemini Nano 모델이 탑재되어,  
  녹음 앱에서 녹음 중 실시간으로 이미지/오디오 내용을 인식하고 요약하는 기능이 구현

- 사용자가 카메라로 보이는 자료를 녹음과 함께 입력하면,  
  기기가 내부 AI를 통해 해당 이미지를 이해하고 관련 텍스트를 생성

출처: [https://github.com/vikhyat/moondream?tab=readme-ov-file](https://github.com/vikhyat/moondream?tab=readme-ov-file)

## 1-6. 갤럭시 온디바이스 AI  
**모바일 NPU로 이미지, 언어, 오디오, 영상 작업을 기기 내에서 직접 생성형 AI 실행**

- 텍스트 기반 이미지 생성  
- 인페인팅 & 아웃페인팅  
- 어조 변환 및 문법 교정  
- 자연어 기반 사진 촬영 (예: “스케이트보드 탈 때 찍어줘”)  

출처: https://github.com/vikhyat/moondream?tab=readme-ov-file

---

## 1-7. LMDeploy  
**LMDeploy를 이용한 InternVL 배포**

- LMDeploy는 LLM의 효율적 압축, 배포, 서빙을 지원하는 오픈소스 툴킷  

### 특징
- 효율적인 추론: 지속적 배치, 병렬화, 고성능 CUDA 커널 등으로 최대 1.8배 높은 처리량  
- 효과적인 양자화: 4비트 양자화 등 방식을 통해 2.4배 빠른 추론  
- 분산 서빙: 여러 머신과 GPU에서 다중 모델 서비스 배포  
- 대화형 추론: 대화 이력 재처리를 줄이는 방식으로 효율적인 대화형 추론  
- 높은 호환성: 다양한 기능을 동시에 사용 가능  

출처: https://lmdeploy.readthedocs.io/en/latest/

---

## 1-7. 실습 - LMDeploy  
**InternVL, Qwen, DeepSeek, Phi 등 다양한 VLM 제공**

### 지원 모델 목록
- LLaVA(1.5, 1.6) (7B~34B)  
- InternLM-XComposer2 (7B, 4khd-7B)  
- InternLM-XComposer2.5 (7B)  
- Qwen-VL (7B)  
- Qwen2-VL (2B, 7B, 72B)  
- Qwen2.5-VL (3B, 7B, 72B)  
- DeepSeek-VL (7B)  
- DeepSeek-VL2 (3B, 16B, 27B)  
- InternVL-Chat (v1.1~v1.5)  
- InternVL2 (1B~76B)  
- InternVL2.5(MPO) (1B~78B)  
- InternVL3 (1B~78B)  
- Phi-3-vision (4.2B)  
- Phi-3.5-vision (4.2B)  
- GLM-4V (9B)  
- Llama3.2-vision (11B, 90B)  
- Molmo (7B-D, 72B)  
- Gemma3 (1B~27B)  
- Llama4 (Scout, Maverick)  

출처: https://github.com/InternLM/lmdeploy

---

## 1-7. 실습 - LMDeploy - InternVL  
**LMDeploy를 이용한 InternVL 배포**

- LMDeploy는 LLM의 효율적 압축, 배포, 서빙을 지원하는 오픈소스 툴킷  

### 오프라인 배포
```python
from lmdeploy import pipeline
from lmdeploy.vl import load_image

pipe = pipeline('OpenGVLab/InternVL2-8B')

image = load_image('https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg')
response = pipe((f'describe this image', image))
print(response)
```

### 온라인 배포
```
lmdeploy serve api_server OpenGVLab/InternVL2-8B
```

출처: https://lmdeploy.readthedocs.io/en/latest/

---

## 1-8. 기타 sVLM  
**최신 sVLM**

- **Qwen 2.5-VL 3B**  
  - 다양한 크기의 이미지와 장시간 영상 처리 가능  
  - 표, 악보, 화학식 등 다양한 형태의 데이터 및 JSON 형식 등 처리 가능  

- **Phi-3.5 Vision Instruct 4.2B**  
  - OCR, 차트 분석, 비디오 용약 등에 특화된 경량 멀티모달 모델  

- **DeepSeek-VL2 1B**  
  - 중국 AI 스타트업으로 저비용 오픈소스 LLM 및 VLM 개발  

- **Gemma 3 1B**  
  - Google의 멀티모달 오픈소스 모델  
  - 1B ~ 27B의 다양한 크기 모델 제공  

출처:  
https://github.com/QwenLM/Qwen2.5-VL  
https://huggingface.co/microsoft/Phi-3.5-vision-instruct

---

## 2. 한국어 sVLM  

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**언어별 토큰 길이 격차 (토큰 정보밀도 차이)**

- 언어에 따라 동일한 문장이라도 토큰화 후 길이에 큰 차이 발생  
- 영어 중심 토크나이저는  
  - 영어가 일부 언어보다 최대 2.5배 높은 정보 밀도를 보여, 같은 토큰 길이에 더 많은 내용을 담을 수 있음  
  - 비영어권 언어는 컨텍스트 활용 효율이 낮고 토큰 낭비가 발생하는 “구조적” 불이익 존재  
  - (언어 자체 한계가 아닌, 토큰화 방법의 효율성 차이)

예시 (Tokens / Characters 비교)  
- 영어: 4 / 23  
- 한국어: 7 / 13  
- 중국어: 4 / 7  
- 일본어: 9 / 12  

출처: https://huggingface.co/blog/royswastik/transformer-tokenization-vocabulary-creation

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**토크나이저의 언어 편중 이슈**

- 주요 빈도가 높은 표현 위주로 설계되어, 사용 빈도가 적거나 형태가 설계 언어와 다른 언어는 비효율적으로 긴 토큰 시퀀스가 생성  

**형태소가 복잡한 언어의 토큰화**
- 핀란드어, 독일어의 경우, 하나의 단어가 매우 길거나 여러 의미를 접합해 표현하므로, 서브워드 단위로 쪼개지는 토큰 수가 크게 증가  

출처:  
Ali, Mehdi, et al. “Tokenizer choice for llm training: Negligible or crucial?” Findings of the Association for Computational Linguistics: NAACL, 2024.  
https://medium.com/@geosar/the-importance-of-tokenizers-for-multilingual-llms-a-case-study-on-greek-af5301b0bacf

---

## 2-1. 언어별 구조적·형태적 차이에 따른 토큰화 복잡성  
**토큰을 줄이려는 시도 – 한국어**

예시 문장:  
이번 방학 때 뭐해? (What is your plan for this vacation?)

- 기본(Base): 19 Tokens  
- 확장(Extended): 8 Tokens  

→ 한국어 맞춤형 토크나이저를 통해 동일 문장의 토큰 수를 절반 이하로 감소 가능

출처:  
Seo, Jean, et al. “How does a Language-Specific Tokenizer affect LLMs?” arXiv preprint arXiv:2502.12560 (2025)

---

## 2-2. 한국어 sVLM 모델  
**한국어 sVLM 모델**

- HyperCLOVAX-SEED-Vision-Instruct-3B는 NAVER가 개발한 한국어 특화 멀티모달 모델로, 텍스트와 이미지를 동시에 이해하고 텍스트를 생성  

출처: https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B

- HyperCLOVAX-SEED-Vision-Instruct-3B는 NAVER가 개발한 한국어 특화 멀티모달 모델로,  
  텍스트와 이미지를 동시에 이해하고 텍스트를 생성  

### HyperCLOVA X Vision의 정량 지표

**Public Benchmarks**

| Model | SEEDv1 (image) | MMMU (val) | TextVQA (val) | DocVQA (test) | ChartQA (test) | InfographicVQA (test) | MathVista (testmini) | VQAv2 | Average |
|--------|----------------|-------------|----------------|----------------|----------------|-----------------------|----------------------|--------|----------|
| GPT-4V | 69.1 | 56.8 | 78 | 88.4 | 78.5 | 75.1 | 49.9 | 77.2 | 71.63 |
| HCX-VLM | 75.6 | 45.1 | 77.9 | 89.8 | 81 | 65.2 | 57.1 | 81 | 71.59 |

달성률(%) 99.94  

**K-GED (한국 초·중·고 검정고시) 성능**

| Model | Correct Answers |
|--------|----------------|
| GPT-4o | 1152 / 1480 (77.8 %) |
| HCX-VLM | 1240 / 1480 (83.8 %) |

---

### 예시 1 : 안내문 요약  
> 이 사진에 있는 안내판에는 일본어 문장이 쓰여 있습니다. 요약 결과 :  
> - 1952년 졸업생들이 기증한 조각  
> - 아사쿠라 호우미의 작품으로 일본 제협회 출품작  
> - 제목은 “평화가 오다”, 1957년 학생들의 염원을 담아 기증  
> - 안내문은 작품의 제작자와 의도를 설명  

---

### 예시 2 : 요리 절차 추론  
> 재료 : 소고기, 양파, 토마토, 햄버거 빵 → 함께 햄버거 만드는 순서 예측 결과  
> 1. 햄버거 빵 준비  
> 2. 패티 형성 및 양념  
> 3. 팬에 기름 두르고 패티 굽기  
> 4. 토마토·양파 슬라이스  
> 5. 햄버거 조립 및 치즈 추가  

---

### 예시 3 : 그래프 해석  
> 원그래프에 따르면 Company A 점유율이 50%로 가장 높고,  
> Company B 25%, C 15%, D 10% → A가 최대 시장 점유율 보유  

---

## HuggingFace를 통한 한국어 sVLM 모델 사용  

1. HuggingFace 로그인 및 모델 다운로드  
2. 커스텀 모델 등록 및 불러오기  
3. 대화 데이터 구성 및 입력 생성  
4. 텍스트 생성  

---

### 1️⃣ HuggingFace 로그인 및 모델 다운로드
```python
from huggingface_hub import login
# 1. 토큰 로그인 (토큰은 https://huggingface.co/settings/tokens 에서 생성)
login(token="token_id")

from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="naver-hyperclovax/HyperCLOVAX-SEED-Vision-Instruct-3B",
    local_dir="./hyperclovax_vision_3b",
    local_dir_use_symlinks=False
)
```

---

### 2️⃣ 커스텀 모델 등록 및 불러오기
```python
from transformers import AutoTokenizer, AutoProcessor, AutoConfig, AutoModelForCausalLM
from hyperclovax_vision_3b.modeling_hyperclovax import HCXVisionForCausalLM, HCXVisionConfig

# 1. 커스텀 등록
AutoConfig.register("hyperclovax_vlm", HCXVisionConfig)
AutoModelForCausalLM.register(HCXVisionConfig, HCXVisionForCausalLM)

# 2. 모델 로드
model_path = "./hyperclovax_vision_3b"

tokenizer = AutoTokenizer.from_pretrained(model_path)
processor = AutoProcessor.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to("cpu")
```

---

### 3️⃣ 텍스트 생성
```python
chat = [
    {"role": "system", "content": "당신은 친절한 한국어 AI 비서입니다."},
    {"role": "user", "content": "안녕?"},
    {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"},
    {"role": "user", "content": "너는 무슨 음식 좋아해?"}
]

input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt", tokenize=True)
input_ids = input_ids.to(device="cpu")

output_ids = model.generate(
    input_ids,
    max_new_tokens=64,
    do_sample=True,
    top_p=0.6,
    temperature=0.5,
    repetition_penalty=1.0
)
print("="*80)
print("LLM EXAMPLE")
print(tokenizer.batch_decode(output_ids)[0])
print("="*80)
```

---

### 4️⃣ 텍스트 + 이미지 프롬프트
```python
vlm_chat = [
    {"role": "system", "content": {"type": "text", "text": "System Prompt"}},
    {"role": "user", "content": {"type": "text", "text": "User Text 1"}},
    {
        "role": "user",
        "content": {
            "type": "image",
            "filename": "tradeoff_sota.png",
            "image": "https://github.com/naver-ai/rdnet/blob/main/resources/images/tradeoff_sota.png?raw=true",
            "ocr": "List the words in the image in raster order...",
            "lens_keywords": "Gucci Ophidia, cross bag, Supreme shoulder bag",
            "lens_local_keywords": "[0.07, 0.21, 0.92, 0.90] Gucci Ophidia"
        }
    }
]
```

---

### 5️⃣ 텍스트 생성 (이미지 입력 포함)
```python
new_vlm_chat, all_images, is_video_list = processor.load_images_videos(vlm_chat)
preprocessed = processor(all_images, is_video_list=is_video_list)

input_ids = tokenizer.apply_chat_template(
    new_vlm_chat,
    return_tensors="pt",
    tokenize=True,
    add_generation_prompt=True,
)

output_ids = model.generate(
    input_ids=input_ids.to(device="cpu"),
    max_new_tokens=8192,
    do_sample=True,
    top_p=0.6,
    temperature=0.5,
    repetition_penalty=1.0,
    **preprocessed,
)
print(tokenizer.batch_decode(output_ids)[0])
```

## 2-2. 한국어 sVLM 모델  
**한국어 sVLM 모델**

- Kanana-1.5-v-3b-instruct는 Kakao가 개발한 한국어 특화 멀티모달 모델

| 모델 비교 | 전체 평균 | 영어 이미지 이해 | 한국어 이미지 이해 | 영어/한국어 멀티모달 지시 이해 |
|-------------|------------|------------------|------------------|------------------------------|
| kanana-1.5-v-3b-instruct (3.62B) | 약 70 | 약 75 | 약 60 | 약 70 |
| HCX-SEED-Vision-3B (3.72B) | 약 68 | 약 70 | 약 58 | 약 65 |
| Phi-3-Vision (4.15B) | 약 65 | 약 68 | 약 55 | 약 60 |
| Qwen2.5-VL-3B (3.75B) | 약 72 | 약 75 | 약 62 | 약 70 |
| InternVL2.5-4B (3.94B) | 약 68 | 약 70 | 약 56 | 약 66 |

출처: https://huggingface.co/kakaocorp/kanana-1.5-v-3b-instruct

---

# 다른 이미지 파운데이션 모델들 소개

---

## Remind – VLM의 성능을 높이는 트릭  
**Set of Mark (SoM)**

- 세그멘테이션을 위해 서로 다른 모델들을 결합하여 사용  
- SEEM, Semantic-SAM, SAM, MaskDINO 등 활용  

### 예시 비교  
- 입력: 이미지  
- 입력 + SoM  
→ 세밀한 객체 인식 및 위치 정확도 향상

> GPT-4V 기본 입력 → “컵”으로 오답  
> GPT-4V + SoM → “램프(12번)”으로 정답 인식  
> 위치 기반 질의(창가 좌석 등) 정확도 상승

출처: Yang et al., *Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V*, arXiv 2023

---

## 2-1. 이미지 파운데이션 모델  
**영상 파운데이션 모델 개요**

- 컴퓨터 비전(CV)에서 방대한 데이터를 학습한 모델들  
- 분할(Segmentation), 탐지(Detection), 3D 및 깊이 예측(3D & Depth) 등 다양한 작업 수행 가능  

### 영상 파운데이션 모델의 예시  
- 이미지-텍스트 유사도 측정  
- 비전-언어 모델  
- 멀티모달 융합  
- 3D LLM 구조 (Perceiver + LLM 기반 3D Feature 학습)

---

## 2-2. 이미지 세그멘테이션 모델  
**Segment Anything (SAM, 2023; SAM2, 2024) – Meta**

- 컴퓨터 비전에서도 방대한 양의 데이터로 Foundation 모델을 구축 가능함을 증명  
- 클릭, 박스, 부분 세그먼트, 텍스트 등의 유저 입력을 받아 원하는 영역 마스크를 추출  
- 약 1,100만 개 이미지 (약 10억 개의 마스크) 학습  

출처:  
Ravi et al., *SAM 2: Segment Anything in Images and Videos*, arXiv 2024  
Kirillov et al., *Segment Anything*, ICCV 2023  

---

## 2-2. 이미지 내 물체 탐지 모델  
**Grounding DINO (2023) – IDEA Research**

- 텍스트 입력을 통해 이미지 내 물체를 탐지  
- 대규모 데이터 기반으로 다양한 물체에 대한 높은 일반화 성능 확보  
- 객체 탐지 분야 Foundation 모델로 우수한 성능 달성  

**응용**  
- 이미지 검색, 탐지, 분류 작업  

출처:  
Liu, Shilong, et al. *Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection.* arXiv:2303.05499 (2023)

---

## 2-2. 이미지 내 인스턴스 탐지 및 세그멘테이션 모델  
**Grounded SAM (2024) – IDEA Research**

- Grounding DINO + SAM 결합 모델  
- 텍스트 입력으로 객체 탐지뿐 아니라 분할까지 수행 가능  
- Grounding DINO의 박스를 SAM의 입력으로 활용해 개별 물체 분할  

예시  
- 텍스트 입력: “말, 구름, 풀, 하늘, 언덕”  
- Grounding DINO: 모든 물체 탐지  
- Grounded SAM: 모든 물체를 탐지 및 분할 가능  

출처:  
https://github.com/IDEA-Research/Grounded-Segment-Anything

---

## 2-2. 비디오 내 인스턴스 탐지 및 세그멘테이션 모델  
**SAMURAI (2024) – Univ. Washington**

- 비주얼 물체 트래킹 분야 최신 (State-of-the-art, 2025.05 기준)  
- SAM2 기반 응용 모델  
- 응용 사례: 비디오 편집, 물체 제거기, 이상행동 감지, CCTV 자동 분석, 스포츠 중계 등  

출처:  
Yang et al., *SAMURAI: Adapting Segment Anything – Motion-Aware Memory*, arXiv 2024

---

## 2-3. 영상 생성 파운데이션 모델들  
**이미지 생성 (Image Generation)**

- 대규모 이미지 학습을 통해 텍스트 설명으로 새로운 이미지를 생성  

### 응용 사례 1
- 텍스트 외 조건(자세, 환경, 스타일 등)을 입력받아 이미지 생성  

### 응용 사례 2
- 텍스트 기반 3D 객체 생성  

출처:  
Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*, CVPR 2022  
Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, CVPR 2023  
Poole et al., *DreamFusion: Text-to-3D using 2D Diffusion*, ICLR 2023  
Youwang et al., *Paint-it: Text-to-Texture Synthesis via Deep Convolutional Networks*, CVPR 2024  

---

## 2-3. Closed 이미지 생성 모델  
**DALL·E 3 (OpenAI)**

- 출시 시기: 2023년 10월 (ChatGPT 통합 출시)  
- ChatGPT 및 Bing Image Creator에서 사용 가능  
- 대화형 프롬프트 개선 및 이미지 생성 지원  
- ChatGPT 내장형 서비스  
- 복잡한 프롬프트를 정교하게 반영하며 안전장치 강화  

예시 Prompt: **“우울한 아보카도”**

출처: https://openai.com/index/dall-e-3/

## 2-3. Closed 이미지 생성 모델 – DALL·E 예시

### DALL·E 2 vs DALL·E 3 비교
- **Prompt**: *An expressive oil painting of a basketball player dunking, depicted as an explosion of a nebula.*

| 모델 | 예시 설명 |
|------|------------|
| DALL·E 2 | 색채 표현은 강렬하나, 세부 묘사 및 공간 표현이 다소 거칠음 |
| DALL·E 3 | 섬세한 질감 표현, 배경(성운)의 입체감과 조명 효과 향상 |

출처: https://openai.com/index/dall-e-3/

---

### DALL·E 3 추가 예시

| 유형 | 설명 |
|------|------|
| **스티커 이모지** | 인물 사진을 기반으로 캐릭터 스티커 생성 |
| **지브리 스타일** | “원본 구조를 유지한 채로, 지브리 스타일로 만들어줘” 프롬프트를 적용한 사례 |

출처: https://openai.com/index/dall-e-3/

---

## 2-3. Closed 이미지 생성 모델 – Midjourney v7

**Midjourney v7 (Midjourney Inc.)**
- 출시 시기: 2025년 4월 알파 버전 공개  
- 모든 이미지에서 세부 묘사(높은 품질), 프롬프트 해석 정확도 향상  
- 손/신체 표현의 일관성 개선  
- 긴 프롬프트 이해, 세밀한 스타일 조정(색상·음영 등) 가능  
- 텍스트 포함 이미지 생성  

출처: https://updates.midjourney.com/v7-alpha/

---

### Midjourney v7 예시  
- 실제 같은 촬영 질감과 조명 효과  
- 영화적 분위기, 캐릭터 묘사 정확도 향상  
- 다양한 예술 스타일을 정밀하게 재현 가능  

출처: https://updates.midjourney.com/v7-alpha/

---

## 2-3. Open Source 이미지 생성 모델  
**Stable Diffusion 3 / 3.5 (Stability AI)**

- 출시 시기: 2024년 2월, 10월 공개  
- 오픈소스 가중치 공개 (HuggingFace에서 다운로드 가능)  
- Diffusion Transformer 아키텍처 도입 → 이미지 품질 및 다중 객체 표현 개선  
- 텍스트 및 글자 표현 향상 → 이미지 내 문구 생성 정확도 상승  
- 다양한 크기의 모델 제공 (800M~8B 파라미터)  

**Prompt:** *Photo studio shot of a chameleon*

출처:  
https://huggingface.co/spaces/stabilityai/stable-diffusion-3-5-large  
https://petapixel.com/2024/02/23/stability-ai-preview-next-gen-ai-image-generator-stable-diffusion-3/

---

## 2-3. Open Source 이미지 생성 모델  
**FLUX (Flux.1) – Black Forest Labs**

- 출시 시기: 2024년 8월 공개  
- 일부 상용(Pro) 버전 존재하나 Dev/Schnell은 오픈소스 제공  
- 12억 파라미터 Rectified Flow Transformer 기반 최신 모델  
- 프롬프트 준수, 스타일 다양성, 복잡한 장면 생성에 강점  
- 텍스트 이미지화 성능 우수 → 이미지 안의 글자·숫자 표현 가능  

**모델 변형**
- Pro: 최고 성능 (API 유료)  
- Dev: 오픈 가중치, 연구용(비상업)  
- Schnell: 경량·고속, 오픈소스/상업용 허용  

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

### FLUX (Flux.1) 예시  
- 다양한 예술 스타일, 현실적 조명, 고해상도 묘사 가능  
- 인물, 동물, 건축물, 제품 등 다중 카테고리 표현에 강점  

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

### FLUX (Flux.1) 텍스트 표현 예시
**Prompt:**  
*Latte art in a rich, creamy coffee, with "Stablecog" beautifully inscribed in intricate white foam.*

→ 실제 라떼 거품 위에 정교하게 문구가 새겨진 모습 구현

출처: https://huggingface.co/black-forest-labs/FLUX.1-dev

---

## 2-3. 이미지 생성모델 응용 – 파인튜닝으로 용도 변경  
**ControlNet (2023)**

- 컨트롤 조건 입력을 기반으로 사용자가 원하는 이미지를 생성  
- 커뮤니티 중심으로 매우 활발히 응용되고 있음  
- 입력 예시: Sketch, Normal map, Depth map, Canny edge, Human pose 등  
- 출력 예시: 동일 구조의 다양한 스타일 이미지 생성 가능  

출처: Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, ICCV 2023  

---

### ControlNet 응용 예시 2
- Edge 이미지 + 텍스트 조건을 함께 입력  
- 예시 프롬프트: “a high-quality and extremely detailed image”  
- 다양한 모델(SD 1.5, Comic Diffusion, Protogen 3.4 등)로 각기 다른 스타일 생성  

출처: Zhang et al., *Adding Conditional Control to Text-to-Image Diffusion Models*, ICCV 2023

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 노블-뷰 생성 모델 - Zero123XL(콜롬비아 대학; 2023) : 2D에서 3D로 변환
- 2D 이미지를 입력으로 받아 해당 물체를 특정 위치의 카메라 뷰로 바라보았을 때의 모습을 생성하는 모델  
- 추가로 2D 이미지 입력만으로 해당 물체의 3D 전체 모습을 재현할 수 있음  
- 응용 : 3D 모델링, 가상현실(VR) 및 증강현실(AR) 콘텐츠 생성에 사용  

**입력(Input)**  
**합성(Synthesized)**  

Down 30°  Left: 90°

입력 이미지  
3D 영상  

Liu, Ruoshi, et al. "Zero-1-to-3: Zero-shot one image to 3d object." ICCV. 2023.

---

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 정교한 3D Depth map 추정 – Marigold (2024)
- 단안 깊이 추정(monocular depth estimation)을 위해 이미지 생성 Diffusion 모델을 합성데이터에 파인튜닝  

(상단: 원본 이미지 / 하단: 예측된 깊이맵 / 하단부: 3D 복원 결과)

---

# 2-3. 이미지 생성모델 응용 - 파인튜닝으로 용도 변경

## 이미지 & 3D 동시 생성 모델 - JointDiT(Microsoft, POSTECH)
- 출시 시기: 2025년 5월  
- 기능: 이미지와 3D 깊이 맵 동시 생성, 입력 이미지의 3D 추정, 3D 기반 이미지 생성 등 다양한 기능 지원  
- 물리적으로 더욱 그럴듯한 장면 생성  

Byung-Ki et al., JointDiT: Enhancing RGB-Depth Joint Modeling with Diffusion Transformers, arXiv, 2025, https://byungki-k.github.io/JointDiT/

---

# 2-4. 3D 파운데이션 모델

## Depth Anything v2(HKU, TikTok; 2024)
- SAM 이후 연구된 많은 vision foundation 모델 중 깊이맵(depth map) 예측을 위한 모델  
- SAM과 마찬가지로 약 150만 개의 방대한 데이터로 학습됨  
- 이때 약 6,200만개의 라벨링 되지 않은 데이터를 추가로 활용하여 성능 극대화  
- 응용 : 자율주행, 로봇 비전, 3D 복원 등 다양한 작업에서 사용  

입력 영상  
Depth Anything으로 예측한 깊이맵  

출처: https://depth-anything.github.io  

---

# 2-4. 3D 파운데이션 모델

## 사람 중심 모델 - Sapiens(Meta; 2024)
- 인간 형태 인식을 위해 3000만 개의 이미지로 학습된 파운데이션 모델  
- 사람 중심 태스크들  

    - 2D Pose Estimation : 인간의 자세를 예측함  
    - Body-part Segmentation : 신체부위를 구분함  
    - Depth Estimation : 카메라와의 거리를 예측함  
    - Surface Normal Prediction : 3D 모델링을 위해 표면의 법선 방향을 예측함  

Image | Pose | Segmentation | Depth | Normal  

출처: https://github.com/facebookresearch/sapiens  

---

# 2-5. Closed 비디오 생성 모델

## Sora (OpenAI)
- 출시 시기: 2024년 12월 ChatGPT Pro (월 $200) 플랜에 공개. 웹 플랫폼 sora.com을 통해 제공  
  - ChatGPT Plus 사용자는 제한적으로 720p 이용 가능.  
- 텍스트 → 비디오 생성 및 이미지/동영상 → 비디오 확장 모두 지원  
- 최대 1080p, 20초 길이 영상 생성 (Pro 구독 시)  
- ChatGPT와 통합된 대화형 편집·사용자 피드백으로 반복 개선 가능  
- 물리적인 이해를 보여줌 (월드 모델로의 가능성을 보임)  

출처: Brooks et al., “Video generation models as world simulators,” Technical report 2024  

---

# 2-5. Closed 비디오 생성 모델

## Veo 2 (Google Gemini)
- 출시 시기: 2025년 4월 Gemini Advanced 구독자에게 공개  
  - Google AI Studio(Gemini)에 통합  
- 8초 길이, 720p 해상도의 와이드스크린 비디오 생성  
- 생성 영상에는 워터마크가 포함되어 합성 비디오 식별 가능  
- Whisk Animate 기능으로 정적 이미지를 비디오로 변환 가능  
- TikTok, YouTube 등에 바로 공유 가능 편의성 제공  

Prompt: *An animated shot of a tiny mouse with oversized glasses, reading a book by the light of a glowing mushroom in a cozy forest den.*

출처: https://techcrunch.com/2025/04/15/googles-veo-2-video-generator-comes-to-gemini/

---

# 2-5. Closed 비디오 생성 모델

## Veo 3 (Google Gemini)
- 자연스럽게 싱크된 소리까지 같이 생성  

(속보입니다.)

[유튜버 딸깍 디자이너 제공.]

---

# 2-5. Closed 비디오 생성 모델

## 비디오 편집 모델
- Modify Video (Luma Labs)  

(좌: 원본 영상 / 우: 편집 후 영상 예시)

# 2-5. Closed 비디오 생성 모델  
## | 비디오 편집 모델 Canvas (Higgsfield)

---

# 2-5. 응용 사례 - 컨텐츠 생성  
- [ AI로 만든 광고/영화 - Coca-Cola  

---

# 2-5. 응용 사례 - 비디오 생성 모델 기술 스택 사례  
## | HeyGen's Avatar IV  

- 입력 {텍스트 스크립트, 목소리 샘플, 사진 한 장}  
- 출력 {스피킹 비디오}  

- 기술스택  
  - NotebookLM (Google)로 podcast 스크립트 및 음성 생성  
  - ⇒ Avatar IV (HeyGen)로 영상 생성

---

# 2-5. Open Source BICIDE  
## | Wan 2.2 (Jul. 2025)

- text-to-video, text & image-to-video, sound-to-video, and image-to-video  
- 시네마 퀄리티  
- 1280x720 (720P), 24 FPS 까지 생성 가능

---

# 2-6. Dynamic 3D 파운데이션 모델  
## | MegaSaM (Google DeepMind)

- 출시 시기: 2024년 12월 (CVPR 2025 구두 발표)  
- 단안 카메라 동영상에서의 정확한 카메라 포즈 및 깊이 추정

---

# 2-6. Dynamic 3D 파운데이션 모델  
## | CUT3R (UC Berkeley, Google DeepMind)

- 출시 시기: 2025년 1월 (CVPR 2025 구두 발표)  
- 가상 시점에서의 미관측 영역 추론  
- 비디오 스트림이나 순서가 없는 사진 모음과 같은 다양한 길이의 이미지를 자연스럽게 처리

# 2-7. Audio-Vision Language Models  
## | Audio-Vision Language Models

- 대규모 언어모델에 영상, 소리 입력을 확장해 멀티모달 언어모델로 확장 발전 중  
- ImageBind 기반 비디오 입력 : OneLLM (2024)  
- 프레임 단위 비디오 입력: VideoLLaMA2 (2024)

---

## | Toward Unified Foundation Models  
### NEXT-GPT : Any-to-Any Multimodal Large Language Model (2023)

---

## | 유용한 파운데이션 모델들 정리

- 최신 프론티어 모델들은 계속해서 갱신되고 있어, 본인만의 리스트를 만들어 놓는 것이 경쟁력이 될 수 있음.

- Image: DINOV3  
- Image & Text: CLIP, BLIP, (Grounded: GLIPv2)  
- Language-to-policy: RT1, RT2  
- Multi-modal embedding: ImageBind, Mega-Transformer  
- Multi-modal LLM: InternVL, Qwen3-VL  
- Speech recognition: wav2vec, Whisper  
- Object 3D: Zero123XL  
- Text & satellite: RemoteCLIP  
- Audio & text: CLAP

---

## 강의 정리  
### 오늘 공부한 내용 요약 및 정리

- 모바일 환경에서도 실행 가능한 SVLM 들, 한국어 SVLM  
- 다양한 이미지/영상 파운데이션 모델들  
  - Segment Anything: 범용 객체 분할  
  - Grounding SAM : 텍스트와 연결된 객체 탐지/분할  
  - Stable Diffusion, FLUX: 텍스트 기반 이미지 생성  
  - Depth Anything, Sapiens: 2D 이미지에서 3D 변환  
  - Wan2.2: X-to-Video 생성 모델

# 4차시  
## 개인화, 합성 데이터 활용 사례

---

## 학습 시작

- ■ 이미지 파운데이션 모델인데도 우리 동네 관광 가이드로 활용하려고 했더니 성능이 떨어집니다.  
- 위성사진 판독에 사용하려고 해도 세밀한 구조를 잘 구분하지 못합니다.  
- 제 도메인에 맞는 모델을 만들려면 어떻게 해야할까요? 꼭 대규모로 재학습해야하는 걸까요?  

- 의료영상 데이터는 개인정보 문제로 확보가 어렵고, 움직임, 3D 데이터 등은 고가의 특수한 장비가 없으면 취득이 불가 합니다.  
- 제가 속한 기관에서는 이런 데이터 취득을 지원해주지 않아요 ᅲᅲ  
- 부족한 현실 데이터 문제를 극복할 수 있는 방법은 없을까요?

---

## 학습 목표

- ■ 도메인 특화, 개인화 모델 확보를 위한 적응 학습법들이 어떤 것들이 있는지 설명할 수 있다.  
- 적응 학습법들의 개념을 구분하여 설명할 수 있다.  
- 합성데이터의 사례를 파악하고, 역할과 응용법을 고찰한다.  
- **(실습)** Hugging Face와 Gradio를 활용해 간단한 모델 서빙과 배포를 할 수 있다.

# 파운데이션 모델의 주 응용 방법 - 적응 학습 -

---

## 1-1. 파운데이션 모델 + Fine-tuning  
### | 파운데이션 모델 (Foundation model)과 미세조정(Fine-tuning)이 필요한 이유

- 방대한 데이터로 학습된 초대형 딥러닝 모델. 다양한 작업이나 범용적인 문제에 바로 적용 가능  
- 최근에는 텍스트 뿐만 아니라 이미지, 오디오, 비디오 등의 다양한 입력 데이터를 처리할 수 있는 **멀티모달**로 확장  
- 하지만 최신 정보나 특정한 작업/도메인에 최적화되어 있지 않아, 즉시 활용이 어려운 경우가 반드시 있음  

---

### 1-1. AI 리터러시++ (강사 생각)

- ■ 차별화된 AI 종합활용능력  
  - AI의 작동 원리를 이해하고  
  - AI가 생성한 정보를 비판적으로 분석하며  
  - AI를 도구로서 효과적으로 활용할 수 있는 역량  
  - + AI를 내 입맛대로 **변경해서 사용할 수 있는 능력**

---

## 1-1. 파운데이션 모델 + Fine-tuning  
### | 미세조정 (Fine-tuning): 추가 학습을 통해 이미 학습된 모델을 조금만 튜닝하는 것

- 미세 조정(fine-tuning)을 통해 **특정 작업에 특화된 모델**을 개발할 수 있다  
- SSAFY  
- 파운데이션 모델 + Fine-tuning = **실용적인 개인화 파운데이션 모델**  
  - 적은 데이터로 학습 가능  
  - 학습 리소스 절약 가능  
  - 특정 작업에 대한 우수한 성능

---

## 1-2. Fine-tuning이란?  
### | 미세조정 (Fine-tuning): 추가 학습을 통해 이미 학습된 모델을 조금만 튜닝하는 것

- (MLLM 가정) 사전 학습된 모델에 프롬프팅을 통한 작업을 했을 때보다 **더 좋은 퀄리티**의 결과물을 생성  
- 프롬프트에 넣는 예제보다 **훨씬 더 많은 예제**를 통해 학습 가능  
- 프롬프트의 **길이가 줄어들면서 토큰 개수 절약**  
- 응답하는 데에 걸리는 시간(**latency**)을 단축

# 1-3. Remind - Gradient Descent(GD)  
## | Gradient(경사): 손실함수(Loss) 미분을 통해 구한 기울기?

---

# 1-3. 하이퍼파라미터 - Learning Rate  
## | 손실함수가 큰 값일 때 미세하게 조정하기 어려우므로 뉴럴넷 모델에 작은 비율로 반영함  
## | Learning rate: 반영할 비율

---

## [ 적절한 learning rate 값

- 모델과 데이터마다 달라 실험을 통해 구함  
- 예시: **0.005배 (5e-3)**, **0.0003배 (3e-4)**

---

## ᅵ 너무 낮은 learning rate 값

- local minimum에 빠져서 global minimum에 도달할 가능성이 낮아짐  
- 예시: **0.00000001배 (1e-8)**

---

## ᅵ 너무 높은 learning rate 값

- 마구 점프를 뛰다보니 global minimum으로 딱 맞춰 가기 어려워짐  
- 예시: **0.1배 (1e-1)**  
- 미세조정에서는 좋은 시작점에서부터 시작하기 때문에 **작은 learning rate부터 보수적으로 시작해야 함**

# 1-4. Parameter-Efficient Fine-Tuning (PEFT)

## | AI 모델의 크기

- 하드웨어의 발전, 대규모 데이터의 축적 그리고 AI 모델의 발전에 따라  
  → 학습 비용과 모델 용량이 **기하급수적으로 증가**하고 있음  

---

## | 효율적인 모델 학습

- 오픈소스로 공개된 고성능 파운데이션 모델을 출발점으로 미세조정하는 접근이 일반화되었으나, **여전히 높은 비용**  
- 효율적인 미세조정 방법  
  - 프롬프트 튜닝 (prompt tuning)  
  - Adaptor 모듈 추가 학습 (예: **Low-Rank Adaptation of Large Language Models; LoRA**)

---

## | 프롬프트 디자인 (prompt design)

- 언어모델에서 주로 활용  
- 모델이 원하는 레벨의 결과를 출력할 수 있도록 입력 텍스트를 변형하는 방법  

- 장점:  
  - 추가 학습 없이 사전학습된 모델의 예측 성능을 끌어올릴 수 있음  

- 단점:  
  - 프롬프트를 사람이 직접 설계해야 한다는 부담  
  - 성능 향상이 제한적  

---

## | 프롬프트 튜닝 (prompt tuning; 2021)

- 학습 가능한 프롬프트로서, **가상 토큰(virtual token)** 을 입력에 추가  
- 역전파를 통해 **오직 가상 토큰에 대한 임베딩만 학습**하고 나머지 모델은 고정  

- 장점:  
  - 사람의 디자인 없이 **스스로 프롬프트를 학습**할 수 있음  
  - 사전학습된 모델을 **고정**할 수 있음  
  - (지식 손실 없음 — 일반 파인튜닝은 지식 손실 발생)  
  - **적은 비용**으로 새로운 데이터셋의 모델을 학습할 수 있음  

- 단점:  
  - 학습된 프롬프트는 **해석 불가 (그저 숫자 열일 뿐)**

---

## | Adaptor 모듈 추가 학습

- **Activation을 변경**하기 위해 **작은 모듈**을 추가하여 학습하는 기법

---

# 1-5. 개인화 모델 예시  
## 프롬프트 튜닝 응용 사례 - DreamBooth

- 영상 생성 모델 개인화 방법 - 입/출력 결과 예시  
- 영상 생성 모델 개인화 방법 - 방법론 오버뷰  
  - **학습 가능 토큰 (Unique identifier)** 와 모델을 같이 Fine-tuning  
- 영상 생성 모델 개인화 방법 - 응용 결과 예시

# 데이터 효율화를 위한 합성 데이터 사용

---

## 2-1. 합성데이터 활용법 1  
### | Knowledge Distillation (Teacher-Student 학습)

- 사전학습된 고성능 모델의 지식을 작은 모델에 압축해서 빠르고 효율적으로 만들 수 없을까?  
- 지금까지 배운 미세조정과 같은 전이학습(Transfer learning)은  
  → 사전학습된 모델과 새로 학습할 모델(타겟 모델)의 **구조가 동일한 경우**를 가정하고 있었음  

---

### | 지식증류

- **높은 성능의 무거운 모델(선생님)** 을 모방하도록  
  **가벼운 모델(학생)** 을 학습하는 방법  

- 또는,  
  크기가 작은 모델(student)만으로 **충분히 학습하기 어려운 데이터 특징**을 학습하기 위해  
  비교적 무겁고 성능이 높은 모델(teacher)의 도움을 받는 기법으로 볼 수 있음  

- 선생님 모델이 예측한 **soft-label 값**과  
  학생 모델의 예측 값이 가까워지도록 학습 유도  

- **Soft-label** : [0, 1] 사이의 모델의 예측을 가짜 라벨(정답)로 사용

---

## 2-2. 합성데이터 활용법 2  
### | 파운데이션 모델들을 툴로 활용하는 방법 - InstructPix2Pix (2023)

- **명령(지시사항: instruction)** 에 따라 이미지 편집을 수행하는 모델  
- 기존 방법: 입력 이미지와 출력 이미지에 대한 **상세 설명 필요**  
- 본 방법: 입/출력 이미지 상세 설명 없이, **명령만으로 편집 수행**  

---

### InstructPix2Pix (1)

- 기존 범용 데이터셋:  
  `{이미지, 이미지 설명 (캡션)}`  
- 지시사항(instruction) 기반 이미지 편집을 **지도학습 문제**로 전환  
  → 입력 데이터-정답 쌍 필요  
- 가장 먼저,  
  `{이미지 편집에 대한 지시사항, 편집 전 이미지, 편집 후 이미지}`  
  형식의 학습 데이터셋 생성  

---

### InstructPix2Pix (2)

- 기존 범용 데이터셋:  
  `{이미지, 이미지 설명 (캡션)}`  
- 지시사항(instruction) 기반 이미지 편집을 지도학습 문제로 전환  
  → 입력 데이터-정답 쌍 필요  
- 가장 먼저,  
  `{이미지 편집에 대한 지시사항, 편집 전 이미지, 편집 후 이미지}`  
  형식의 학습 데이터셋 생성

# 2-2. 합성데이터 활용법 2 (계속)

### InstructPix2Pix (3)

- 그 후, 생성된 텍스트 데이터셋을 기반으로  
  → 별도의 이미지 편집 생성 모델로 **영상 데이터 쌍 생성**

---

### InstructPix2Pix (4)

- 생성된 이미지-명령 쌍 데이터셋을 기반으로  
  → **최종 이미지 편집 생성 모델을 학습 (fine-tuning)**

---

### | ILLaVA에서도 합성데이터 활용

- GPT를 활용하여 **시각 설명 데이터 (visual instruction data)** 생성  
- 기존에 존재하는 이미지, 캡션, 탐지 데이터셋 정답 데이터를 활용  
- GPT를 이용하여 **문제-정답 데이터 쌍을 생성**

---

# 2-3. 합성데이터 활용법 3  
### | 간단한 시뮬레이션 기반 합성 데이터: 실제 데이터를 모방하거나 새로 생성한 인공 데이터

- 예시: **가상의 이미지, 텍스트, 소리** 등을 알고리즘을 통해 생성  
- 실제 데이터를 수집하거나 사용하기 어려운 경우에 대체 가능  
- 데이터 부족 문제를 해결하고 모델 성능을 개선하는 데 사용  

---

### [ 합성 데이터는 데이터 취득이 어려운 문제에서 특히 더 유용

- 실제 촬영하기 어려운 **움직임이나 환경을 시뮬레이션**하여  
  → **다양성 높은 데이터**를 생성 가능  

- 예시:  
  - **모션 증폭**  
    - 심박수 변화, 건물 진동 등의 **미세한 움직임**을 합성 데이터를 통해 학습 가능

# What's next?

---

## 3-1. AGI를 향해서  
### | Human's Intelligence (cognition) = perception ∪ higher cognitive processes

---

### | 텍스트-비디오 생성 예시  
### | 응용사례: 비디오 생성 기반 3D 장면 복원  
### | Human's Intelligence (cognition) = perception ∪ higher cognitive processes

---

## 3-1. Sora (2024) by OpenAI: EESSAFY 비디오 생성 모델

- 월드 모델로의 잠재성  
- 로봇 제어와 같은 **Embodied AI의 핵심 컴포넌트**로 주목 받고 있음

---

## 3-2. 언어모델 + 검색증강생성  
### | 언어모델 (LLM) + 검색증강생성 (Retrieval Augmented Generation; RAG)

- **유연성** : 추가 학습 없이 최신 정보 제공  
- **개인화** : 검색과 언어모델의 합성으로 개인 맞춤형 답변 가능  
- **정확성** : Verification을 통한 환각(Hallucination) 현상 감소

---

## 3-2. AGI를 향해서  
### | 툴 증강 언어모델 (Tool Augmented LLM, Agent)

#### Visual Programming by AI² (2023)  
- **Toolformer (2023)**  
- **Claude - Computer Use, MCP**

---

### | Visual Programming (2023)

- 언어 모델의 **추가 학습 없이**,  
  주어진 툴을 사용하여 사용자가 텍스트로 요청한 영상 처리를 수행  
- 사전 정의된 툴들 (예: Python APIs)

#### 응용 사례  
- 영상 질의응답  
- 영상 기반 추론  
- 영상 편집

---

### | Claude Computer Use

- 텍스트를 기반으로 **컴퓨터를 사람처럼 사용할 수 있는 서비스**  
- 컴퓨터가 수행하길 바라는 지시사항을 텍스트로 입력하면 자동으로 명령 수행  
- 각 명령어를 실행하는 **agentic tool**로 구성되어 있는 서비스

---

## 3-3. Agent  
### | Genspark AI Browser

---

## 3-3. Multi-Agent  
### | Agent Laboratory

- **Agent system**을 활용하여 연구를 자동으로 수행하는 시스템 개발  
- 연구를 진행하는 단계를 **agent system처럼 구축**하여  
  → 자동으로 **연구 주제 탐색 및 논문 작성**을 유기적으로 수행

# 실습. 허깅페이스 기반 배포/서빙

---

## 실습. 허깅페이스(Huggingface)

- AI 관련 **오픈 소스 모델과 데이터셋을 공유하는 플랫폼**
- 주요 특징:  
  - 사전학습 모델 가중치 제공  
  - 모델 학습을 위한 다양한 데이터셋 제공  
- 응용 분야:  
  - 자연어 처리(NLP)  
  - 컴퓨터 비전(CV)  
  - 음성 인식(Speech) 등 다양한 분야에서 사용

---

## | 허깅페이스 활용

- Huggingface에서 제공하는 모델을 **직접 불러와 다양한 작업에 적용**  
- 파운데이션 모델을 활용한 **손쉬운 실습 가능**

---

## 실습. Huggingface에서 제공하는 모델 서빙

### | 모델 서빙

- 사용자에게 **모델의 예측 결과를 전달**하는 절차  
- 주요 요소:  
  - **배포**: 학습된 모델을 서비스 가능한 상태로 변환하여 시스템에 설치 및 실행 유지  
  - **API 제공**: 입력을 전달하고 실행할 수 있는 인터페이스 제공 (예: REST API, gRPC)  
  - **운영 보조 기능**: 확장, 라우팅, 모니터링 등의 툴 제공

---

### | Hugging Face Inference API

- 별도 서버 구축 없이 Hugging Face 플랫폼에서 **REST API**만으로 모델 사용 가능  
- **연구 및 테스트 목적**: request 수 제한 있음 (무료, 유료 버전 존재)  
- 모든 게시 모델이 **Deploy**를 지원하는 것은 아님

---

### | Inference API 사용법 예시

- OpenAPI라고도 불림  
- 지원 언어: Python, JavaScript, cURL 등  
- `api_key`: 사용자별 고유 액세스 키  
  - Hugging Face 홈페이지의 **Access Token 발급 후 대체 필요**

---

## 실습. 모바일 모델 서빙

### | 안드로이드에서 Gemma 모델 실행하기

- 모바일 서빙 프레임워크:  
  - MediaPipe  
  - MLC LLM  
- 장점:  
  - 인터넷 연결이 없어도 작동  
  - 개인정보 보호에 유리  
- MLC 프레임워크를 통해 Gemma 모델을 다운로드하여 Deploy 가능  
- 실행 예시:  
  - MediaPipe → Gemma1  
  - MLC LLM → Gemma2

---

### | 다양한 온디바이스 모델 실행

- 예:  
  - LLM  
  - 얼굴 인식 모델 (MobileFace) 등  
- **ONNX**: 멀티플랫폼 호환성을 위한 추가 학습 주제  
- 온디바이스 배포 방법에 대한 **조사 필요**

---

## 실습. Huggingface 기반 데모 페이지

### | Gradio

- 머신러닝 모델을 웹 인터페이스로 쉽게 배포할 수 있게 도와주는 오픈소스 라이브러리  
- 코딩 지식 없이도 웹 브라우저로 모델과 상호작용 가능  
- Hugging Face와 통합되어 사용 → Gradio 기반 데모 생성·배포 용이  
- 다양한 입력/출력 형식 지원 (이미지, 텍스트, 오디오 등)  
- **간단한 코드 몇 줄**로 Gradio 앱을 만들어 Hugging Face에 업로드 가능  
- Hugging Face Spaces에 배포 시 **라이브 데모 페이지 자동 생성**

---

## 강의 정리

- **파인튜닝**은 모델을 특정 도메인/사용자에 맞게 효율적으로 적용할 수 있는 매우 실용적인 기술이다.  
- **합성데이터 활용법**은 학습/평가 데이터 취득이 어려울 때 매우 실용적인 방법론이다.  
  → 생각보다 **간단한 데이터**도 높은 활용성을 가질 수 있다.  
- 이미지 파운데이션 모델의 개발 동향:  
  - 이미지 + 언어모델의 성공 사례  
  - 멀티모달 언어모델로 확장  
- **Huggingface**는 다양한 모델이 공유되어 활용 가능한 플랫폼  
  → **Gradio**를 통해 손쉽게 모델을 서빙 가능