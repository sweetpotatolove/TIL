## 🔹 Gradient Boosting Classifier
**Gradient Boosting**은 여러 개의 약한 학습기(weak learner), 주로 결정 트리(Decision Tree) 를 순차적으로 학습시켜
오차를 점진적으로 줄여 나가는 앙상블(Ensemble) 학습 방법

- 첫 번째 모델이 예측한 결과의 잔차(residual, 오차) 를 다음 모델이 학습
- 이렇게 오차를 보정하는 과정을 반복하면서 하나의 강력한 예측 모델(strong learner) 을 만들어냄
- 손실 함수의 기울기(gradient) 를 따라가며 오차를 줄여나가기 때문에
"Gradient Boosting"이라는 이름이 붙음

### ⚙️ 동작 원리
1. 초기 예측값을 설정 (예: 평균값으로 시작)
2. 실제값과의 차이(오차, Residual)를 계산
3. 오차를 예측하도록 새로운 결정 트리를 학습
4. 새 모델의 결과를 기존 예측에 누적
5. 이 과정을 n_estimators 횟수만큼 반복

-> 💡 각 단계에서 잘못 예측된 데이터에 더 큰 가중치(weight) 를 주어,
모델이 어려운 샘플에 집중하도록 유도

### 주요 하이퍼파라미터
| 매개변수              | 의미          | 역할                                |
| ----------------- | ----------- | --------------------------------- |
| **n_estimators**  | 약한 학습기의 개수  | 반복 횟수가 많을수록 성능 ↑ (단, 과적합 위험 ↑)    |
| **learning_rate** | 학습률         | 각 단계에서 얼마나 강하게 보정할지 결정 (작을수록 안정적) |
| **max_depth**     | 각 트리의 최대 깊이 | 트리의 복잡도 조절 (과적합 방지용)              |
| **random_state**  | 난수 고정 시드    | 실험 재현성 확보용                        |


### 코드 예시
```python
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 데이터 표준화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Gradient Boosting 모델 생성 및 학습
model = GradientBoostingClassifier(
    n_estimators=10,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
model.fit(X_train_scaled, y_train)

# 예측
y_pred = model.predict(X_test_scaled)
```

### 장단점
- 장점
  - 예측 정확도가 높음
  - 이상치(Outlier)에 비교적 강함
  - 다양한 데이터 유형에 적용 가능

- 단점
  - 학습 시간이 오래 걸림
  - 하이퍼파라미터 튜닝 필요
  - 너무 많은 트리를 사용하면 과적합 가능


## 🔹 Logistic Regression (로지스틱 회귀)
**로지스틱 회귀(Logistic Regression)** 는 이름에 회귀(Regression) 가 들어가지만, 실제로는 이진 분류(Binary Classification) 문제를 해결하는 지도 학습(Supervised Learning) 알고리즘

- 입력 데이터가 특정 클래스(예: 혼잡 / 비혼잡)에 속할 확률(0~1) 을 예측
- 선형 회귀 결과를 시그모이드(Sigmoid) 함수를 통해 확률 형태로 변환
- 특정 임계값(보통 0.5)을 기준으로 클래스를 분류

### L2 정규화 (Ridge Regularization)
L2 정규화는 모델의 과적합(overfitting) 을 방지하기 위한 방법으로,
**가중치가 너무 커지는 것을 억제**하여 모델의 복잡도를 줄임

- C 값이 작을수록 → 정규화 강도가 강함 (가중치 작게 유지)
- C 값이 클수록 → 정규화가 약함 (가중치 자유로움 → 과적합 위험 ↑)

### ⚙️ Logistic Regression 주요 하이퍼파라미터
| 파라미터              | 설명                                                   | 기본값       | 참고 / 역할                                                                                               |
| ----------------- | ---------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| **penalty**       | 정규화 방식 선택 (`'l1'`, `'l2'`, `'elasticnet'`, `'none'`) | `'l2'`    | 과적합 방지를 위해 가중치에 패널티 부여 <br>→ L2: Ridge, L1: Lasso                                                     |
| **C**             | 정규화 강도 제어 (λ의 역수)         | `1.0`     | 작을수록 정규화 강함 (가중치 작게), <br> 클수록 정규화 약함 (가중치 자유로움)                                                      |
| **solver**        | 최적화 알고리즘 선택       | `'lbfgs'` | - `'liblinear'`: 작은 데이터, L1/L2 지원<br>- `'lbfgs'`: L2, 다중 클래스 지원<br>- `'saga'`: L1/L2/elasticnet 모두 지원 |
| **max_iter**      | 학습 반복 횟수      | `100`     | 수렴(convergence)이 안 될 경우 값 증가              |
| **multi_class**   | 다중 클래스 분류 방식        | `'auto'`  | `'ovr'`(One-vs-Rest), `'multinomial'`(Softmax)              |
| **random_state**  | 난수 시드 고정        | `None`    | 재현 가능한 결과를 위해 고정 값 사용                        |
| **fit_intercept** | 절편(bias) 추가 여부     | `True`    | False면 데이터가 이미 평균 0일 때 사용                      |
| **class_weight**  | 클래스 불균형 보정    | `None`    | `'balanced'`로 설정 시 자동 가중치 부여                                                                          |
| **n_jobs**        | 병렬 처리 개수       | `None`    | `'liblinear'` 외의 solver에서는 미지원               |


