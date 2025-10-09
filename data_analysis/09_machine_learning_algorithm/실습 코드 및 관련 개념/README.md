## 🔹 NumPy 주요 함수 정리
### `np.arange()`
일정한 간격의 숫자 배열을 생성하는 함수

- 형태
  ```python
  np.arange(start, stop, step)
  ```
  - start: 시작값 (기본값 0)
  - stop: 끝값 (포함X)
  - step: 증가 간ㅇ격 (기본값 1)

- 예시
  ```python
  np.arange(5)          # array([0, 1, 2, 3, 4])
  np.arange(2, 10, 2)   # array([2, 4, 6, 8])
  ```

### `.reshape()`
배열의 형태(차원) 를 변경하는 함수

- 형태
  ```python
  array.reshape(rows, cols)
  ```

- 예시
  ```python
  arr = np.arange(6)          # [0 1 2 3 4 5]
  arr.reshape(2, 3)           # [[0 1 2]
                              #  [3 4 5]]
  ```

- 활용
  - scikit-learn 모델(LinearRegression)은 2차원 입력만 허용하므로
  - `np.arange(len(data)).reshape(-1, 1)` 형태로 변환해야 함
  - (즉, `(n,)` -> `(n, 1)` 형태로 변환)

### `np.array()`
Python 리스트(list)를 NumPy 배열로 변환하는 함수

- 예시
  ```python
  data = [10, 20, 30]
  np.array(data)  # array([10, 20, 30])
  ```

- 활용
  - sklearn 모델의 입력은 반드시 NumPy 배열 형태여야 함
  - ex. `np.array([[len(weekdays_data) - 1]])` 
    - "마지막 날의 인덱스(예: [[30]])"를 모델 입력 형태로 변환한 것


## 🔹 랜덤 포레스트 (Random Forest)
여러 개의 의사결정나무(Decision Tree) 를 학습시켜, 그 예측 결과를 투표(Voting) 또는 평균(Avg.) 하는 앙상블 학습(Ensemble Learning) 기법

-> 분류(Classification)와 회귀(Regression) 문제 모두 사용 가능

-> 과적합(Overfitting)에 강하고, 변수 중요도(Feature Importance)를 해석하기 쉬움

### 🌲 동작 원리
1. Bootstrap Sampling (부트스트랩 샘플링)
    - 원본 데이터에서 중복을 허용하며 랜덤하게 샘플링
    - 각 트리(Tree)는 다른 데이터셋으로 학습됨

2. Random Feature Selection (무작위 특성 선택)
    - 각 노드를 분할할 때 전체 특성이 아닌 일부 특성만 무작위로 고려
    - 트리 간 다양성을 높여 과적합 방지

3. Ensemble (앙상블)
    - 여러 트리의 결과를 **평균(회귀)** 또는 **투표(분류)** 로 결합

### 코드 예시
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# 1. 독립변수(X): 시간대별 교통량 / 종속변수(y): 혼잡 여부
X = df.loc[:, '0시':'23시']
y = df['혼잡']

# 2. 데이터 분리 (훈련 70%, 테스트 30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 3. 랜덤 포레스트 분류 모델 생성 및 학습
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. 예측
predicted = model.predict(X_test)

# 5. 정확도 평가
accuracy = model.score(X_test, y_test)
print(f"테스트 데이터 정확도: {accuracy:.2f}")

# 테스트 셋의 첫 번째 샘플 확인
X_first = X_test.iloc[[0]]
date_first = df.loc[0, '일자']

# 실제값과 예측값 비교
actual = y_test.iloc[0]
pred = model.predict(X_first)[0]

