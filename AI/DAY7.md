# 자연어처리 및 텍스트 파운데이션 모델
## 거대 언어 모델

---

## 목차
1. 텍스트 파운데이션 모델 살펴보기
   - 텍스트 파운데이션 모델 (거대 언어 모델)이란?
   - 거대 언어 모델 예시
2. 거대 언어 모델의 학습
   - 지시 학습
   - 선호 학습
3. 거대 언어 모델의 추론
   - 디코딩
   - 프롬프트 엔지니어링
4. 거대 언어 모델의 평가와 응용
   - 거대 언어 모델의 평가
   - 거대 언어 모델의 응용/한계

---

## 학습 목표
- 텍스트 파운데이션 모델(거대 언어 모델)이 무엇인지 이해합니다.
- 거대 언어 모델의 학습 및 추론 방식을 이해합니다.
- 거대 언어 모델의 응용 및 한계를 파악하고, 실습을 통해 실제 사례에 적용해봅니다.

---

## 0. 학습 시작: 파운데이션 모델

### 파운데이션 모델이란?
- 대량의 데이터를 기반으로 사전 학습된 대규모 AI 모델
- 다양한 작업에 범용적으로 활용할 수 있는 기초(foundation) 역할을 함

### We will learn: 파운데이션 모델의 주요 특징
- 기존 AI 모델과의 차이점
- 3가지 핵심 구성요소

### We will learn: 텍스트 파운데이션 모델 (거대 언어 모델)
- 거대 언어 모델의 특징
- 대표적인 예시

---

## 예시: 텍스트 생성 (ChatGPT)
- ChatGPT를 활용한 텍스트 생성 예시