### 코드 예시
```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 데이터 표준화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 로지스틱 회귀 모델 생성 및 학습
model = LogisticRegression(
    C=1.0,          # 정규화 강도 (1.0 = 기본값)
    penalty='l2',   # L2 정규화
    random_state=42
)
model.fit(X_train_scaled, y_train)

# 예측
y_pred = model.predict(X_test_scaled)
```

### 장단점
- 장점
  - 확률 기반 예측이 가능
  - 단순하고 해석 용이
  - 계산 비용이 적고 빠름

- 단점
  - 비선형 관계 데이터엔 부적합
  - 이상치에 민감
  - 다중 공선성 시 성능 저하 가능


## 🔹 앙상블 학습 (Ensemble Learning)
앙상블 학습은 여러 개의 개별 모델(약한 학습기, Weak Learner)을
결합하여 하나의 강력한 모델(Strong Learner) 을 만드는 기법

### 앙상블 학습 방식 비교
| 구분              | **배깅 (Bagging)**     | **부스팅 (Boosting)**                                          | **스태킹 (Stacking)**                        |
| --------------- | -------------------- | ----------------------------------------------------------- | ----------------------------------------- |
| **핵심 아이디어**     | 여러 모델을 **병렬로 독립 학습** | 여러 모델을 **순차적으로 학습**하며 오차 보정                                 | 여러 모델의 **출력을 조합하는 메타 모델** 학습              |
| **학습 구조**       | 병렬 (Parallel)        | 순차 (Sequential)                                             | 병렬 + 메타 모델                                |
| **데이터 샘플링 방식**  | 부트스트래핑(중복 허용 랜덤 샘플링) | 이전 모델이 틀린 데이터에 가중치 부여                                       | 각 모델은 동일한 데이터 학습                          |
| **대표 알고리즘**     | 🎯 Random Forest     | 🚀 Gradient Boosting, AdaBoost, XGBoost, LightGBM, CatBoost | 🧠 StackingClassifier / StackingRegressor |
| **결과 결합 방식**    | 평균(회귀) / 다수결(분류)     | 가중합 (이전 모델 보정)                                              | 메타 모델이 예측 결합                              |
| **병렬 처리 가능 여부** | ✅ 가능                 | ❌ 불가능 (순차 구조)                                               | ⚙️ 가능 (메타 모델 제외)                          |
| **과적합 위험도**     | 낮음                   | 상대적으로 높음 (학습률 조절 필요)                                        | 중간 (메타 모델에 따라 다름)                         |
| **예측 성능**       | 안정적                  | 매우 우수                                                       | 가장 높은 수준 (잘 조합 시)                         |

### 주요 앙상블 알고리즘
| 알고리즘                  | 방식                     | 주요 특징                                  |
| --------------------- | ---------------------- | -------------------------------------- |
| **Random Forest**     | Bagging                | 다수의 결정 트리를 랜덤 샘플로 학습하여 평균 또는 다수결 예측    |
| **Extra Trees**       | Bagging (랜덤성 강화)       | 노드 분할 시 무작위 기준 사용 → 속도 향상, 과적합 방지      |
| **AdaBoost**          | Boosting               | 잘못 분류된 샘플에 높은 가중치 부여, 단순 모델의 연쇄 개선     |
| **Gradient Boosting** | Boosting               | 잔여 오차(Residual)를 학습하며 손실 함수의 그래디언트 최소화 |
| **XGBoost**           | Boosting (고속화)         | Gradient Boosting을 병렬화하고 정규화 추가        |
| **LightGBM**          | Boosting (Leaf-wise)   | 트리 확장 시 리프 노드 기준으로 성장, 대용량 데이터에 적합     |
| **CatBoost**          | Boosting (Categorical) | 범주형 변수 자동 처리, 오버피팅 방지                  |
| **Stacking**          | Stacking               | 여러 모델의 예측 결과를 메타 모델이 통합하여 최종 예측        |

### 배깅 vs 부스팅 vs 스태킹
| 항목            | **배깅 (Bagging)** | **부스팅 (Boosting)** | **스태킹 (Stacking)** |
| ------------- | ---------------- | ------------------ | ------------------ |
| **모델 독립성**    | 서로 독립적           | 순차적 (이전 모델에 의존)    | 독립 모델 + 메타 모델      |
| **주요 목적**     | 분산(Variance) 감소  | 편향(Bias) 감소        | 여러 모델의 강점을 결합      |
| **대표 알고리즘**   | RandomForest     | XGBoost, LightGBM  | StackingClassifier |
| **병렬화 가능 여부** | 가능               | 불가능                | 가능                 |
| **장점**        | 과적합에 강하고 안정적     | 높은 예측 성능           | 종합적 정확도 향상         |
| **단점**        | 비선형 관계 한계        | 느린 학습, 파라미터 민감     | 복잡한 구조, 해석 어려움     |

### 앙상블 장점
- **정확도 향상** : 여러 모델의 평균 또는 투표 결과로 예측 안정성 향상
- **편향(Bias) 감소** : Boosting은 반복 학습을 통해 오차 보정  
- **분산(Variance) 감소** : Bagging은 랜덤 샘플링으로 모델 변동성 완화
- **일반화 성능 향상** : 개별 모델보다 테스트 데이터에 더 강건한 성능 확보