print(f"선택된 날짜: {date_first}")
print(f"실제 혼잡 여부: {'혼잡' if actual else '비혼잡'}")
print(f"예측 혼잡 여부: {'혼잡' if pred else '비혼잡'}")
```
- RandomForestClassifier
  - 주요 파라미터
    - `n_estimators` : 생성할 트리(Decision Tree) 개수 (기본값 100)
    - `max_depth` : 트리의 최대 깊이 제한 (기본값 None(자동))
    - `min_samples_split` : 노드를 분할하기 위한 최소 샘플 수 (기본값 2)
    - `min_samples_leaf` : 리프 노드에 있어야 하는 최소 샘플 수 (기본값 1)
    - `max_features` : 각 트리 분할 시 고려할 특성의 개수 (기본값 "sqrt" (분류일 때))
    - `random_state` : 랜덤 시드 고정 (기본값 None)

### 정리
| 항목     | 설명                                      |
| ------ | --------------------------------------- |
| 모델 유형  | 앙상블 기반 지도학습(분류/회귀 모두 가능)                |
| 학습 구조  | 다수의 의사결정나무(Decision Tree) 결합            |
| 특징 선택  | 각 트리마다 랜덤한 특성(feature) 조합 사용            |
| 예측 방식  | 분류: 다수결 투표(Voting)<br>회귀: 평균(Averaging) |
| 해석 가능성 | 각 변수별 `feature_importances_`로 중요도 확인 가능 |


## 🔹 데이터 스케일링 (표준화, Standardization)
각 특성(feature)의 값이 서로 다른 범위나 단위를 가질 때, 평균을 0, 표준편차를 1로 맞추는 정규화 기법

-> 모델이 **모든 특성을 동일한 기준에서 학습**하도록 만들어줌

-> 특히 **거리 기반 알고리즘(KNN, SVM, PCA 등)** 에서 필수적으로 사용

### 필요한 이유
| 상황                 | 문제점                           | 표준화 효과        |
| ------------------ | ----------------------------- | ------------- |
| 특성마다 단위가 다름        | 예: 교통량(단위: 대) vs 속도(단위: km/h) | 단위 차이 제거      |
| 한 특성의 값 범위가 매우 큼   | 모델이 큰 값에 더 민감해짐               | 스케일을 동일하게 맞춰줌 |
| 거리 기반 알고리즘 (KNN 등) | 거리 계산 시 큰 값이 지배적              | 모든 축에서 균형 유지  |

### ✅ 예시: KNN 모델 학습 전 표준화
```python
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 1. 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 2. StandardScaler 객체 생성
scaler = StandardScaler()

# 3. 훈련 데이터로 기준(평균, 표준편차) 학습 후 변환
X_train_scaled = scaler.fit_transform(X_train)

# 4. 동일한 기준으로 테스트 데이터 변환
X_test_scaled = scaler.transform(X_test)

# 5. KNN 모델 생성 및 학습
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
```
- `fit()` : 훈련 데이터의 평균(μ)과 표준편차(σ) 계산 -> 스케일 기준 학습
- `transform()` : 계산된 μ, σ로 데이터 변환 -> 실제 표준화 적용
- `fit_transform()` : `fit()` + `transform()`을 한 번에 수행(훈련 데이터용)


## 🔹 분류 모델 성능 평가 지표
### 혼동 행렬 (Confusion Matrix)
**실제 클래스와 모델 예측 결과를 비교**하여, 모델이 어떤 오류를 주로 범했는지 한눈에 파악할 수 있는 표

|    실제 ↓ / 예측 →   |               Positive (1)              |               Negative (0)              |
| :--------------: | :-------------------------------------: | :-------------------------------------: |
| **Positive (1)** |  **TP (True Positive)**<br>실제 1 → 예측도 1 | **FN (False Negative)**<br>실제 1 → 예측은 0 |
| **Negative (0)** | **FP (False Positive)**<br>실제 0 → 예측은 1 |  **TN (True Negative)**<br>실제 0 → 예측도 0 |

- 코드
  ```python
  from sklearn.metrics import confusion_matrix

  conf_matrix = confusion_matrix(y_test, y_pred)
  print(conf_matrix)
  ```

### 주요 성능 지표 (Precision, Recall, F1-score)
| 지표   | 수식             | 의미       | 좋은 모델 기준    |
| ------ | ---------------- | ------------ | ----------- |
| **정밀도 (Precision)**  | $\text{Precision} = \frac{TP}{TP + FP}$ | 모델이 "혼잡"이라 예측한 것 중 실제 혼잡인 비율 | 높을수록 좋음     |
| **재현율 (Recall)**     | $\text{Recall} = \frac{TP}{TP + FN} $ | 실제 혼잡인 데이터 중 모델이 잘 맞춘 비율     | 높을수록 좋음     |
| **F1 점수 (F1-score)** | $F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$ | 정밀도와 재현율의 조화 평균              | 1에 가까울수록 좋음 |
| **정확도 (Accuracy)**   | $Accuracy = \frac{TP + TN}{TP + TN + FP + FN} $   | 전체 중 올바르게 예측한 비율             | 1에 가까울수록 좋음 |

- 코드
  ```python
  from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

  # 혼동 행렬
  conf_matrix = confusion_matrix(y_test, y_pred)
  print("혼동 행렬 (Confusion Matrix):")
  print(conf_matrix)

  # 분류 리포트 (Precision, Recall, F1)
  report = classification_report(y_test, y_pred)
  print("\n분류 성능 평가 (Classification Report):")
  print(report)

  # 정확도
  accuracy = accuracy_score(y_test, y_pred)
  print(f"\n모델 정확도(Accuracy): {accuracy:.2f}")
  ```


## 🔹 단항 회귀 vs 다항 회귀
### 단항 회귀 (Simple Linear Regression)
하나의 독립 변수(X)와 종속 변수(y) 간의 **직선(linear) 관계**를 학습하는 회귀 모델

- 수식
  - $y = w_0 + w_1x $
  - 설명
    | 기호          | 의미           |
    | ----------- | ------------ |
    | $\hat{y}$ | 예측값          |
    | $w_0$     | 절편 (bias)    |
    | $w_1$     | 기울기 (weight) |
    | $x$      | 독립 변수        |


- 코드 예시
  ```python
  linear_model = LinearRegression()
  linear_model.fit(X_train, y_train)
  y_pred_linear = linear_model.predict(X_test)

  mse_linear = mean_squared_error(y_test, y_pred_linear)
  rmse_linear = np.sqrt(mse_linear)
  print(f"단항 회귀 RMSE: {rmse_linear:.2f}")
  ```

### 다항 회귀 (Polynomial Regression)
단항 회귀에서 확장된 형태로, **비선형 관계(곡선형 데이터)** 를 표현할 수 있음

- 수식
  - $y = w_0 + w_1x + w_2x^2 + w_3x^3 + \dots + w_nx^n$
  - 설명
    | 기호      | 의미                    |
    | ------- | --------------------- |
    | $n$   | 다항식의 차수 (예: 2차, 3차 등) |
    | $w_i$ | 각 항의 가중치              |
    | $x^i$ | 독립 변수의 i차 항           |

- 코드 예시
  ```python
  from sklearn.preprocessing import PolynomialFeatures

  poly = PolynomialFeatures(degree=2)
  X_poly = poly.fit_transform(days)

  X_train_poly, X_test_poly, y_train_poly, y_test_poly = train_test_split(
      X_poly, traffic_at_8am, test_size=0.2, random_state=42
  )

  poly_model = LinearRegression()
  poly_model.fit(X_train_poly, y_train_poly)

  y_pred_poly = poly_model.predict(X_test_poly)
  mse_poly = mean_squared_error(y_test_poly, y_pred_poly)
  rmse_poly = np.sqrt(mse_poly)

  print(f"다항 회귀 RMSE: {rmse_poly:.2f}")
  ```

### 단항 vs 다항 회귀 비교
| 항목     | **단항 회귀 (Linear Regression)** | **다항 회귀 (Polynomial Regression)** |
| ------ | ----------------------------- | --------------------------------- |
| 관계 형태  | 직선 관계 (선형)                    | 곡선 관계 (비선형)                       |
| 복잡도    | 낮음 (단순)     | 높음 (차수 ↑ 시 복잡도 ↑)  |
| 표현력    | 제한적 (직선만 표현)     | 유연함 (곡선 패턴 학습 가능)   |
| 과적합 위험 | 낮음     | 높음 (차수↑ 시 overfitting 위험)         |
| 사용 예시  | 온도 ↗ → 판매량 ↗  | 요일별 교통량처럼 주기성 있는 데이터              |
| 수식 예시  | $y = w_0 + w_1x $    |  $y = w_0 + w_1x + w_2x^2$   |

### 예측 예시 코드: 5번 실습
```python
# 단항 회귀 예측
predicted_traffic_linear = linear_model.predict(np.array([[len(weekdays_data)]]))[0]