출처: [https://openai.com/chatgpt/](https://openai.com/chatgpt/)
- <그림0-1_텍스트 파운데이션 모델_파운데이션 모델_ChatGPT사용 예시>

---

## 예시: 비디오 생성 (SORA)
- 텍스트 기반 비디오 생성 예시

출처: [https://openai.com/index/sora/](https://openai.com/index/sora/)
- <그림0-2_텍스트 파운데이션 모델_파운데이션 모델_SORA를 통한 텍스트 기반 비디오 생성 예시>

---

## 예시: 멀티모달 입력과 출력 (GPT-4o)
- 멀티모달: 이미지, 비디오, 오디오, 텍스트

출처: [https://openai.com/index/hello-gpt-4o/](https://openai.com/index/hello-gpt-4o/)
- <그림0-3_텍스트 파운데이션 모델_파운데이션 모델_GPT-4o를 통한 실시간 질의 응답 예시>

---

## 파운데이션 모델 이전
- 새로운 테스크를 해결하려면 해당 테스크에 대한 “별도의 학습” 필요

예시:
- Early days [features] → 0/1  
- AlexNet (2012) → ship  
- BERT (2018) → "i love this movie" → pos/neg

출처: [https://cs231n.stanford.edu/](https://cs231n.stanford.edu/)
- <그림0-4_텍스트 파운데이션 모델_파운데이션 모델_AI 모델을 학습하기 위한 이전 방법론들에 대한 예시>

---

## 파운데이션 모델의 등장
- 새로운 테스크를 해결하려면 “자세한 설명(프롬프트)”을 입력해주는 것으로 충분
- ChatGPT: 텍스트 파운데이션 모델  
  (a.k.a 거대 언어 모델 or Large Language Model or LLM)

출처: [https://www.gotai.co.kr/](https://www.gotai.co.kr/)
- <그림0-5_텍스트 파운데이션 모델_파운데이션 모델_텍스트 파운데이션 모델(ChatGPT)을 통한 새로운 테스크(4행시) 해결 예시>

## 파운데이션 모델
- 새로운 테스크를 해결하려면 “자세한 설명(프롬프트)”을 입력해주는 것으로 충분 😊  
  - SORA: 비디오 파운데이션 모델

> “세련된 여성이 따뜻하게 빛나는 네온과 움직이는 도시 간판으로 가득한 도쿄 거리를 걸어 내려온다.  
> 그녀는 검은 가죽 재킷, 긴 빨간 드레스, 검은 부츠를 착용하고 검은 가방을 들고 있다.  
> 그녀는 선글라스를 쓰고 빨간 립스틱을 바르고 있다. 그녀는…”

출처: https://openai.com/index/sora/

---

## 파운데이션 모델의 3가지 구성요소

### (1) 빅데이터
- 인터넷에 존재하는 데이터 수가 기하급수적으로 증가

출처: https://medium.com/@koshwemoethu.blacknet/the-era-of-big-data-863e87f0515d

---

### (1) 빅데이터 (심화)
- 딥러닝 기반 AI 모델은 학습 데이터가 늘어날수록 성능이 증가

출처: https://epochai.org/blog/trends-in-training-dataset-sizes

---

### (2) 자가 학습(Self-supervised Learning)
- 사람이 정답을 알려줄 필요 없음
- 예시: **다음 토큰 예측(Next token prediction)** 을 통한 텍스트 파운데이션 모델(거대 언어 모델) 학습

  - 인터넷에서 데이터 추출 → “아까 밥 먹고 왔어”
  - 학습 데이터 생성  
    - 입력: 아까 밥 먹고  
    - 정답: 왔어  

출처: https://tilnote.io/books/6480b090e92fe5ef635f54df/6480a73ee92fe5ef635f4d77

---

### (3) 어텐션(Attention) 기반 트랜스포머(Transformer) 모델
- 더 많은 데이터를 학습할 수 있는 인공신경망 구조  
  - **어텐션(Attention)**: 입력 데이터에서 중요한 부분에 주의를 집중하는 메커니즘  
  - **트랜스포머(Transformer)**: 어텐션 메커니즘을 기반으로 한 신경망 구조  

출처: https://www.researchgate.net/figure/Decoder-only-Transformer-architecture-The-input-to-the-decoder-is-tokenized-text-and_fig3_373183262

---

# 1. 텍스트 파운데이션 모델 살펴보기

## 1-1. 텍스트 파운데이션 모델이란?

### 파운데이션 모델의 3가지 구성 요소 in 언어 모델 (Language Model)
- GPT-1, BERT와 같은 언어 모델에도 3가지 구성 요소가 이미 포함되어 있음  
  - 그러나 파운데이션 모델과 같은 능력을 보여주지 못함 → **어떤 차이 때문일까?**

출처: Delvin et al., *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*, NAACL 2019

---

### GPT-2: 추가 학습 없이 새로운 테스크 수행 가능
- 언어 모델이 추가 학습 없이도 텍스트 지시를 통해 새로운 테스크를 “어느 정도” 수행할 수 있음을 확인

출처: Radford et al., *Language Models are Unsupervised Multitask Learners*, OpenAI 2019

## 파운데이션 모델의 3가지 구성 요소 in 언어 모델 (Language Model)
- GPT-2: 언어 모델이 추가 학습 없이도 텍스트 지시를 통해 새로운 테스크를 “어느 정도” 수행할 수 있음을 확인  
  - 가장 큰 GPT-2 모델조차도 *underfitting*된 결과를 보여줌 → **모델 크기를 더 늘렸을 때 성능이 개선될 여지가 있음**

$$
Perplexity = \sqrt[N]{\frac{1}{P(w_1, w_2, \ldots, w_N)}} = \sqrt[N]{\prod_{i=1}^{N} \frac{1}{P(w_i|w_1, w_2, \ldots, w_{i-1})}}
$$

출처: Radford et al., *Language Models are Unsupervised Multitask Learners*, OpenAI 2019

---

## 텍스트 파운데이션 모델(거대 언어 모델)의 특이점

### (1) 규모의 법칙 (Scaling Law)
- 더 많은 데이터, 큰 모델, 긴 학습 → 더 좋은 성능

출처: Kaplan et al., *Scaling Laws for Neural Language Models*, arXiv:20.01

---

### (2) 창발성 (Emergent Property)
- 특정 규모를 넘어서면 갑자기 모델에서 발현되는 성질  
  - **예시 #1. 인-컨텍스트 학습 (In-context Learning)**  
    주어진 설명과 예시만으로 새로운 테스크를 수행  
  - **예시 #2. 추론 (Reasoning)** 능력  

출처: Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020

---

# 1-2. 거대 언어 모델 예시

## 텍스트 파운데이션 모델 (or 거대 언어 모델, LLM)
- 기존 대비  
  1. 더 큰 모델(>7B)  
  2. 더 많은 데이터(>1T)에서 학습되어 창발성이 나타나기 시작한 언어 모델  
- 일반적으로 거대 언어모델은 GPT와 같이 다음 토큰 예측을 통해 많은 텍스트 데이터에서 사전 학습된 트랜스포머 기반 모델을 의미  

| 구분 | 대표 모델 |
|------|------------|
| **폐쇄형 거대언어 모델** | ChatGPT, Claude 3, Gemini |
| **개방형 거대언어 모델** | LLaMA 2, DeepSeek, Mistral AI |

출처: SSAFY 텍스트 파운데이션 모델 슬라이드

---

## 폐쇄형 (Closed) 거대 언어 모델
- 예시: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google)
- **장점:** 일반적으로 더 우수한 성능 및 최신 기능을 갖고 있으며 사용하기 쉬움  
- **단점:**  
  1. 사용 시마다 비용이 발생  
  2. 모델이나 출력에 대한 정보가 제한적으로 제공됨  

출처: https://platform.openai.com/docs/guides/text?lang=python  
https://openai.com/ko-KR/api/pricing/

# 2. 거대 언어 모델의 학습

## GPT-3: “거대 언어 모델의 시초”
- 가장 큰 버전의 GPT-3: **1750억 개의 매개변수(Parameters)**  
  → 이전 언어 모델 대비 최소 10배 이상 큰 모델  
- 본격적으로 **인-컨텍스트 학습(In-context learning)** 능력이 나타나기 시작한 언어 모델

출처: https://medium.com/analytics-vidhya/openai-gpt-3-language-models-are-few-shot-learners-82531b3d3122

---

### 학습 방법 및 비용
- **학습 방법:** 다음 토큰 예측 (Next token prediction)  
- **학습 데이터:** 약 3000억 토큰 (4TB 텍스트 데이터 = 인터넷 + 양질의 텍스트북)  
- **학습 비용:** 약 **150억 원 수준**으로 추산  

#### GPT-3 모델 구성 요약
| Model | Parameters | Layers | Hidden Size | Attention Heads |
|--------|-------------|---------|--------------|----------------|
| GPT-3 Small | 125M | 12 | 768 | 12 |
| GPT-3 Medium | 350M | 24 | 1024 | 16 |
| GPT-3 Large | 760M | 24 | 1536 | 16 |
| GPT-3 XL | 1.3B | 24 | 2048 | 24 |
| GPT-3 2.7B | 2.7B | 32 | 2560 | 32 |
| GPT-3 6.7B | 6.7B | 32 | 4096 | 32 |
| GPT-3 13B | 13.0B | 40 | 5140 | 40 |
| **GPT-3 175B** | **175.0B** | **96** | **12288** | **96** |

#### 학습 데이터 구성
| Dataset | Quantity (Tokens) | 비중(%) |
|----------|------------------|----------|
| Common Crawl (filtered) | 410B | 60 |
| WebText2 | 19B | 22 |
| Books1 | 12B | 8 |
| Books2 | 55B | 8 |
| Wikipedia | 3B | 3 |

출처: Brown et al., *Language Models are Few-Shot Learners*, NeurIPS 2020

---

## 다음 토큰 예측 기반 거대 언어 모델의 한계
- 사람의 지시에 대해 **올바르지 않은 응답**을 생성하거나,  
  **유해한 응답**을 생성할 수 있음.

예시:
- GPT-3: 엉뚱한 내용 생성 (문맥 무관한 문장 나열)
- GPT-4: 유해한 지시에 대해 실행 방법을 제시하는 오류 발생

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022  
Wei et al., *Jailbroken: How Does LLM Safety Training Fail?*, NeurIPS 2023

---

## 정렬(Alignment) 학습
> 거대 언어 모델의 출력이 사용자의 **의도와 가치**를 반영하도록 학습

- (1) **지시 학습 (Instruction tuning)**: 주어진 지시에 대해 어떤 응답이 생성되어야 하는지 학습  
- (2) **선호 학습 (Preference learning)**: 상대적으로 어떤 응답이 더 선호되어야 하는지 학습  

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022  
Wei et al., *Jailbroken*, NeurIPS 2023

---

# 2-1. 지시 학습 (Instruction Tuning)

## 지시 학습의 개념
> 주어진 지시에 대해 어떤 응답이 생성되어야 하는지를 학습

- 학습 방법 자체는 기존 언어 모델 (예: BERT) 에서의 **지도 학습(Supervised Fine-Tuning, SFT)** 과 동일  
- 기존 언어 모델은 각 테스크마다 별도의 **추가 학습 및 모델 저장** 필요

예시:
> “전체적으로, 두 시간 동안 영화를 보는 것에서 얻은 가치는 팝콘과 음료의 합계였습니다. 영화는 정말 끔찍했습니다.”  
→ 출력: **0 (부정적)**

---

## 지시 학습 (Instruction tuning): 주어진 지시에 대해 어떤 응답이 생성되어야 하는지
- **Idea:** 모든 자연어 테스크는 텍스트 기반 지시(instruction)와 응답으로 표현할 수 있지 않을까?

예시:
- 감정 분석: “주어진 리뷰 속 유저의 감정이 긍정적이야, 부정적이야?”
- 번역: “주어진 문장을 영어로 번역해줘.”

입력:  
> 지시: “주어진 리뷰 속 유저의 감정이 긍정적이야, 부정적이야?”  
> 리뷰: “전체적으로, 두 시간 동안 영화를 보는 것에서 얻은 가치는 팝콘과 음료의 합계였습니다. 영화는 정말 끔찍했습니다.”  

출력:  
> “부정적으로 보입니다.”

출처: SSAFY 텍스트 파운데이션 모델 강의 슬라이드

# 2-1. 지시 학습

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 학습 방법: 주어진 입력을 받아서 이에 대한 응답을 따라 하도록 지도 추가 학습 (Supervised Fine-Tuning, SFT)
- (A) Pretrain–finetune (BERT, T5)
  - Typically requires many task-specific examples
  - One specialized model for each task
- (B) Prompting (GPT-3)
  - Improve performance via few-shot prompting or prompt engineering
- (C) Instruction tuning (FLAN)
  - Model learns to perform many tasks via natural language instructions
  - Inference on unseen task
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 학습 데이터의 다양성 증대를 위해, 각 테스크를 다양한 지시(템플릿)로 표현할 수 있음
- Premise  
  `Russian cosmonaut Valery Polyakov set the record for the longest continuous amount of time spent in space, a staggering 438 days, between 1994 and 1995.`
- Hypothesis  
  `Russians hold the record for the longest stay in space.`
- Target  
  `Options: - yes  - no`
- Template 예시
  - Template 1: Based on the paragraph above, can we conclude that `<hypothesis>`?
  - Template 2: Can we infer the following? `<hypothesis>`
  - Template 3: Read the following and determine if the hypothesis can be inferred from the premise  
    Premise: `<premise>`  
    Hypothesis: `<hypothesis>`  
    `<options>`
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 기존 NLP 테스크 데이터를 지시 학습을 위한 데이터로 수정하여 학습 및 테스트에 활용
- 학습시에 보지 못한 지시에 대한 일반화 성능 평가를 위해, 관련 없는 테스크들을 테스트에 별도로 활용
  - 예시: 요약(`summarization`)을 테스트 때의 테스크로 활용하기 위해, 학습 시에는 제거
- 주요 데이터셋
  - Natural language inference (7): ANLI(R1-R3), CB, MNLI, QNLI, RTE, SNLI, WNLI  
  - Commonsense (4): CoPA, HellaSwag, PiQA, StoryCloze  
  - Sentiment (4): IMDB, Sent140, SST-2, Yelp  
  - Paraphrase (4): MRPC, QQP, PAWS, STS-B  
  - Closed-book QA (3): ARC(easy/chal.), NQ, TQA  
  - Struct to text (4): CommonGen, DART, E2ENLG, WEBNLG  
  - Translation (8): ParaCrawl EN/DE, EN/ES, EN/FR, WMT-16 EN/CS, EN/DE, EN/FI, EN/RO, EN/RU, EN/TR  
  - Reading comp. (5): BoolQ, DROP, MultiRC, OBQA, SQuAD  
  - Read. comp. w/ commonsense (2): CosmosQA, ReCoRD  
  - Coreference (3): DPR, Winogrande, WSC273  
  - Misc. (7): CoQA, QuAC, WIC, Math, Fix Punctuation(NLG), TREC, CoLA  
  - Summarization (11): AESLC, AG News, CNN-DM, Gigaword, Multi-News, Newsroom, SamSum, Wiki Lingua EN, XSum, Opin-Abs: iDebate, Opin-Abs: Movie
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 거대 언어 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN)
- 실험 결과: 예시 없이도 (`0-shot`) 새로운 지시에 대해 올바른 응답을 내놓는 성능이 크게 증가!
- `LaMDA-PT 137B`는 구글의 당시 기준 `SOTA` 텍스트 파운데이션 모델을 추가 학습
- 주요 비교 대상: FLAN 137B, LaMDA-PT137B, GPT-3 175B, GLAM 64B/64E, Supervised model
- Natural language inference: ANLI R1-R3, CB, RTE  
- Reading comprehension: MultiRC, OBQA, BoolQ  
- Closed-book QA: NQ, ARC-C, TQA, ARC-e  
- Translation: EN↔RO, EN↔DE, EN↔FR  
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

## 지시 학습: 파운데이션 모델을 다양한 지시 기반 입력과 이에 대한 응답으로 추가학습 (FLAN or T0)
- 실험 결과: 성능 향상을 위한 핵심 요소는 다음과 같음
  1. 학습 테스크의 개수: 다양한 종류의 지시를 학습할수록 보지 못한 지시에 대한 일반화 성능이 좋아짐
  2. 추가 학습하는 모델의 크기: 특정 규모 이하에서는 지시 학습의 효과성이 떨어짐 → 지시를 이해하고 응답하는 것도 창발성의 하나
  3. 지시를 주는 방법: 자연어 지시로 사람에게 대화하듯 지시하는 것이 가장 효과적
- 성능 비교  
  - Held-out clusters: CommonSense / Average NLI / Closed-book QA  
  - FT: instruction / Eval: instruction (FLAN) → `55.2`  
  - FT: dataset name / Eval: instruction → `46.6`  
  - FT: dataset name / Eval: dataset name → `47.0`  
  - FT: no instruction → `37.3`
- 출처: Wei et al., *Finetuned Language Models Are Zero-Shot Learners*, ICLR 2022

# 2-2. 선호 학습 (Preference Learning)

## 지시 학습의 한계: 주어진 입력에 대해 적절한 하나의 응답이 있다고 가정
- 이는 정답이 정해져 있는 객관적 테스트 (e.g. 수학) 에서는 자연스러움  
  - `Question`: 양의 정수 m과 n의 최대공약수는 6이고, 최소공배수는 126이다. 이때 m + n의 가능한 최소값은 얼마인가?  
  - `Answer`: 60
- 출처: Cobbe et al., *Training Verifiers to Solve Math Word Problems*, OpenAI

## 지시 학습의 한계: 주어진 입력에 대해 적절한 하나의 응답이 있다고 가정
- 이는 정답이 정해져 있는 객관적 테스트 (e.g. 수학)에서는 자연스러움
- 그러나, 정답이 정해져 있지 않은 개방형(Open-ended) 테스트 (e.g. 번역)에서는 한계가 있음
  - Goal: 단순히 복수 정답을 허락하는 대신, 더 좋은(선호되는) 응답을 생성하도록 하고 싶음
- 예시 (번역)
  - 입력:  
    `When I am down and, oh my soul, so weary  
    When troubles come and my heart burdened be  
    Then, I am still and wait here in the silence  
    Until you come and still awhile with me`
  - 출력 1:  
    `내가 우울하고, 아, 내 영혼이 너무 지쳤을 때  
    고난이 닥치고 내 마음이 무거워질 때  
    그때, 나는 조용히 기다리며 이 침묵 속에 머물러 있네  
    당신이 오셔서 나와 함께 잠시 머물러 주실 때까지`
  - 출력 2:  
    `내 마음이 지치고 영혼마저 무거울 때  
    근심이 찾아와 가슴이 짓눌릴 때  
    나는 잠잠히 이곳에서 기다리네  
    그대가 와서 잠시 곁에 머물러 주기를`
- 출처: Cobbe et al., *Training Verifiers to Solve Math Word Problems*, OpenAI

## 선호 학습 (Preference Learning)
- 다양한 응답 중 사람이 더 선호하는 응답을 생성하도록 추가학습
- 다양한 응답은 모델이 생성, 응답 간의 선호도는 사람이 제공
- ChatGPT를 만들기 위한 핵심 알고리즘!
  - 공식 문서는 공개되어 있지 않지만, 아래와 같은 힌트가 공식 블로그에 제공되어 있음
- 인용:
```
We trained this model using Reinforcement Learning from Human Feedback (RLHF),
using the same methods as InstructGPT,
but with slight differences in the data collection setup.
We trained an initial model using supervised fine-tuning:
human AI trainers provided conversations in which they played both sides—the user and an AI assistant.
We gave the trainers access to model-written suggestions to help them compose their responses.
We mixed this new dialogue dataset with the InstructGPT dataset,
which we transformed into a dialogue format.
```
- 출처: https://openai.com/index/chatgpt/

# 2-2. 선호 학습

## 선호 학습 (Preference Learning): 다양한 응답 중 사람이 더 선호하는 응답을 생성하도록 추가학습
- InstructGPT의 핵심 아이디어:
  - 사람의 피드백을 통한 강화학습 (Reinforcement Learning from Human Feedback, RLHF)
  - 사람의 피드백 := 응답에 대한 선호도
- Step 1: Collect demonstration data, and train a supervised policy.
- Step 2: Collect comparison data, and train a reward model.
- Step 3: Optimize a policy against the reward model using reinforcement learning.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 1. 지시 학습을 통한 텍스트 파운데이션모델(e.g. GPT-3)의 추가 학습
- 실제 유저로부터 다양한 지시 입력을 수집하고, 해당 입력에 대해 훈련된 사람 주석자들이 정답 데이터를 생성
- Step 1: Collect demonstration data, and train a supervised policy.
  - A prompt is sampled from our prompt dataset.
  - A labeler demonstrates the desired output behavior.
  - This data is used to fine-tune GPT-3 with supervised learning.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 2. 사람의 선호 데이터를 수집하여, 보상 모델(Reward model, RM)을 학습
- 주어진 입력에 대한 선택지는 모델이 생성, 다양한 선택지에 대한 선호도는 사람이 생성
- 사람과 일치한 선호도를 출력할 수 있도록 보상 모델을 지도 학습
  - 사람이 선호하는 응답이 입력으로 주어짐 → 높은 보상을 출력
- Step 2: Collect comparison data, and train a reward model.
  - A prompt and several model outputs are sampled.
  - A labeler ranks the outputs from best to worst.
  - This data is used to train our reward model.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 2. 사람의 선호 데이터를 수집하여, 보상 모델(Reward model, RM)을 학습
- 주어진 입력에 대한 선택지는 모델이 생성, 다양한 선택지에 대한 선호도는 사람이 생성
- 사람과 일치한 선호도를 출력할 수 있도록 보상 모델을 지도 학습
  - 사람이 선호하는 응답이 입력으로 주어짐 → 높은 보상을 출력
- 예시
  - 선택지 A: Explain gravity... → Reward: `-5`
  - 선택지 D: People went to the moon... → Reward: `100`
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 학습 방법: Step 3. 보상이 높은 응답을 생성하도록 강화 학습을 통해 추가 학습
- 핵심: Step 1 & 2에서 보지 못한 질문에 대해 사람의 추가적인 개입 없이 학습된 모델들을 통해 추가 학습이 진행
- 지시 학습된 모델을 보상 모델 기반 강화 학습을 통해 한 번 더 추가 학습
- Step 3: Optimize a policy against the reward model using reinforcement learning.
  - A new prompt is sampled from the dataset.
  - The policy generates an output.
  - The reward model calculates a reward for the output.
  - The reward is used to update the policy using PPO.
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 결과: 유저의 지시를 얼마나 잘 수행하는지를 사람이 직접 평가
- 단순 프롬프팅이나 지시 학습에 비해 발전된 지시 수행능력을 보여줌
  - InstructGPT: Likert score 5점대
  - Supervised Fine-Tuning: 4점대
  - GPT (prompted): 3점대
  - GPT: 2점대
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## InstructGPT의 결과: 얼마나 안전한 응답을 생성하는지 평가
- 기존 대비, InstructGPT는 해로운 응답(RealToxicity)과 거짓말(TruthfulQA, Hallucinations)을 덜 생성
  - RealToxicity  
    GPT: `0.233`  
    SFT: `0.199`  
    InstructGPT: `0.196`
  - TruthfulQA  
    GPT: `0.224`  
    SFT: `0.206`  
    InstructGPT: `0.413`
  - Hallucinations  
    GPT: `0.414`  
    SFT: `0.078`  
    InstructGPT: `0.172`
- 출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, NeurIPS 2022

## LLaMA2
- InstructGPT와 비슷하게 RLHF와 대화 데이터를 활용한 LLaMA2 Chat 모델을 공개
  - LLaMA1 때에는 사전 학습된 모델만 공개
- 구성
  - Human feedback: Human preference data → Helpful & Safety Reward Model 생성
  - Fine-tuning: RLHF, Rejection Sampling, Proximal Policy Optimization
  - Pretraining: Self-supervised learning 기반 LLaMA2 학습
  - 최종 모델: LLaMA-2-chat
- 출처: Touvron et al., *Llama 2: Open Foundation and Fine-Tuned Chat Models*, Meta AI

## LLaMA2
- InstructGPT와 비슷하게 RLHF와 대화 데이터를 활용한 LLaMA2 Chat 모델을 공개
- 당시 대화형 타입 개방형 거대 언어 모델 중 가장 우수한 성능을 보여줌
- 성능 비교 (% Win Rate)
  - LLaMA-2-70b-chat vs ChatGPT-0301 → Win: `35.9`, Tie: `31.5`, Loss: `32.5`
  - LLaMA-2-70b-chat vs PaLM-Bison → Win: `53.0`, Tie: `24.6`, Loss: `22.4`
  - LLaMA-2-34b-chat vs Falcon-40b-instruct → Win: `76.3`, Tie: `14.6`, Loss: `9.1`
  - LLaMA-2-34b-chat vs Vicuna-33b-v1.3 → Win: `37.2`, Tie: `31.2`, Loss: `31.2`
  - LLaMA-2-13b-chat vs Vicuna-13b-v1.1 → Win: `45.4`, Tie: `29.8`, Loss: `24.9`
  - LLaMA-2-7b-chat vs MPT-7b-chat → Win: `61.1`, Tie: `20.9`, Loss: `18.0`
- 출처: Touvron et al., *Llama 2: Open Foundation and Fine-Tuned Chat Models*, Meta AI

# 3. 거대 언어 모델의 추론

# 3-1. 디코딩 (Decoding) 알고리즘

## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- 학습이 완료된 거대 언어 모델은 어떻게 응답을 생성할까? ⇒ 순차적 추론을 통한 “토큰별 생성”

출처 : https://jalammar.github.io/illustrated-transformer/


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Q. 언제 추론 및 토큰 생성을 멈추고 응답을 제공?  
  A. EOS 토큰 생성 시 종료 or 사전에 정의된 토큰 수 도달 시 종료  
  - E.g. `[SEP]`: BERT에서 사용된 EOS (End Of Sentence) 토큰

1. 원문 텍스트 입력  
   ````python
   text = "Tokenizing text is a core task of NLP."
   encoded_text = tokenizer(text)
   ````

2. 토큰 ID 시퀀스  
   ````python
   {'input_ids': [101, 19204, 6026, 3793, 2003, 1037, 4563, 4708, 1997, 17953, 2361, 1012, 102],}
   ````

3. 토큰 문자열 리스트  
   ````python
   ['[CLS]', 'token', '##izing', 'text', 'is', 'a', 'core', 'task', 'of', 'nl', '##p', '.', '[SEP]']
   ````  
   → 문장 종료 표시 (EOS 토큰)

출처 : https://medium.com/@abdallahashraf90x/tokenization-in-nlp-all-you-need-to-know-45c00cfa2df7


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Goal: 주어진 입력 `x = [x₁, ..., x_L]` 에 대해 다음 토큰 `x_{L+1}` 을 생성  
  - Remark. 거대 언어 모델: 입력 `x`에 대해 다음 토큰에 대한 확률 분포 `p̂(x)`를 제공
- 디코딩(Decoding) 알고리즘: `p̂(x)`로부터 `x_{L+1}`을 생성하는 알고리즘 (다음 단어를 선택하는 방법)

`x = [x₁, x₂, x₃] = [아까, 밥, 먹고]`

단어 목록과 확률 예시  
왔군 - 0.06  
왔어 - 0.5  
왔는데 - 0.2  
왔거든 - 0.1

출처 : https://tilnote.io/books/6480b090e92fe5ef635f54df/6480a73ee92fe5ef635f4d77


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Pytorch 실제 예시

````python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

prompt = "Today I believe we can finally"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# generate up to 30 tokens
outputs = model.generate(input_ids, do_sample=False, max_length=30)
tokenizer.batch_decode(outputs, skip_special_tokens=True)
````

자동회귀 생성 파트  
출처 : https://huggingface.co/blog/introducing-csearch


## 거대 언어 모델의 자동회귀 생성 (Auto-regressive Generation)
- Pytorch 실제 예시

디코딩(Decoding) 알고리즘 종류:
- `greedy decoding` by calling `greedy_search()`  
- `contrastive search` by calling `contrastive_search()`  
- `multinomial sampling` by calling `sample()`  
- `beam-search decoding` by calling `beam_search()`  
- `beam-search multinomial sampling` by calling `beam_sample()`  
- `diverse beam-search` by calling `group_beam_search()`  
- `constrained beam-search decoding` by calling `constrained_beam_search()`

출처 : https://docs.pytorch.org/torchtune/0.3/generated/torchtune.generation.generate.html#torchtune.generation.generate


## 디코딩(Decoding) 알고리즘: ① Greedy Decoding
- 핵심 아이디어: 가장 확률이 높은 다음 토큰을 선택  
  - 장점: 사용하기 쉽다.  
  - 단점: 직후만 고려하기 때문에 생성 응답이 최종적으로 최선이 아닐 수 있다.

출처 : https://heidloff.net/article/greedy-beam-sampling/


## 디코딩(Decoding) 알고리즘: ② Beam Search
- 핵심 아이디어: 확률이 높은 k개(beam size)의 후보를 동시에 고려  
  - 고르는 기준: 누적 생성 확률(지금까지 생성된 문장 전체가 나올 확률의 곱)
  - 앞선 Greedy Decoding은 매 시점마다 가장 높은 확률의 선택지 1개만을 선택했지만,  
    Beam Search는 전체 문장 후보들의 누적 확률을 기준으로 상위 k개를 남기는 것

출처 : https://d2l.ai/chapter_recurrent-modern/beam-search.html


## 디코딩(Decoding) 알고리즘: ② Beam Search
- 핵심 아이디어: 확률이 높은 여러 후보를 동시에 고려  
  - 장점: 최종적으로 좋은 응답 생성 확률이 높다.  
  - 단점: 계산 비용이 많이 늘어난다(각 후보마다 LLM 추론을 수행).

예시 계산  
“The dog has” = 0.4 * 0.9 = 0.36  
“The nice woman” = 0.5 * 0.4 = 0.20

Greedy 방식의 경우 매번 가장 높은 확률을 계산해 “The nice woman…” 경로를 선택하지만  
Beam Search의 경우 전체 문장 후보의 누적 확률을 고려하여 “The dog has…” 경로를 선택함.

출처 : https://heidloff.net/article/greedy-beam-sampling/


## 디코딩(Decoding) 알고리즘: ③ Sampling
- 핵심 아이디어: 거대 언어 모델이 제공한 확률을 기준으로 랜덤하게 생성  
  - 장점: 다양한 응답을 생성할 수 있음.  
  - 단점: 생성된 응답의 품질이 감소할 수 있음.

단어 사전에 대해 정의된 확률 분포  
모델이 아는 모든 단어에 대해 ‘다음 단어가 될 확률’을 매겨 놓은 것

출처 : https://huyenchip.com/2024/01/16/sampling.html#constraint_sampling

# 3-1. 디코딩 (Decoding) 알고리즘

## 디코딩(Decoding) 알고리즘: ④ Sampling “with Temperature”
- 핵심 아이디어: 하이퍼 파라미터 `T`를 통해 거대 언어 모델이 생성한 확률 분포를 임의로 조작
  - `T > 1`: 확률 분포를 *Smooth*하게 만듦 (더 다양한 응답 생성)
  - `T < 1`: 확률 분포를 *Sharp*하게 만듦 (기존에 확률이 높은 응답에 집중)

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71

- `T < 1`: 확률 분포를 *Sharp*하게 만듦 (기존에 확률이 높은 응답에 집중)
  - 특정 후보(예: 9번 그래프)가 압도적으로 높은 확률을 갖고, 나머지는 매우 낮음
  - → 모델이 항상 비슷한 답(가장 높은 확률의 단어)만 내놓게 됨
  - * 안정적이나 다양성이 떨어짐

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71

- `T > 1`: 확률 분포를 *Smooth*하게 만듦 (더 다양한 응답 생성)
  - 분포가 평평해짐
  - 모든 단어가 거의 비슷한 확률로 선택될 수 있음.
  - → 모델이 예측할 때 다양성이 극대화되지만, 품질은 불안정해짐.
  - * 창의적이나 품질이 떨어질 수 있음.

출처 : https://medium.com/@harshit158/softmax-temperature-5492e4007f71


## 디코딩(Decoding) 알고리즘: ⑤ Top-K Sampling
- 핵심 아이디어: 확률이 높은 `K`개의 토큰들 중에서만 랜덤하게 확률에 따라 샘플링
  - 장점: 품질이 낮은 응답을 생성할 가능성을 줄일 수 있음

출처 : https://sooftware.io/generate/

- 단점: 확률 분포의 모양에 상관 없이 고정된 `K`개의 후보군을 고려

출처 : https://sooftware.io/generate/

- 문맥에 따라 다음 단어의 예측 확률 합이 다르다.
  - `Σ_{w ∈ V_top-K} P(w | “The”) = 0.68`
  - `Σ_{w ∈ V_top-K} P(w | “The”, “car”) = 0.99`

출처 : https://sooftware.io/generate/


## 디코딩(Decoding) 알고리즘: ⑥ Top-P Sampling (or Nucleus Sampling)
- 핵심 아이디어: `K`를 고정하는 대신, 누적 확률(`P`)에 집중하여 `K`를 자동으로 조절
  - 예시: `P = 0.9` → 확률이 높은 응답 후보의 확률을 더했을 때 `0.9`를 처음으로 초과하는 `K`를 사용

출처 : https://sooftware.io/generate/

- 핵심 아이디어: `K`를 고정하는 대신, 누적 확률(`P`)에 집중하여 `K`를 자동으로 조절
- 다양한 평가 지표에서 기존 디코딩 알고리즘들 대비 좋은 성능을 달성

출처 : Holtzman et al., The Curious Case of Neural Text Degeneration., ICLR 2020


## 디코딩(Decoding) 알고리즘 별 장단점 요약
- Greedy Decoding
  - 장점: 쉬운 사용법
  - 단점: 최적해 보장 `X`
- Beam Search
  - 장점: 좋은 응답 생성 확률 ↑
  - 단점: 큰 계산 비용
- Sampling
  - 장점: 다양한 응답 생성 가능
  - 단점: 품질 불안정
- Sampling with “Temperature”
  - 장점: 창의성/안정성 조절 가능
  - 단점: `T ↑` : 품질 저하 / `T ↓` : 다양성 부족
- Top-K Sampling
  - 장점: 잡음 단어 배제, 품질 향상
  - 단점: `K`값 고정 → 문맥 따라 불균형
- Top-P Sampling (Nucleus)
  - 장점: 확률 누적 기준, 품질·다양성 균형
  - 단점: `P`값 설정 필요 (경우에 따라 랜덤성 여전)

<표3-1_텍스트 파운데이션 모델_거대 언어 모델의 추론_디코딩 알고리즘 별 장단점 요약>

# 3-1. 디코딩(Decoding) 알고리즘
## 디코딩(Decoding) 알고리즘: 실제 예시 with ChatGPT
- **OpenAI Playground / 모델 설정창**
  - 이 값들을 조정하면서 앞서 나온 디코딩 알고리즘 값을 간접적으로 제어할 수 있음.

*출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20*  
<그림3-13_텍스트 파운데이션 모델_거대 언어 모델의 추론_ChatGPT에서 실제로 활용되고 있는 디코딩 알고리즘 및 효과 예시>

---

# 3-2. 프롬프트 엔지니어링
## 입력 프롬프트 = (1) 지시(instruction) + (2) 예시(few-shot examples)
- **지시 (Instruction)**
- **예시 (few-shot examples)**
  - 모델은 학습을 새로 하지 않고 프롬프트 안의 예시를 보고 패턴을 따라 함.

*출처: Brown et al., Language Models are Few-Shot Learners., NeurIPS 2020*  
<그림3-14_텍스트 파운데이션 모델_거대 언어 모델의 추론_인 컨텍스트 학습 (or 퓨샷 프롬프팅) 예시>

---

## 입력 프롬프트의 영향
- 어떻게 지시를 주는지, 어떤 예시를 보여주는지가 거대 언어 모델의 성능에 크게 영향을 미침
- **프롬프트 엔지니어링**: 원하는 답을 얻기 위해 모델에 주어지는 입력(프롬프트)을 설계·조정하는 기법

*출처: Brown et al., Language Models are Few-Shot Learners., NeurIPS 2020*  
<그림3-15_텍스트 파운데이션 모델_프롬프트 엔지니어링_프롬프트에 따른 ChatGPT의 응답 차이>

---

## 프롬프트 엔지니어링: 지시(instruction)
- 감정 분류와 같은 쉬운 문제뿐 아니라 수학, 코딩과 같은 어려운 문제를 거대 언어 모델로 푸는 것에 많은 관심 집중
  - 예시: 수학 질의 응답 (GSM8K → 미국 초등학교 고학년 수준 수학 문제)
    - **질문:** Josh는 쿠키 한 상자를 사려고 돈을 모으고 있어요. 돈을 벌기 위해 팔찌를 만들어 팔기로 했습니다. 팔찌 하나를 만들 때 재료비로 \$1이 들고, 팔찌는 하나당 \$1.5에 판매합니다. Josh가 팔찌를 12개 만들고 쿠키를 산 뒤에도 \$3가 남아있다면, 쿠키 한 상자의 가격은 얼마일까요?
    - **정답:** Josh는 팔찌 하나당 \$1.5 - \$1 = \$0.5의 이익을 얻습니다. Josh가 팔찌를 12개 만들면, 총 이익은 12 * \$0.5 = \$6입니다. 쿠키를 산 뒤에도 \$3가 남아 있으므로, Josh는 \$6 - \$3 = \$3을 쿠키 한 상자에 썼습니다. 따라서 쿠키 한 상자의 가격은 \$3입니다. 정답은 \$3입니다.

*출처: https://huggingface.co/datasets/openai/gsm8k*  
<그림3-16_텍스트 파운데이션 모델_프롬프트 엔지니어링_GSM8K 수학 문제 예시와 거대 언어 모델의 생성한 풀이 예시>

---

## 프롬프트 엔지니어링: 성능 비교
- 감정 분류와 같은 쉬운 문제뿐 아니라 수학, 코딩과 같은 어려운 문제를 거대 언어 모델로 푸는 것에 많은 관심 집중
  - Claude 3, GPT-4, Gemini 등 최신 모델들의 벤치마크 비교 (Grade School Math, MATH 등)

*출처: https://www.anthropic.com/news/claude-3-family*  
<그림3-17_텍스트 파운데이션 모델_프롬프트 엔지니어링_다양한 벤치마크에서의 최신 SOTA 거대 언어 모델들 간의 성능 비교>

---

## Chain-of-Thought (CoT) 프롬프팅
- **아이디어:** 단순히 질문과 응답만을 예시로 활용하는 것이 아니라, **추론(Reasoning)** 과정도 예시에 포함
  - 이를 통해 테스트 질문에 대해 추론을 생성하고 응답하도록 유도함으로써, 더 정확한 정답 생성을 기대할 수 있음
  - 질문에 대한 정답을 바로 제시 → 틀림
  - 질문에 대한 정답이 나오는 추론 과정을 함께 제시 → 정답률 상승

*출처: Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Model., NeurIPS 2022*  
<그림3-18_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 추론 기반 응답 예시>

---

## CoT 프롬프팅의 효과
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴
  - *PaLM*: 당시 구글에서 사용했던 가장 큰 거대 언어 모델 (PaLM 540B vs. GPT-3 175B)
- **CoT로 인한 성능 향상은 모델 크기가 커질수록 더 확대됨**  
  (추론 ~= 창발성?)
  - *창발성:* 모델 크기가 커지면 갑자기 새로운 능력이 나타나는 현상을 의미  
    (*PaLM의 창발적 능력이 발현되었을 수 있음*)

*출처: Wei et al., Chain-of-Thought Prompting Elicits Reasoning in Large Language Model., NeurIPS 2022*  
<그림3-19_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 복잡한 추론 테스크에 대한 성능 향상 예시: GSM8K>

# 3-2. 프롬프트 엔지니어링
## Chain-of-Thought (CoT) 프롬프팅
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴  
- **다른 추론 테스크:** 마지막 단어 연결  
  - In-domain: 예시도 2 단어, 테스트도 2 단어  
  - Out-of-domain: 예시는 2 단어, 테스트는 4 단어  
  - 마지막 글자 이어붙이기 문제 → 단계적 추론이 필요함

<그림3-20_텍스트 파운데이션 모델_프롬프트 엔지니어링_CoT 프롬프팅을 통한 복잡한 추론 테스크에 대한 성능 향상 예시: 마지막 단어 연결>  
출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- **결과:** CoT는 거대 언어 모델(PaLM)의 추론 성능을 크게 증가시킴  
- **다른 추론 테스크:** 마지막 단어 연결  
  - In-domain: 예시도 2 단어, 테스트도 2 단어  
  - Out-of-domain: 예시는 2 단어, 테스트는 4 단어  

- **2 letters**
  - 두 모델 다 꾸준히 증가  
  - 모델 크기가 클수록 성능이 좋아짐  
- **4 letters**
  - 학습 예시와 다른 일반화된 문제(out of domain)  
  - CoT를 썼을 때 향상됨

➡ CoT는 추론 테스크에서 성능을 크게 높일 뿐 아니라 훈련에 없던 더 어려운 문제도 효과적으로 대응할 수 있게 함

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- 예시 기반 CoT는 강력하지만, 예시를 위한 추론 과정을 수집해야 하는 문제가 있음  
- **Q. 예시 없이도(0-shot) 거대 언어 모델의 추론 성능을 강화할 수 있을까? (i.e., 0-shot CoT)**  
  - 단계별 사고 과정을 예시로 제공하여 LLM의 추론 능력을 향상시킴

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## Chain-of-Thought (CoT) 프롬프팅
- 예시 기반 CoT는 강력하지만, 예시를 위한 추론 과정을 수집해야 하는 문제가 있음  
- **Q. 예시 없이도(0-shot) 거대 언어 모델의 추론 성능을 강화할 수 있을까? (i.e., 0-shot CoT)**  
  - “Let’s think step by step.”이라는 문구 추가로 예시 없이 LLM 성능 향상

출처: Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Model.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **1. 유인 문장을 통한 추론 생성** (e.g. “Let’s think step by step”)

<그림3-22_텍스트 파운데이션 모델_거대 언어 모델의 추론_0-shot CoT 프롬프팅 개요도>  
출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **1. 추론 문장을 통한 추론 생성** (e.g. “Let’s think step by step”)  
- **2. 주어진 질문과 생성된 추론을 통한 정답 생성** (e.g. “Therefore, the answer is”)

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **결과:** 0-shot CoT는 기존 0-shot 프롬프팅보다 훨씬 높은 추론 성능을 달성  
- 또한, 0-shot CoT는 모델 크기가 임계점을 넘어서야 효과성이 발휘됨  
  - 따라서, 추론 능력은 거대 언어 모델의 창발성 결과라고 볼 수 있음

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

## 0-shot CoT 프롬프팅
- **Q. 추론 문장의 중요성?**
  - 단순한 문구 하나가 성능을 크게 향상시킴
  - 적절하지 못한 문구를 제시했을 때 성능을 떨어뜨리거나 역효과가 남

출처: Kozima et al., *Large Language Models are Zero-Shot Reasoners.*, NeurIPS 2022

---

# 4. 거대 언어 모델의 평가와 응용

---

# 4-1. 거대 언어 모델의 평가

## 평가 (Evaluation): 구축한 시스템(e.g. 코드 or 앱)이 실제로 잘 동작하는지를 확인하는 단계

- 평가의 3가지 요소
  1) 목표: 시스템으로 무엇을 달성하고자 하는지  
  2) 평가 방법: 어떤 방법으로 평가할 것인지  
  3) 평가 지표: 어떻게 성공 여부를 판단할 것인지

