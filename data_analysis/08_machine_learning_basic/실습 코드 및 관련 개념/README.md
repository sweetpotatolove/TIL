# 실습 관련 개념 정리
## 🔹 One-Hot Encoding
⚡ **One-Hot Encoding**은 범주형 데이터를 숫자로 변환할 때 자주 사용하는 방법으로

⚡ 특정 범주(category)에 해당하면 `1`, 아니면 `0`을 부여하여
모델이 각 범주를 독립된 특징으로 인식하도록 만들어줌

### 예시: 날짜 One-Hot Encoding
| Day of Week | Day_0 | Day_1 | Day_2 | Day_3 | Day_4 | Day_5 | Day_6 |
| ----------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0 (월)       | 1     | 0     | 0     | 0     | 0     | 0     | 0     |
| 3 (목)       | 0     | 0     | 0     | 1     | 0     | 0     | 0     |
| 6 (일)       | 0     | 0     | 0     | 0     | 0     | 0     | 1     |

### 수동 구현 (`apply` + `lambda`)
```python
# "Day of Week" 컬럼에 0~6 (월~일)이 들어 있다고 가정
# 각 요일에 대해 새로운 컬럼 생성
for i in range(7):
    data[f'Day_{i}'] = data['Day of Week'].apply(lambda x: 1 if x == i else 0)
```
- `lambda x` : 행마다 Day of Week 값을 받아옴
- `1 if x == i else 0` : 해당 요일이면 1, 아니면 0
- `.apply()` : 각 행에 함수를 적용하여 새로운 컬럼 생성
- 람다식 구조 분석
  ```python
  # 일반 함수 버전
  def f(x):
      return 1 if x == i else 0

  # 람다 버전
  # lambda x: -> 이름 없는 함수인데, 입력값이 'x'
  lambda x: 1 if x == i else 0
  ```

### 자동 구현 (`pd.get_dummies()`)
```python
import pandas as pd

data = pd.DataFrame({
    'Day of Week': [0, 3, 6]
})

encoded = pd.get_dummies(data, columns=['Day of Week'], prefix='Day')
print(encoded)
```
- `pd.get_dummies()`
  - **범주형 데이터(categorical data)** 를
모델이 학습할 수 있는 **이진(0/1) 형태**로 자동 변환해주는 함수
  - 즉, One-Hot Encoding을 손쉽게 구현 가능
  - 주요 파라미터
    | 옵션             | 기본값        | 설명                         |
    | -------------- | ---------- | -------------------------- |
    | **data**       | (필수)       | 변환할 데이터프레임                 |
    | **columns**    | `None`     | 인코딩할 컬럼 지정 (여러 개 가능)       |
    | **prefix**     | `None`     | 생성되는 컬럼 이름 앞에 붙일 접두사       |
    | **drop_first** | `False`    | 첫 번째 더미 컬럼을 제거 (다중공선성 방지용) |
    | **dtype**      | `np.uint8` | 생성된 더미 컬럼의 데이터 타입          |


## 🔹 Label Encoding
⚡ **Label Encoding**은 **문자열(범주형 데이터)을 정수형 숫자**로 변환하는 가장 기본적인 인코딩 방식

⚡ 각 고유한 문자열 값에 대해 하나의 고유한 정수 라벨을 부여함

### 🔍 개념
| 문자열 값 | 정수 라벨 |
| ----- | ----- |
| A     | 0     |
| B     | 1     |
| C     | 2     |
- 예를 들어, `['A', 'C', 'B', 'A']`라는 컬럼이 있다면
- Label Encoding 결과는 `[0, 2, 1, 0]`

### 코드 구현
```python
from sklearn.preprocessing import LabelEncoder

# LabelEncoder 객체 생성
encoder = LabelEncoder()

# 인코딩 대상 데이터
colors = ['Red', 'Green', 'Blue', 'Green']

# 변환 수행
encoded = encoder.fit_transform(colors)

print("인코딩 결과:", encoded)
print("클래스 목록:", encoder.classes_)

```
- LabelEncoder
  - Scikit-learn에서 제공하는 인코더로,