# 다항 회귀 예측
last_day_index_poly = poly.transform(np.array([[len(weekdays_data)]]))
predicted_traffic_poly = poly_model.predict(last_day_index_poly)[0]

print(f"단항 회귀 예측: {predicted_traffic_linear:.2f}")
print(f"다항 회귀 예측: {predicted_traffic_poly:.2f}")
```
- 단항 회귀 예측
  - `len(weekdays_data)` : 데이터셋의 전체 일수 (예: 31일이면 마지막 날의 인덱스는 31)
  - `np.array([[len(weekdays_data)]])` : scikit-learn의 `predict()` 함수는 **2차원 배열 형태의 입력을 요구**하므로, 단일 인덱스 값을 `[[ ]]` 이중 리스트로 감싸서 넘겨줘야함
  - `linear_model.predict(...)` : 학습된 단항 회귀 모델이 입력값(마지막 날 인덱스)에 대한 예측 교통량(8시 기준) 을 계산
  - `[0]` : predict()의 결과는 배열 형태이므로, 실제 예측값을 꺼내기 위해 [0]을 붙임
  - 즉, 단항 회귀 모델이 학습한 "요일에 따른 선형 추세"를 기반으로 마지막 날의 8시 교통량을 직선 관계로 예측

- 다항 회귀 예측
  - `poly.transform()` : `x, x², x³ …` 같은 다항 항들을 자동으로 생성해줌
    - 예를 들어, `degree=2`라면 입력값 `x = 31 → [1, 31, 31²]` 로 변환됨
  - `poly_model.predict(...)` : 학습된 다항 회귀 모델이 변환된 다항식 입력을 기반으로 마지막 날의 8시 교통량을 곡선 형태의 관계로 예측함
  - `[0]` : 예측값을 배열에서 꺼내서 실수(float) 형태로 출력
  - 즉, 다항 회귀 모델은 비선형(곡선) 관계를 반영하여 교통량의 변화 패턴(예: 주중 상승 → 주말 하락 등)을 더 정교하게 예측