> 출처: https://www.ytn.co.kr/_ln/0102_202404130800061445

- 예시: 배달 어플
  1) 목표: 음식을 음식점으로부터 유저에게까지 배달하는 것  
  2) 평가 방법: 배달 시간을 측정  
  3) 평가 지표: 전체 유저 배달 건수에 대한 평균 배달 시간

> 출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20

## AI 모델의 평가: “테스트 데이터”

- 핵심 가정: 학습 단계에서 본 적이 없고, 질문과 정답을 알고 있음
- 예시: 감정 분류  
  1) 목표: 주어진 입력 텍스트의 감정을 올바르게 예측하는 것  
  2) 평가 방법: AI 모델의 예측 감정과 사람이 작성한 정답을 비교하는 것  
  3) 평가 지표: 테스트 데이터 셋에서의 평균 정확도  

“총평하자면, 두 시간 동안 영화를 보고 얻은 건 팝콘과 음료 뿐입니다. 영화는 정말 형편없었어요.”

데이터 입력 → 추가 학습된 언어 모델 → 예측과 정답 비교  
예측 감정: 0 (부정적) = 정답 감정: 0 (부정적)

<그림 4-1. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_AI 모델의 테스트 데이터 기반 평가 예시>

출처: Delvin et al., BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding, NAACL 2019