문자열(또는 범주형 데이터)을 정수형 숫자(Label) 로 변환함
  - 각 고유한 클래스 값을 0부터 시작하는 정수로 매핑하는 역할
  - 주요 메서드
    | 메서드                    | 설명                          | 예시                         |
    | ---------------------- | --------------------------- | -------------------------- |
    | `fit(y)`               | 데이터의 고유값을 학습하여 내부 매핑 테이블 생성 | `'Red' → 2`, `'Blue' → 0`  |
    | `transform(y)`         | 학습된 매핑 기준으로 실제 데이터 변환       | `'Green' → 1`              |
    | `fit_transform(y)`     | `fit` + `transform` 동시에 수행  |                            |
    | `inverse_transform(y)` | 숫자를 다시 원래 문자열로 복원           | `[2, 0] → ['Red', 'Blue']` |
    | `classes_`             | 학습된 고유 클래스 목록 확인            | `['Blue', 'Green', 'Red']` |
  - ⚠️ 주의점
    - LabelEncoder는 **1차원 데이터만 처리 가능**
    - 여러 개의 컬럼(2D 데이터)에 사용하려면 각각 따로 인코딩해야 함
      ```python
      data['col1'] = encoder.fit_transform(data['col1'])
      data['col2'] = encoder.fit_transform(data['col2'])
      ```

### ⚠️ 주의사항
Label Encoding은 **숫자의 크기가 인위적인 "순서"로 인식**될 수 있음

-> 즉, A=0, B=1, C=2이면
모델이 **“C가 B보다 크다”**처럼 잘못된 관계로 해석할 수 있음 ❌

-> 따라서:
- **순서가 없는 데이터(Nominal)** -> ❌ Label Encoding (대신 `One-Hot Encoding` 권장)
- **순서가 있는 데이터(Ordinal)** → ✅ `Label Encoding` 사용


## 🔹 이상치 탐지 (Outlier Detection)
⚡ 이상치는 데이터의 전반적인 분포에서 벗어난 극단적인 값을 의미

⚡ 이상치가 존재하면 모델 학습 시 왜곡이 발생하거나 예측 성능이 저하될 수 있으므로
분석 전에 반드시 탐지 및 처리해야 함

### IQR (Interquartile Range) 기반 이상치 탐지
데이터의 **사분위수(Quartile)** 를 이용해 이상치를 판별

-> 데이터의 중간 50% 구간(Q1~Q3)을 기준으로, 이 범위에서 너무 벗어난 값을 이상치로 간주함

| 구분                | 의미             |
| ----------------- | -------------- |
| **Q1 (1사분위수)**    | 하위 25% 지점의 값   |
| **Q3 (3사분위수)**    | 상위 25% 지점의 값   |
| **IQR (Q3 - Q1)** | 데이터의 중앙 50% 범위 |

- 이상치 판단 기준
  - $lower_bound=Q1−1.5×IQR$
  - $upper_bound=Q3+1.5×IQR$

- 코드 예시
  ```python
  # 1. 사분위수 계산
  Q1 = data['Speed (km/h)'].quantile(0.25)
  Q3 = data['Speed (km/h)'].quantile(0.75)
  IQR = Q3 - Q1

  # 2. 이상치 기준선 설정
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  # 3. 이상치 판별
  data['IQR Outlier'] = (data['Speed (km/h)'] < lower_bound) | (data['Speed (km/h)'] > upper_bound)
  ```

- 특징
  - 분포가 비정규일 때도 사용 가능
  - 계산이 간단하고, 극단값에 덜 민감함
  - 데이터 양이 작으면 경계선이 불안정해짐
  - 비정규분포, 소규모 데이터셋에 적합함