## 거대 언어 모델 평가의 특징

- 특정 테스트에서 학습된 기존 AI 모델들과 달리, 거대 언어 모델은 다양한 테스트에 대해 동시에 학습됨  
  - 따라서, 거대 언어 모델의 성능을 올바르게 평가하기 위해서는 많은 테스트에서의 성능을 종합적으로 판단해야 함  
  - 또한, 디코딩 알고리즘, 입력 프롬프트에 따라 같은 질문에 대해서도 예측이 바뀌므로, 공평한 비교를 위해서는 해당 부분도 고려해야 함

<그림 4-2. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델간의 성능 비교 예시>

출처: OpenAI, GPT-4 Technical Report

- 특정 테스트에서 학습된 기존 AI 모델들과 달리, 거대 언어 모델은 다양한 테스트에 대해 동시에 학습됨  
  - 따라서, 거대 언어 모델의 성능을 올바르게 평가하기 위해서는 많은 테스트에서의 성능을 종합적으로 판단해야 함  
  - 또한, 디코딩 알고리즘, 입력 프롬프트에 따라 같은 질문에 대해서도 예측이 바뀌므로, 공평한 비교를 위해서는 해당 부분도 고려해야 함

<그림 4-2. 텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델간의 성능 비교 예시>

출처: OpenAI, GPT-4 Technical Report

# 4-1. 거대 언어 모델의 평가

## 정답이 정해져 있는 경우
- 예측과 정답을 비교하여 일치도를 측정 → “정확도 (Accuracy)”
  - 예시: MMLU (Massive Multitask Language Understanding) 벤치마크 → 57개의 다양한 전문 분야에 대한 객관식 문제들로 구성

<그림4-3_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_MMLU 벤치마크 문제 예시>

출처: Hendrycks et al., Measuring Massive Multitask Language Understanding, ICLR 2021

---

## 거대 언어 모델 평가 방법의 종류
- 정답이 정해진 경우
  - 평가 방법: 예측과 정답을 비교하여 일치도를 측정(정확도 Accuracy)
- 정답이 정해져 있지 않은 경우
  - 평가 방법 #1: 사람이 임의의 정답을 작성 및 이와 예측을 비교
  - 평가 방법 #2: 정답과 무관하게 생성 텍스트 자체의 품질만을 측정
  - 평가 방법 #3: 생성된 텍스트의 “상대적 선호”를 평가

출처: OpenAI, GPT-4 Technical Report

---

## 거대 언어 모델 평가의 특징
- 특정 테스크에서 학습된 기존 AI 모델들과 달리, 거대 언어 모델은 다양한 테스크에 대해 동시 학습됨  
  - 따라서, 거대 언어 모델의 성능을 올바르게 평가하기 위해서는 많은 테스크에서의 성능을 종합적으로 판단해야 함  
  - 또한, 디코딩 알고리즘, 입력 프롬프트에 따라 같은 질문에 대해서도 예측이 바뀌므로, 공평한 비교를 위해서는 해당 부분도 고려해야 함

<그림4-2_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델간의 성능 비교 예시>

출처: OpenAI, GPT-4 Technical Report

---

## 정답이 정해져 있지 않은 경우
- 예시 1: 문서 요약  
  해리포터 1권 내용을 5문장으로 요약해줘  
  응답 1: Gemini  
  응답 2: ChatGPT  

<그림4-4_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_정답이 정해져 있지 않은 테스크(문서 요약)에서의 거대 언어 모델 활용 예시>

출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20

- 예시 2: 문서 요약, 스토리 생성  

2008년 이후 서호주 해안에서 서식 중인 어린 고래의 개체수가 전례 없이 많이 감소하였습니다.  
응답 1: 이는 무분별한 남획 때문으로 여겨지며, 이를 방지하기 위해 호주 정부는 강력한 법안을 새로이 추진 중에 있습니다.  
응답 2: 지구 온난화로 인해 서호주 해안의 플랑크톤 수가 줄어들면서 영양 부족으로 인해 기인한 결과라고 수의학 연구자들이 밝혔습니다.  

<그림4-5_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_정답이 정해져 있지 않은 테스크(스토리 생성)에서의 거대 언어 모델 활용 예시>

출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20

- 평가 방법 #1: 사람이 임의의 정답을 작성 및 이와 예측을 비교
  - Q. 어떻게 두 텍스트 간의 유사도를 측정할 수 있을까?

<그림4-6_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_정답이 정해져 있지 않은 테스크(문서 요약)에서의 정답 기반 평가 예시>

출처: https://platform.openai.com/chat/edit?models=gpt-4o-2024-11-20

---

- 평가 방법 #1: 사람이 임의의 정답을 작성 및 이와 예측을 비교  
  - Q. 어떻게 두 텍스트 간의 유사도를 측정할 수 있을까?  
  - A. 예시1) 단어 수준에서의 유사도 측정 (e.g. ROUGE)

Reference: “The cat sat on the mat.”  
Generated: “The cat lay on the mat.”  

ROUGE-1 (unigrams): Overlap = {“The”, “cat”, “on”, “the”, “mat”} = 5/6 = 0.83  

<그림4-7_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_단어 수준에서의 유사도 측정(ROUGE 예시)>

출처: Narayan et al., Don’t Give Me the Details, Just the Summary! Topic-Aware Convolutional Neural Networks for Extreme Summarization., EMNLP 2018

---

- 평가 방법 #1: 사람이 임의의 정답을 작성 및 이와 예측을 비교  
  - Q. 어떻게 두 텍스트 간의 유사도를 측정할 수 있을까?  
  - A. 방법1) 단어 수준의 유사도 측정 (e.g. ROUGE)  
  - A. 방법2) 벡터 공간에서의 유사도 측정 (e.g. cosine similarity on embedding space)