### Z-score 기반 이상치 탐지
**Z-score**는 각 데이터가 평균으로부터 몇 표준편차(σ) 떨어져 있는지를 나타냄

-> 데이터가 정규분포를 따른다고 가정할 때,
Z-score의 절댓값이 **3 이상**이면 일반적으로 이상치로 간주함

-> $Z = \frac{x - \mu}{\sigma}$

| 기호         | 의미    |
| ---------- | ----- |
|  $x$      | 데이터 값 |
|  $\mu$    | 평균    |
|  $\sigma$ | 표준편차  |

- 코드 예시
  ```python
  from scipy import stats

  # 1. Z-score 계산
  data['Z-score'] = stats.zscore(data['Speed (km/h)'])

  # 2. Z-score 기준으로 이상치 판별 (절댓값이 3 초과)
  data['Z-score Outlier'] = (abs(data['Z-score']) > 3)
  ```

- 특징
  - 정규분포(가우시안 분포)를 가정
  - 이상치의 "정도"를 수치로 표현 가능
  - 정규분포가 아닐 경우 부정확함
  - 대규모, 정규분포에 가까운 데이터셋에 적합함


## 🔹 회귀(Regression) 모델 성능 평가 지표
⚡ 회귀 모델은 **연속적인 값을 예측**하는 모델로

⚡ 예측값과 실제값의 차이를 수치로 평가하기 위해 여러 지표(metric)를 사용함

|지표 | 수식| 설명| 좋은 모델 기준| 
| ---- | --- | --- | ------- |
| **MAE**<br>(Mean Absolute Error)             | $MAE = \frac{1}{n}\sum_{i=1}^{n} y_i - \hat{y}_i$  | 절대 오차의 평균. 이상치에 둔감하며 해석이 직관적 | 0에 가까울수록 좋음  |
| **MSE**<br>(Mean Squared Error) | $MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$  | 제곱 오차의 평균. 큰 오차에 민감 | 0에 가까울수록 좋음 |                              |              |
| **RMSE**<br>(Root Mean Squared Error)| $RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$ | MSE의 제곱근. 실제 단위로 해석 가능 | 0에 가까울수록 좋음 |                              |              |
| **R² Score**<br>(결정계수) | $R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$ | 모델의 설명력 (1이면 완벽, 0은 평균 수준) | 1에 가까울수록 좋음 |                              |              |
| **MAPE**<br>(Mean Absolute Percentage Error) | $MAPE = (100/n) Σ ∣yᵢ − ŷᵢ∣ / ∣yᵢ∣$ | 상대적 오차 비율(%)   | 0%에 가까울수록 좋음 |

- 코드 사용 예시
  ```python
  import numpy as np
  from sklearn.metrics import mean_absolute_error
  from sklearn.metrics import mean_squared_error
  from sklearn.metrics import r2_score 
  from scipy import stats

  # 예시 데이터
  y_true = np.array([3.0, -0.5, 2.0, 7.0])
  y_pred = np.array([2.5, 0.0, 2.1, 7.8])

  # MAE (평균 절대 오차)
  mae = mean_absolute_error(y_true, y_pred)

  # MSE (평균 제곱 오차)
  mse = mean_squared_error(y_true, y_pred)

  # RMSE (평균 제곱근 오차)
  rmse = np.sqrt(mse)

  # R² Score (결정계수)
  r2 = r2_score(y_true, y_pred)

  # MAPE (평균 절대 백분율 오차)
  mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100

  # 결과 출력
  print("회귀 모델 성능 평가 지표 결과")
  print("--------------------------------")
  print(f"MAE  (Mean Absolute Error): {mae:.4f}")
  print(f"MSE  (Mean Squared Error): {mse:.4f}")
  print(f"RMSE (Root Mean Squared Error): {rmse:.4f}")
  print(f"R²   (R-squared): {r2:.4f}")
  print(f"MAPE (Mean Absolute Percentage Error): {mape:.2f}%")
  ```