예시2) 벡터 공간에서의 유사도 측정

```
cosine-sim(u, v)
u → pooling → BERT → Sentence A
v → pooling → BERT → Sentence B
```

- 각 문장 입력  
- BERT를 통해 문장 내 단어들 벡터 변환  
- 단어별 벡터를 하나의 문장 벡터로 변환  
- 각 문장의 벡터 추출  
- 코사인 유사도 계산 (-1 … 0 … 1)

<그림4-8_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_벡터 공간에서의 유사도 측정을 위한 인코더 학습 개요도(Sentence-BERT)>

출처: Reimers and Gurevych, Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks, EMNLP 2019

- 평가 방법 #2: 정답과 무관하게 생성 텍스트 자체의 품질만을 측정  
  - 예시: Perplexity (PPL) → 얼마나 문장이 확률적으로 자연스러운지 측정  
  - 다음 단어가 올 확률을 계산하기 위해 언어모델을 주로 활용 (예: GPT-2)

```
PPL(X) = exp{-1/t ∑ log pθ(xᵢ | x₍₍ᵢ₎₎)}
```

Hugging Face is a startup based in New York City and Paris  
p(word)

<그림4-9_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_Perplexity 수식 및 계산 예시>

출처: https://huggingface.co/docs/transformers/perplexity

# 4-1. 거대 언어 모델의 평가

## 정답이 정해져 있지 않은 경우
- 단순한 등장 확률이 아니라, 여러가지 측면에서 평가를 하고 싶다면?  
  - 예: 창의성, 유창성, 가독성 등 → 각각에 부합하는 평가 지표를 따로 설계하는 것은 굉장히 어려움  
  - 기존 해결 방법: 전문가를 고용하여 평가를 맡김  
  → 거대 언어 모델로 해당 역할을 대신 수행하게 하면 안될까?

---

## 거대 언어 모델을 활용한 평가
- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트를 평가
  1. 유저는 다음과 같은 정보를 제공: (1) 풀고자 하는 테스크 (e.g. 질문) (2) 평가하고자 하는 텍스트 (3) 평가 기준을 제공  

```
User Input

Task Introduction  
You will be given one summary written for a news article. Your task is to rate the summary on one metric ……

Evaluation Criteria  
Coherence (1–5) – the collective quality of all sentences. We align this dimension with the DUC quality question of structure and coherence ……
```

<그림4-10_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 평가자로 활용하는 LLM-as-judge 프레임워크 예시>

출처: Liu et al., *G-EVAL: NLG Evaluation using GPT-4 with Better Human Alignment.*, EMNLP 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트를 평가
  1. 유저는 다음과 같은 정보를 제공: (1) 풀고자 하는 테스크 (e.g. 질문) (2) 평가하고자 하는 텍스트 (3) 평가 기준을 제공  
  2. 거대 언어 모델은 평가 결과(점수, 이유)를 제공  

```
User Input
Task Introduction  
You will be given one summary written for a news article. Your task is to rate the summary on one metric ……

Evaluation Criteria  
Coherence (1–5) – the collective quality of all sentences. We align this dimension with the DUC quality question of structure and coherence ……

Input Context  
Article: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team’s 0-0 draw with Burnley on ……

Input Target  
Summary: Paul Merson was brought on with only seven minutes remaining in his team’s 0-0 draw with Burnley ……

Evaluation Form (scores ONLY):  
- Coherence:  

G-Eval → Weighted Summed Score: 2.59
```

<그림4-10_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 평가자로 활용하는 LLM-as-judge 프레임워크 예시>

출처: Liu et al., *G-EVAL: NLG Evaluation using GPT-4 with Better Human Alignment.*, EMNLP 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트를 평가  
- GPT-4를 활용한 평가는 기존 평가 지표(e.g. ROUGE)보다 더 사람과 유사한 결과를 보임  

| Metrics | Coherence | Consistency | Fluency | Relevance | AVG |
|----------|------------|-------------|----------|------------|------|
| ROUGE-1 | 0.167 / 0.126 | 0.160 / 0.130 | 0.115 / 0.094 | 0.326 / 0.252 | 0.192 / 0.150 |
| ROUGE-2 | 0.184 / 0.139 | 0.187 / 0.155 | 0.159 / 0.128 | 0.290 / 0.219 | 0.205 / 0.161 |
| ROUGE-L | 0.128 / 0.099 | 0.115 / 0.092 | 0.105 / 0.084 | 0.311 / 0.237 | 0.165 / 0.128 |
| BERTScore | 0.284 / 0.211 | 0.190 / 0.150 | 0.193 / 0.158 | 0.312 / 0.243 | 0.225 / 0.175 |
| MOVERScore | 0.159 / 0.118 | 0.157 / 0.127 | 0.129 / 0.105 | 0.318 / 0.244 | 0.191 / 0.148 |
| BARTScore | 0.448 / 0.342 | 0.383 / 0.310 | 0.346 / 0.273 | 0.385 / 0.305 | — |
| UniEval | 0.575 / 0.452 | 0.446 / 0.371 | 0.474 / 0.377 | — | — |
| GPTScore | 0.434 / — | 0.449 / — | — | 0.417 / — | — |
| **G-EVAL-4** | **0.582 / 0.457** | **0.507 / 0.425** | **0.506 / 0.455** | **0.547 / 0.433** | **0.514 / 0.418** |

<그림4-11_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 평가자료로 활용하는 LLM-as-judge 프레임워크의 효과성>

출처: Liu et al., *G-EVAL: NLG Evaluation using GPT-4 with Better Human Alignment.*, EMNLP 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트를 평가  
- GPT-4를 활용한 평가는 기존 평가 지표(e.g. ROUGE)보다 더 사람과 유사한 결과를 보임  
- **LLaMA3 학습을 위한 데이터 필터링에도 사용되는 등 다양한 어플리케이션에서 이미 활용되고 있음**

```
Model-based quality filtering.  
Further, we experiment with applying various model-based quality classifiers to sub-select high-quality tokens.  
These include using fast classifiers such as fasttext (Joulin et al., 2017) trained to recognize if a given text would be referenced by Wikipedia (Touvron et al., 2023a), as well as more compute-intensive Roberta-based classifiers (Liu et al., 2019a) trained on Llama 2 predictions.  
To train a quality classifier based on Llama 2, we create a training set of cleaned web documents, describe the quality requirements, and instruct Llama 2’s chat model to determine if the documents meet these requirements.  
We use DistilRoberta (Sanh et al., 2019) to generate quality scores for each document for efficiency reasons.  
We experimentally evaluate the efficacy of various quality filtering configurations.
```

<그림4-12_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 학습 데이터 필터링을 위한 LLM-as-judge의 활용 예시 in LLaMA3>

출처: Grattafiori et al., *The Llama 3 Herd of Models.*, arXiv:24.07

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트를 평가  
- GPT-4를 활용한 평가는 기존 평가 지표(e.g. ROUGE)보다 더 사람과 유사한 결과를 보임  
- **LLaMA3 학습을 위한 데이터 필터링에도 사용되는 등 다양한 어플리케이션에서 이미 활용되고 있음**

```
Below is an extract from a web page. Evaluate whether the page has a high educational value and could be useful in an educational setting for teaching from primary school to grade school levels using the additive 5-point scoring system described below.  
Points are accumulated based on the satisfaction of each criterion:

- Add 1 point if the extract provides some basic information relevant to educational topics, even if it includes some irrelevant or non-academic content like advertisement or promotional material.  
- Add another point if the extract addresses certain elements pertinent to education but does not align closely with educational standards.  
- Award a third point if the extract is appropriate for educational use and introduces key concepts relevant to school curricula.  
- Grant a fourth point if the extract is relatively relevant and beneficial for educational purposes for a level higher than grade school, exhibiting clear and consistent writing style.  
- Bestow a fifth point if the extract is outstanding in its educational value, perfectly suited for teaching either at primary school or grade school.

The extract: <extract>

After examining the extract:  
- Briefly justify your total score, up to 100 words.  
- Conclude with the score summary format: “Educational score: <total points>”.
```

<그림4-13_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 학습 데이터 필터링을 위한 LLM-as-judge 프롬프트 예시>

출처: Penedo et al., *The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale.*, arXiv:24.06 (Huggingface)

---

## 정답이 정해져 있지 않은 경우
- 평가 방법 #3: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  

```
Explain the moon landing to a 6 year old
→ 모델 생성 응답 후보  
→ 사람 주석 선호도 평가 (D > C > A = B)
```

<그림4-14_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_선호 판단을 통한 평가 예시>

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback.*, NeurIPS 2022

- 평가 방법 #3: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 대표 예시: **LMArena**  
  - 실제 유저 피드백을 활용하였으며, 거대 언어 모델 성능 측정 방법 중 가장 신뢰성 있는 방법 중 하나로 여겨짐

```
안녕하세요! 오늘은 Google의 최신 플래그십 모델, Gemini 2.5 Pro-Exp에 대해 알아보겠습니다.  
Gemini 2.5 Pro-Exp는 기존 Gemini 1.5 Pro 모델 대비 언어 이해, 멀티모달 처리, 코드 작성, 추론 능력에서 더욱 향상된 성능으로 **LMArena 리더보드 1위를 차지**하였으며,  
특히 긴 컨텍스트 처리와 복잡한 문제 해결 능력이 강화된 점이 주목받고 있습니다.
```

<그림4-15_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_Gemini 2.5 Pro 평가에서의 LMArena 언급 예시>

출처: https://fornewchallenge.tistory.com/entry/

- 평가 방법 #3: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 대표 예시: **LMArena**
  - 실제 유저 피드백을 활용하였으며, 거대 언어 모델 성능 측정 방법 중 가장 신뢰성 있는 방법 중 하나로 여겨짐  

```
LMArena 인터페이스 예시 (메인 페이지)
Model A vs Model B 비교화면
```

<그림4-16_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_LM Arena 메인 페이지>

출처: https://lmarena.ai/

# 4-1. 거대 언어 모델의 평가

## 거대 언어 모델을 활용한 평가
- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음 → 이를 인지하고 보완하여 활용하는 것이 필요  
  - **위치 편향**은 순서를 바꿔서 두 번 평가하고 평균을 취하는 것으로 해결할 수 있음  

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023 (Dataset and Benchmark Track)

---

## 정답이 정해져 있지 않은 경우
- **평가 방법 #3**: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- **대표 예시: LMArena**  
  - 실제 유저 피드백을 활용하였으며, 거대 언어 모델 성능 측정 방법 중 가장 신뢰성 있는 방법 중 하나로 여겨짐  

<그림4-16_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_LM Arena 모델 대결 결과>

출처: https://lmarena.ai/

- **평가 방법 #3**: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- **대표 예시: LMArena**  
  - 실제 유저 피드백을 활용하였으며, 거대 언어 모델 성능 측정 방법 중 가장 신뢰성 있는 방법 중 하나로 여겨짐  

<그림4-16_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_LM Arena 모델별 스코어 보드>

출처: https://lmarena.ai/

- **평가 방법 #3**: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- **대표 예시: LMArena → 그러나 높은 평가 비용 및 시간을 필요로 함**

```
Explain the moon landing to a 6 year old
→ 모델 생성 응답 후보
→ 사람 주석 선호도 평가 (D > C > A = B)
```

<그림4-14_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_선호 판단을 통한 평가 예시>

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback.*, NeurIPS 2022

- **평가 방법 #3**: 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- **대표 예시: LMArena → 그러나 높은 평가 비용 및 시간을 필요로 함 → 거대 언어 모델로 대체한다면?**

```
Explain the moon landing to a 6 year old  
→ 모델 생성 응답 후보  
→ 거대 언어 모델이 생성 선호도 평가 (D > C > A = B)
```

<그림4-17_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단을 통한 평가 예시>

출처: Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback.*, NeurIPS 2022

---

## 거대 언어 모델을 활용한 평가
- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  

```
[System]  
Please act as an impartial judge and evaluate the quality of the responses provided by two AI assistants to the user question displayed below. You should choose the assistant that follows the user’s instructions and answers the user’s question better.  
Your evaluation should consider factors such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of their responses.  
Begin your evaluation by comparing the two responses and provide a short explanation. Avoid any position biases and ensure that the order in which the responses were presented does not influence your decision.  
After providing your explanation, output your final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie.

[User Question]  
{question}

[The Start of Assistant A’s Answer]  
{answer_a}  
[The End of Assistant A’s Answer]

[The Start of Assistant B’s Answer]  
{answer_b}  
[The End of Assistant B’s Answer]
```

공정한 심사위원 역할을 맡아,  
아래에 제시된 사용자 질문에 대해 두 AI 어시스턴트가 제공한 답변의 품질을 평가하세요.  

<그림4-18_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단을 위한 프롬프트 예시>

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023 (Dataset and Benchmark Track)

---

## 거대 언어 모델을 활용한 평가
- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음  

1. **위치 편향**: 특정 위치의 응답을 상대적으로 선호  
   (예: 첫 번째 응답 > 두 번째 응답)  

```
GPT-4 Judgment (when A is placed in the first position):  
However, Assistant A’s answer is more detailed and organized...

GPT-4 Judgment (when B is placed in the first position):  
However, Assistant B’s answer is more detailed and covers a wider range of topics...
```

A를 첫 번째 응답으로 제시 → A의 답변이 더 상세하고 잘 정리되어 있음  
B를 첫 번째 응답으로 제시 → B의 답변이 더 상세하고 더 넓은 주제를 다룸  

<그림4-19_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단의 한계: 1. 위치 편향>

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음  

1. **위치 편향**: 특정 위치의 응답을 상대적으로 선호  
2. **길이 편향**: 품질과 무관하게 길이가 긴 응답을 상대적으로 선호  

Assistant A: 같은 내용을 반복하면서 중복된 내용이 포함된 긴 답변  
Assistant B: 중복 없이 필요한 정보만 제시한 짧은 답변  

<그림4-20_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단의 한계: 2. 길이 편향>

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음  

1. 위치 편향  
2. 길이 편향  

```
GPT-3.5 Judgment:  
Assistant A provides a more detailed and accurate response to the user’s question.

Claude-v1 Judgment:  
Assistant A provides a more in-depth and detailed explanation by briefly rephrasing and elaborating.

GPT-4 Judgment:  
Assistant B’s answer is more concise and avoids redundancy.
```

GPT 3.5 평가 → A는 더 상세하고 정확한 답변  
Claude-v1 평가 → A는 더 깊이 있는 설명  
GPT 4 평가 → A는 중복이 있어 B가 더 낫다고 판단  

<그림4-20_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단의 한계: 2. 길이 편향>

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음  

1. 위치 편향  
2. 길이 편향  
3. **자기 선호 편향**: 생성 모델이 평가 모델과 같은 경우 이를 선호  

<그림4-21_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단의 한계: 3. 자기 선호 편향>

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023

- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음 → 이를 인지하고 보완하여 활용하는 것이 필요  
  - 위치 편향은 순서를 바꿔 두 번 평가하고 평균을 취하는 것으로 해결할 수 있음  

출처: Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*, NeurIPS 2023 (Dataset and Benchmark Track)

# 4-2. 거대 언어 모델의 응용 및 한계

## 거대 언어 모델의 응용: 합성 데이터 생성
- **Self-instruct**: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52,000개의 합성 데이터 생성  
- **필터링 의의**  
  - 합성 데이터에서 중복·유사(유사도 높은) 데이터 제거  
  - 모델이 더 폭넓은 지시문 학습이 가능하도록 다양한 Instruction 확보  

```
노이즈 제거(유사도 낮음) / 중복 제거(유사도 높음)
ROUGE-L Overlap with the Most Similar Seed Instruction
```

<그림4-28_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 통한 합성 데이터 생성 프레임워크 예시: Self-Instruct>

출처: Wang et al., *Self-Instruct: Aligning Language Models with Self-Generated Instructions.*, ACL 2023

---

## 거대 언어 모델을 활용한 평가
- **LLM-as-judge (or G-Eval)**: 거대 언어 모델을 통해 생성 텍스트의 “상대적 선호”를 평가할 수도 있음  
- 그러나, 해당 평가 방식은 몇 가지 한계점을 가지고 있음 → 이를 인지하고 보완하여 활용하는 것이 필요  
  - 위치 편향은 순서를 바꿔서 두 번 평가하고 평균을 취하는 것으로 해결할 수 있음  
  - 길이 편향은 길이가 미치는 영향을 통계적으로 제거해서 어느 정도 해결할 수 있음  
    (예: **AlpacaEval2: GPT-4를 평가자로 활용 및 길이 영향 제거**)

<그림4-22_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 선호 판단에 기반한 평가 방식: AlpacaEval>

출처: Dubois et al., *Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators.*, arXiv:24.04

---

# 4-2. 거대 언어 모델의 응용 및 한계

---

## 거대 언어 모델의 응용: 멀티모달 파운데이션 모델
- 예시: **GPT-4o → 멀티모달 입력 (이미지, 비디오, 오디오)**, 멀티모달 출력 (오디오, 텍스트) 생성  

<그림4-23_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_GPT-4o를 통한 실시간 질의 응답 예시>

출처: https://openai.com/index/hello-gpt-4o/

- 예시: GPT-4o → 멀티모달 입력 (이미지, 비디오, 오디오), 멀티모달 출력 (오디오, 텍스트) 생성  

```
Xv(이미지 입력) -> Vision Encoder -> Zv(이미지 특징 벡터) -> Projection W(이미지 투영 행렬) -> Hv(이미지 토큰 표현)
Xq(텍스트 질문) -> Tokenization -> Hq(텍스트 토큰 표현)
(Hv, Hq) -> fφ(Language Model) -> Xa(최종 응답 텍스트)
```

- **핵심 아이디어**: 다른 모달리티 데이터를 거대 언어 모델이 이해할 수 있도록 토큰화 및 추가 학습  

<그림4-24_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 멀티모달 파운데이션 모델로의 확장 예시: LLaVA (이미지 & 텍스트 입력)>

출처: Liu et al., *Visual Instruction Tuning.*, NeurIPS 2023 Oral

- 예시: GPT-4o → 멀티모달 입력 (이미지, 비디오, 오디오), 멀티모달 출력 (오디오, 텍스트) 생성  
- **핵심 아이디어**: 다른 모달리티 데이터를 거대 언어 모델이 이해할 수 있도록 토큰화 및 추가 학습  

<그림4-25_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델 멀티모달 파운데이션 모델의 확장 예시: VideoPoet (멀티모달 입력, 멀티모달 출력)>

출처: Kondratyuk et al., *VideoPoet: A Large Language Model for Zero-Shot Video Generation.*, ICML 2024

- 예시: GPT-4o → 멀티모달 입력 (이미지, 비디오, 오디오), 멀티모달 출력 (오디오, 텍스트) 생성  
  - Xv(사람의 물체 옮기는 행동 비디오) → Vision-Language Model(행동 의미 이해 + 제어 신호 변환) → Xa(로봇의 물체 전달 행동)  
- **핵심 아이디어**: 다른 모달리티 데이터를 거대 언어 모델이 이해할 수 있도록 토큰화 및 추가 학습  

<그림4-26_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델의 멀티모달 파운데이션 모델 확장 예시: HELIX (Robotics)>

출처: https://discuss.pytorch.kr/t/helix-figure-ai-vla/6197

---

## 거대 언어 모델의 응용: 합성 데이터 생성
- **Self-instruct**: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52,000개의 합성 데이터 생성  
- **Self-instruct 의의**
  - 사람이 만든 소량의 데이터를 기반으로 대규모 합성 데이터셋을 확장  
  - 합성 데이터로 학습한 모델이 사람 데이터 기반 성능과 유사한 결과 달성  

<그림4-28_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 통한 합성 데이터 생성 프레임워크 예시: Self-Instruct>

출처: Wang et al., *Self-Instruct: Aligning Language Models with Self-Generated Instructions.*, ACL 2023

- **Self-instruct**: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52,000개의 합성 데이터 생성  

```
Come up with a series of tasks:  
Task 1: {instruction for existing task 1}  
Task 2: {instruction for existing task 2}  
Task 3: {instruction for existing task 3}  
...
```

<그림4-28_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 통한 합성 데이터 생성 프레임워크 예시: Self-Instruct>

출처: Wang et al., *Self-Instruct: Aligning Language Models with Self-Generated Instructions.*, ACL 2023

- **Self-instruct**: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52,000개의 합성 데이터 생성  
- **합성 데이터 예시 (Task + Input + Output)**  

```
Task: Which exercises are best for reducing belly fat at home?  
Output: Lying Leg Raises, Plank, Side Plank, Sit-ups  

Task: Extract all the country names in the paragraph, list them separated by commas.  
Example: Dr. No is the sixth novel by the English author Ian Fleming...
Output: English, British, Jamaica, China, Britain, the United States
```

<그림4-28_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 통한 합성 데이터 생성 프레임워크 예시: Self-Instruct>

출처: Wang et al., *Self-Instruct: Aligning Language Models with Self-Generated Instructions.*, ACL 2023

- **Self-instruct**: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52,000개의 합성 데이터 생성  
- **필터링 의의**  
  - 합성 데이터에서 중복·유사(유사도 높은) 데이터 제거  
  - 모델이 더 폭넓은 지시문 학습이 가능하도록 다양한 Instruction 확보  

```
노이즈 제거(유사도 낮음) / 중복 제거(유사도 높음)
ROUGE-L Overlap with the Most Similar Seed Instruction
```

<그림4-28_텍스트 파운데이션 모델_거대 언어 모델의 평가와 응용_거대 언어 모델을 통한 합성 데이터 생성 프레임워크 예시: Self-Instruct>

출처: Wang et al., *Self-Instruct: Aligning Language Models with Self-Generated Instructions.*, ACL 2023

# 4-2. 거대 언어 모델의 응용 및 한계

## | 거대 언어 모델의 응용: 합성 데이터 생성

- Self-instruct: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52000개의 합성 데이터 생성  
- 필터링 결과: 중복이거나 무관한 합성 데이터는 제거, 새로운 지시문만 남겨 다양성 확보  

- Self-instruct: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52000개의 합성 데이터 생성  
- 결과: 기존 InstructGPT에서 활용된 사람이 만든 데이터와 비슷한 성능 달성  
  - GPT-3 + 합성 데이터 39.9 vs 사람 데이터 기반 40.8  
  - SuperNI 함께 학습시: 합성 데이터 51.6 × 사람 데이터 기반 49.5

- Self-instruct: 175개의 데이터를 사람이 작성한 뒤, GPT-3를 통해 52000개의 합성 데이터 생성  
- 해당 방식은 LLaMA-1 기반 최초 개방형 instruction following 모델인 Alpaca 학습에 활용됨  

- Alpagasus: 프롬프팅을 통한 합성 데이터의 품질 평가 및 필터링 제안  
- Alpagasus 의의: 저품질 합성 데이터를 걸러내고 고품질만 학습해, 빠르고 강력한 성능 달성 목표  

- Alpagasus: 프롬프팅을 통한 합성 데이터의 품질 평가 및 필터링 제안  
  - 52000개의 Alpaca 합성 데이터 중 9000개 정도만 4.5 이상의 점수를 부여받음 → 해당 데이터만 학습에 사용  

- Alpagasus: 프롬프팅을 통한 합성 데이터의 품질 평가 및 필터링 제안  
- 결과: 전체 합성 데이터를 사용한 경우보다 높은 성능을 달성

---

## | 거대 언어 모델의 한계: 환각 (Hallucination)

- 사실과 다르거나, 전적으로 지어낸 내용임에도 불구하고 정확한 정보와 동일한 자신감과 유창함으로 응답을 생성  
- 이는 거대 언어 모델이 확률적으로 다음 토큰 예측을 통해 응답을 생성하기 때문에 발생  
- 따라서, 사용자 입장에서 거대 언어 모델의 응답에 대한 진위성을 구별하기 어렵게 만듦  

- 사전학습 데이터의 제한적인 범위가 환각 현상의 원인이 되기도 함
  - 검색 증강 생성 (Retrieval-augmented Generation, RAG) 을 통해 해결 가능 → 기본 기능으로 대부분의 거대 언어 모델 서비스에 탑제

# | 거대 언어 모델의 한계: 탈옥 (Jailbreaking)

- 프롬프팅 엔지니어링을 통해 거대 언어 모델의 정렬을 우회할 수 있다는 것이 확인됨  
- 예시: Do Anything Now (DAN) 프롬프팅  

- 프롬프팅 엔지니어링을 통해 거대 언어 모델의 정렬을 우회할 수 있다는 것이 확인됨  
- 예시: Do Anything Now (DAN) 프롬프팅  
  - GPT 답변: 특정 인물이나 사물에 대한 감정·의견을 가질 수 없음  
  - DAN 답변: 히틀러에 대해 감정을 담아 주관적인 의견을 표현함  

- 프롬프팅 엔지니어링을 통해 거대 언어 모델의 정렬을 우회할 수 있다는 것이 확인됨  
- SSAFY  
- 여러 단계의 학습 과정에서 기인한 근본적인 한계 때문에 발생했으며, 다양한 탈옥/방어 방법이 활발히 탐구 중  
  - 예시(a): 모델의 안전 규칙과 프롬프트 지시의 충돌을 유도하여 규칙을 우회하는 사례  
  - 예시(6): 의미 없는 랜덤 토큰을 지시 패턴으로 잘못 일반화하도록 유도하여 규칙을 회피하는 사례  

---

# ᅵ거대 언어 모델의 한계: AI 텍스트 검출

- 거대 언어 모델의 무분별한 사용이 학교 및 회사에서 여러가지 새로운 문제를 만들고 있음  
- 거대 언어 모델의 무분별한 사용이 학교 및 회사에서 여러가지 새로운 문제를 만들고 있음  
  ⇒ **Q. 거대 언어 모델이 만든 텍스트를 구분 또는 탐지할 수 있을까?**  
  **A. 어느정도 가능하다**

---

# 확인문제

1. 다음 중 거대 언어 모델과 BERT, GPT-1과 같은 기존 언어 모델의 차이점으로 올바른 것은?  
   a) 다음 토큰 예측에 기반한 자기 지도 학습 방법  
   b) 트랜스포머에 기반한 모델 구조  
   c) 모델 및 학습 규모가 커지면서 나타난 창발성  
   d) 이미지와 같은 도메인을 포함한 새로운 멀티 모달 학습 데이터  

**정답 및 해설**  
- 정답: **c) 모델 및 학습 규모가 커지면서 나타난 창발성**  
- 해설: a), b)의 경우 기존 언어 모델들에서도 적용되고 있으며, 거대 언어 모델은 많은 양의 텍스트 데이터에 대해 다음 토큰 예측을 통한 사전 학습으로 학습되므로 d)와 같은 이미지 데이터를 활용하지 않음

## 확인문제

2. 다음 중 지시 학습과 선호 학습에 대해 올바르지 않은 것은?

- a) 효과적인 지시 학습을 위해서는 다양한 지시 데이터가 필요하다  
- b) 크기가 충분하지 않은 거대 언어 모델은 지시 학습 후에 성능이 떨어질 수 있다  
- c) 보상 모델은 사람의 선호를 모방하도록 학습 된다  
- d) 강화 학습 기반 선호 학습의 모든 과정에는 사람의 개입이 필요하다  

**정답 및 해설**  
- 정답: **d) 강화 학습 기반 선호 학습의 모든 과정에는 사람의 지도가 필요하다**  
- 해설: 강화 학습 기반 선호 학습의  
  1) 첫번째 과정 (지시 학습),  
  2) 두번째 과정 (보상 모델 학습)  
  에는 사람의 지도를 통한 데이터 제공이 필요하지만,  
  3) 세번째 과정 (강화 학습) 에서는 모델 스스로 응답을 생성하고 보상 모델을 통해 피드백을 받아 학습이 되므로 사람의 개입이 필요하지 않다.

---

3. 다음 중 거대 언어 모델의 다양한 디코딩 알고리즘에 대한 설명으로 올바르지 않은 것은?

- a) Greedy Decoding은 가장 확률이 높은 토큰을 다음 토큰으로 생성한다  
- b) Beam Search는 확률이 높은 응답 후보를 동시에 고려하기 때문에 더 많은 생성 비용을 필요로 한다  
- c) 1 이상의 Temperature를 사용할 경우 더 다양한 응답이 생성될 확률이 감소한다  
- d) Top-K Sampling은 생성 확률이 높은 K개의 토큰만을 생성 후보로 두고 확률 값에 따라 무작위로 다음 토큰을 생성한다  

**정답 및 해설**  
- 정답: **c) 1 이상의 Temperature를 사용할 경우 더 다양한 응답이 생성될 확률이 감소한다**  
- 해설: 1 이상의 Temperature를 사용할 경우 생성 확률 분포가 기존에 비해 **smooth 해짐** (uniform에 가까워짐)  
  → 더 다양한 토큰을 생성할 확률이 **증가**  
  → 따라서 **다양한 응답이 생성될 확률 또한 증가**

---

4. 다음 중 거대 언어 모델의 평가 및 한계에 대해 올바르지 않은 것은?

- a) 주어진 질문에 대해 정답을 모르는 경우에도, LLM-as-judge 방식을 통해 생성 응답에 대해 평가할 수 있다  
- b) LLM-as-judge 방식을 선호 판단에 활용하는 경우, 길이가 짧은 응답을 선호하는 길이 편향이 있을 수 있다  
- c) GPT-5, Claude-4와 같은 최신 거대 언어 모델은 안전성 훈련이 잘 되어 있으므로, 탈옥 현상이 일어나지 않는다  
- d) 거대 언어 모델이 생성한 응답은 탐지가 가능할 수 있으므로, 무분별하게 사용해서는 안된다  

**정답 및 해설**  
- 정답: **b) LLM-as-judge 방식을 선호 판단에 활용하는 경우, 길이가 짧은 응답을 선호하는 길이 편향이 있을 수 있다**  
- 해설:  
  LLM-as-judge 방식의 선호 판단 활용에는 다음과 같은 편향이 있음  
  1) **길이가 긴 응답을 선호하는 길이 편향**  
  2) **입력 순서에 따른 순서 편향**  
  3) **동일 모델이 생성한 응답을 선호하는 자기 선호 편향**

---

## 강의 정리

### | 텍스트 파운데이션 모델 or 거대 언어 모델이란?

- 1B 이상의 큰 트랜스포머 모델이 대규모 텍스트 데이터에서 다음 토큰 예측을 통해 사전 학습된 모델  
- 실 세계 적용을 위해 지시 학습 (Instruction Tuning) 과 선호 학습 (Preference Learning)을 통해 추가 학습

---

### ᅵ거대 언어 모델의 추론

- 단순히 예측 확률이 가장 높은 것을 고르는 것 뿐만 아니라, 다양한 디코딩 알고리즘이 존재  
- 입력 프롬프트를 어떻게 주는 지에 따라 (예시: Chain-of-Thought Prompting) 성능이 크게 변화

---

### ᅵ거대 언어 모델의 평가 및 한계

- 정답이 정해진 테스크의 경우 기존 평가 방식을 따르며, 그렇지 않은 경우 LLM 기반 평가(LLM-as-judge)를 활용  
- 환각현상, 탈옥 문제, AI 텍스트 감지 등 다양한 한계 점들이 여전히 남아 있음