# Pandas 심화
## Pandas와 Numpy
### Pandas
주로 2차원 데이터(표 형태, DataFrmae)를 다룰 때 유용

- 데이터 분석, 전처리, 조작이 편함
- 엑셀, CSV, SQL 결과 같은 표 형식의 데이터 처리에 최적화되어 있음

### NumPy
다차원 배열(1D, 2D, 3D 이상)을 다루는 데 특화됨

- 특히 딥러닝과 고성능 연산을 위해 주로 사용됨
- 3차원 이상 데이터(이미지, 시계열, 텐서 연산 등) 처리에 적합함

  ![alt text](image.png)

- `ndarray` 
  - N 차원(Dimension) 배열(Array) 객체

    ![alt text](image-1.png)
  - ndarray 생성 - `array()`
    - 인자로 주로 파이썬 list 또는 ndarray 입력
      ```python
      import numpy as np

      # 1차원 배열 생성
      array1 = np.array([1, 2, 3])

      # 2차원 배열 생성
      array2 = np.array([[1, 2, 3],
                        [4, 5, 6]])
      ```
      ![alt text](image-2.png)
  
  - ndarray 생성 - `arrange()`
    - 0부터 9까지 숫자를 순차적으로 생성
      ```python
      sequence_array = np.arange(10)
      print(sequence_array)
      print(sequence_array.dtype, sequence_array.shape)
      ```
      ![alt text](image-3.png)

  - ndarray 생성 - `zeros()` / `ones()`
    - (3, 2) shape를 가지는 모든 원소가 0, dtype은 int32인 ndarray 생성
      ```zero_array = np.zeros((3, 2), dtype='int32')
      print(zero_array)
      print(zero_array.dtype, zero_array.shape)
      ```
      ![alt text](image-4.png)
  
  - 데이터 타입 - `ndarray.dtype`
    - ndarray 내 데이터 타입은 같은 데이터 타입만 가능 -> ndarray.dtype 속성
    - 즉, 한 개의 ndarray 객체에 int와 float 함께 불가능 -> `astype()` 활용하여 형변환
      ```python
      list1 = [1, 2, 3]
      print(type(list1))

      array1 = np.array(list1)
      print(type(array1))
      print(array1, array1.dtype)
      ```
      ![alt text](image-5.png)

  - 형태(shape)와 차원(ndim)
    - 형태 - `ndarray.shape` 속성
    - 차원 - `ndarray.ndim` 속성

      ![alt text](image-7.png)

    - (2, 3) shape을 가지는 모든 원소가 1, dtype은 int32인 ndarray 생성
      ```python
      array2 = np.array([[1, 2, 3],
                        [4, 5, 6]])

      print("array2:")
      print(array2)
      print("Shape:", array2.shape)
      print("차원 수 (ndim):", array2.ndim)
      ```
      ![alt text](image-6.png)
    
  - 차원과 크기 변경 - `reshape()`
    - 즉, 배열의 모양을 바꾼다
      ```python
      
      array1 = np.arange(10)
      print('array1:\n', array1)

      # (2, 5)로 reshape
      array2 = array1.reshape(2, 5)
      print('array2:\n', array2)

      # (5, 2)로 reshape
      array3 = array1.reshape(5, 2)
      print('array3:\n', array3)

      # (4, 3)으로 reshape 시도 - 오류 발생
      # array1.reshape(4, 3)  # ValueError 발생
      ```
      ![alt text](image-9.png)
    
  - 차원과 크기 변경 - `reshape(-1, N)`
    - -1에 해당하는 axis의 크기는 가변적
    - -1이 아닌 인자 값에 해당하는 axis 크기는 인자 값으로 고정하여 shape 변환
      ```python
      array1 = np.arange(10)

      # 자동 계산 가능한 경우
      array2 = array1.reshape(-1, 5)
      print('array2 shape:', array2.shape)

      array3 = array1.reshape(5, -1)
      print('array3 shape:', array3.shape)

      # 자동 계산 불가능한 경우 - 오류 발생
      # array4 = array1.reshape(-1, 4)  # ValueError 발생
      ```
      ![alt text](image-10.png)

      에러 이유 설명
    
  - axis (축)
    - 행, 열, 높이 단위 XX
    - axis0, axis1, axis2와 같이 axis 단위로 부여
      - axis0: 배열의 가장 바깥쪽..

      ![alt text](image-8.png)
    
    - (2, 3) shape을 가지는 모든 원소가 1, dtype은 int32인 ndarray 생성

- DataFrame과 Numpy/List/Dictionary 상호변환
  - `Numpy/List/Dictionary -> DataFrame`
    - List -> DataFrame
      ```python
      list2_df = pd.DataFrame(list, columns = col_name)
      ```
    - Numpy(ndarray) -> DataFrame
      ```python
      np2_df = pd.DataFrame(ndarray, columns=col_name)
      ```
    - Dictionary -> DataFrame
      ```python
      dict = {'col1': [1, 11], 'col2': [2, 22]}
      dict2_df = pd.DataFrame(dict)
      ```
  
  - `DataFrame -> Numpy/List/Dictionary`
    - DataFrame -> List
      ```
      DataFrame 객체의 values 속성을 이용하여 먼저 ndarray로 변환 후 tolist()를 이용하여 list로 변환
      ```
    - DataFrame -> Numpy(ndarray)
      ```
      DataFrame 객체의 values 속성을 이용하여 ndarray로 변환
      ```
    - DataFrame -> Dictionary
      ```
      DataFrame 객체의 to_dict()를 이용하여 변환
      ```


## 데이터 처리와 집계
### 데이터 처리
- 객체 생성
  - Default index인 `RangeIndex`를 사용한 객체 생성
    ```python
    import numpy as np
    import pandas as pd

    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    ```
    ![alt text](image-11.png)
  
  - datetime index를 사용한 객체 생성
    ```python
    dates = pd.date_range("20130101", periods=6)
    print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df)
    ```
    ![alt text](image-12.png)

  - 딕셔너리를 사용한 객체 생성
    ```python
    df2 = pd.DataFrame({
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    })
    print(df2)
    ```
    ![alt text](image-13.png)

- 데이터 확인
  - 타입 확인
    ```python
    print(df2.dtypes)
    ```
    ![alt text](image-14.png)

  - 데이터프레임 확인
    ```python
    print(df.head())     # 상위 5개 행
    print(df.tail(3))    # 하위 3개 행
    ```
    ![alt text](image-15.png)

  - index, column 확인
    ```python
    print(df.index)
    print(df.columns)
    ```
    ![alt text](image-16.png)

  - DataFrame을 numpy로 변환
    ```python
    print(df.to_numpy())
    ```
    ![alt text](image-17.png)
  
  - 통계 정보 확인
    ```python
    print(df.describe())
    ```
    ![alt text](image-18.png)
  
  - `Transpose` 연산
    ```python
    print(df.T)
    ```
    ![alt text](image-19.png)

### 데이터 선택
- label을 활용한 데이터 선택
  - DataFrame에서 Series 데이터 추출
    ```python
    print(df["A"])
    ```
    ![alt text](image-20.png)

  - DataFrame에서 slice 사용하여 행들 추출
    ```python
    df[0:3]

    df["20130102":"20130104"]
    ```
    ![alt text](image-21.png)
    ![alt text](image-22.png)
  
  - DataFrame에서 slice 사용하여 행들 추출 (label slice)
    ```python
    df.loc["20130102":"20130104", ["A", "B"]]
    ```
    ![alt text](image-23.png)
  
  - 특정 행과 열에 있는 scalar 값 추출
    ```python
    df.loc[dates[0], "A"]       # 위치 기반 접근
    df.at[dates[0], "A"]        # 가장 빠른 방식
    ```
    ![alt text](image-24.png)

- position을 활용한 데이터 선택
  ```python
  df.iloc[3]                  # 4번째 행 전체
  df.iloc[3:5, 0:2]           # 4~5번째 행, 1~2번째 열
  df.iloc[[1, 2, 4], [0, 2]]  # 특정 행/열 조합
  df.iloc[1:3, :]             # 2~3번째 행, 전체 열
  df.iloc[:, 1:3]             # 전체 행, 2~3번째 열
  df.iloc[1, 1]               # 2행 2열 값
  df.iat[1, 1]                # 빠른 2행 2열 접근
  ```
  ![alt text](image-28.png)

  ![alt text](image-25.png)

- boolean을 활용한 indexing
  ```python
  df[df["A"] > 0]             # A 열이 0보다 큰 행만

  df[df > 0]                 # 전체 DataFrame에서 양수만 표시, 나머지는 NaN
  ```
  ![alt text](image-26.png)

  ![alt text](image-27.png)

  ```python
  df2 = df.copy()
  df2["E"] = ["one", "one", "two", "three", "four", "three"]

  df2[df2["E"].isin(["two", "four"])]
  ```
  ![alt text](image-29.png)

### 데이터 정렬
- `sort_values()`
  - 오름차순이 기본 (`ascending=True`)
  - 내림차순 정렬 시 `ascending=False` 설정
    ```python
    # 이름 기준 오름차순 정렬
    titanic_sorted = titanic_df.sort_values(by=['Name'])
    titanic_sorted.head(3)

    # Pclass와 Name 기준 내림차순 정렬
    titanic_sorted = titanic_df.sort_values(by=['Pclass', 'Name'], ascending=False)
    titanic_sorted.head(3)
    ```
    ![alt text](image-30.png)

### 데이터 고유값 파악
- `unique()`
  - 컬럼 내 몇건의 고유값이 있는지 파악
    ```python
    print(titanic_df['Pclass'].nunique())
    print(titanic_df['Survived'].nunique())
    print(titanic_df['Name'].nunique())
    ```
    ![alt text](image-31.png)    

### 데이터 집계
- DataFrame, Series에서 집계(Aggregation) 수행
  - `count()`
    ```python
    titanic_df.count()
    ```
    ![alt text](image-32.png)

  - `mean()`
    ```python
    # 평균
    titanic_df[['Age', 'Fare']].mean()
    ```
    ![alt text](image-33.png)
  
  - `sum()`
    ```python
    # 합계
    titanic_df[['Age', 'Fare']].sum()
    ```
    ![alt text](image-34.png)
  
  - `min()`
    ```python
    # 최솟값
    titanic_df[['Age', 'Fare']].min()
    ```
    ![alt text](image-35.png)

- DataFrame 그룹화
  - `groupby()`
    - 데이터를 특정 컬럼을 기준으로 묶은 후, 해당 그룹에 대해 집계 연산 수행

    - groupby() 수행 후 DataFrameGroupBy 객체 반환
      ```python
      # groupby 객체 생성
      titanic_groupby = titanic_df.groupby('Pclass')
      ```
    - 반환된 DataFrameGroupBy 객체에 대해 다양한 집계함수 적용
      ```python
      # Age와 Fare에 대해 count
      titanic_groupby[['Age', 'Fare']].count()
      ```
      ![alt text](image-36.png)
    
  - 동일한 컬럼에 대해 서로 다른 집계함수를 적용하고 싶은 경우 `agg()` 활용
    ```python
    # 최대값과 최소값을 나란히 출력
    titanic_df.groupby('Pclass')['Age'].max(), titanic_df.groupby('Pclass')['Age'].min()

    # max, min 함께 보기
    titanic_df.groupby('Pclass')['Age'].agg([max, min])
    ```
    ![alt text](image-37.png)
    ![alt text](image-38.png)

    ```python
    titanic_df.groupby(['Pclass']).agg(
        age_max=('Age', 'max'),
        age_mean=('Age', 'mean'),
        fare_mean=('Fare', 'mean')
    )      
    ```
    ![alt text](image-39.png)
    
  - 여러 컬럼에 여러 집계함수 적용 시 **`agg()` 내에 딕셔너리 형태로** 전달
    ```python
    agg_format = {
        'Age': 'max',
        'SibSp': 'sum',
        'Fare': 'mean'
    }
    titanic_df.groupby('Pclass').agg(agg_format)
    ```
    ![alt text](image-40.png)

### 데이터 가공
- lambda 식 이해
  ```python
  # 일반 함수
  def get_double(a):
    return a * 2
  
  # 람다식
  lambda_double = lambda x : x * 2
  ```

- `apply()`
  - lambda식을 결합하여 데이터를 일괄적으로 가공
    - 'Name_lem' -> 이름의 길이를 일괄 계산하여 추가
      ```python
      titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x: len(x))
      titanic_df[['Name', 'Name_len']].head(3)
      ```
      ![alt text](image-41.png)
    
    - 'Child_Adult' -> 나이가 15세 이하이면 Child, 그렇지 않으면 Adult
      ```python
      # 나이 기준으로 아동/성인 구분
      titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x: 'Child' if x <= 15 else 'Adult')
      titanic_df[['Age', 'Child_Adult']].head(8)
      ```
      ![alt text](image-42.png)

    - 나이에 따라 연령대 분류하는 함수
      ```python
      def categorize_age(age):
          """
          나이에 따라 연령대를 분류하는 함수
          """
          if age <= 5:
              return 'Baby'
          elif age <= 12:
              return 'Child'
          elif age <= 18:
              return 'Teenager'
          elif age <= 25:
              return 'Student'
          elif age <= 35:
              return 'Young Adult'
          elif age <= 60:
              return 'Adult'
          else:
              return 'Elderly'

      # 'Age' 컬럼의 값을 기반으로 연령대 분류 후 'Age_cate' 컬럼에 저장
      # categorize_age(x)는 'Age'값을 입력받아 해당 연력대 카테고리를 반환함
      titanic_df['Age_cate'] = titanic_df['Age'].apply(categorize_age)

      # 'Age'와 'Age_cate' 컬럼 확인
      titanic_df[['Age', 'Age_cate']].head()
      ```
      ![alt text](image-43.png)

## 데이터 병합 및 변환
### 데이터 병합
- concat
  ```python
  import pandas as pd

  df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']})

  df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

  df3 = pd.concat([df1, df2], axis=0)  # 행 병합
  df4 = pd.concat([df1, df2], axis=1)  # 열 병합

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df3)
  print('\n')
  print(df4)
  ```
  ![alt text](image-44.png)

- Inner Merge
  ```python
  import pandas as pd

  df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

  df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

  df_merged = pd.merge(df1, df2, on='key', how='inner')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-45.png)

- Outer Merge
  ```python
  import pandas as pd

  df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

  df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

  df_merged = pd.merge(df1, df2, on='key', how='outer')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-46.png)

- Left Merge
  ```python
  import pandas as pd

  df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

  df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

  df_merged = pd.merge(df1, df2, on='key', how='left')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-47.png)

- Right Merge
  ```python
  import pandas as pd

  df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

  df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']})

  df_merged = pd.merge(df1, df2, on='key', how='right')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-48.png)

- join
  ```python
  import pandas as pd

  df1 = pd.DataFrame({
      'A': ['A0', 'A1', 'A2'],
      'B': ['B0', 'B1', 'B2']
  }, index=['K0', 'K1', 'K2'])

  df2 = pd.DataFrame({
      'C': ['C0', 'C1', 'C2'],
      'D': ['D0', 'D1', 'D2']
  }, index=['K0', 'K2', 'K3'])

  df_merged = df1.join(df2, how='left')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-49.png)

  - join 추가 예시
    ```python
    sales = pd.DataFrame({
        'customer_id': [1, 2, 3, 4],
        'product_id': [101, 102, 103, 104],
        'quantity': [5, 2, 3, 1]
    })

    customers = pd.DataFrame({
        'customer_id': [1, 2, 3, 5],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'city': ['Seoul', 'Busan', 'Daegu', 'Incheon']
    })

    sales = sales.set_index('customer_id')
    customers = customers.set_index('customer_id')

    merged_data = sales.join(customers, how='left')

    print(sales)
    print('\n')
    print(customers)
    print('\n')
    print(merged_data)
    ```
    ![alt text](image-50.png)

- 열 이름 변경
  ```python
  df1 = pd.DataFrame({
      'key': ['K0', 'K1', 'K2', 'K3'],
      'A': ['A0', 'A1', 'A2', 'A3'],
      'C': ['C0', 'C1', 'C2', 'C3']   # C열 추가
  })

  df2 = pd.DataFrame({
      'key': ['K0', 'K1', 'K2'],
      'C': ['C4', 'C5', 'C6'],    # C열 중복
      'D': ['D0', 'D1', 'D2']
  })

  df_merged = pd.merge(df1, df2, on='key', how='inner', suffixes=('_left', '_right'))

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-51.png)

- 불필요한 열 제거
  ```python
  df1 = pd.DataFrame({
      'key': ['K0', 'K1', 'K2', 'K3'],
      'A': ['A0', 'A1', 'A2', 'A3'],
      'B': ['B0', 'B1', 'B2', 'B3']
  })

  df2 = pd.DataFrame({
      'key': ['K0', 'K1', 'K2'],
      'C': ['C0', 'C1', 'C2'],
      'D': ['D0', 'D1', 'D2']
  })

  df_merged = pd.merge(df1, df2, on='key', how='inner')
  df_merged = df_merged.drop('B', axis=1)

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-52.png)

- 여러 열 기준 병합
  ```python
  df1 = pd.DataFrame({
      'key1': ['K0', 'K1', 'K2', 'K3'],
      'key2': ['K4', 'K5', 'K6', 'K7'],
      'A': ['A0', 'A1', 'A2', 'A3'],
      'B': ['B0', 'B1', 'B2', 'B3']
  })

  df2 = pd.DataFrame({
      'key1': ['K0', 'K1', 'K2'],
      'key2': ['K4', 'K5', 'K6'],
      'C': ['C0', 'C1', 'C2'],
      'D': ['D0', 'D1', 'D2']
  })

  df_merged = pd.merge(df1, df2, on=['key1', 'key2'], how='inner')

  print(df1)
  print('\n')
  print(df2)
  print('\n')
  print(df_merged)
  ```
  ![alt text](image-53.png)

### 데이터 변환
- `replace()`
  - 원본 값을 특정 값으로 대체
    ```python
    import numpy as np

    # 예: Titanic 데이터
    replace_test_df['Sex'] = replace_test_df['Sex'].replace({'male': 'Man', 'female': 'Woman'})
    print(replace_test_df.head(10))
    ```
    ![alt text](image-54.png)
  
  - 결측값 처리시에도 사용됨
    ```python
    # NaN을 특정 값으로 대체
    replace_test_df['Cabin'] = replace_test_df['Cabin'].replace(np.nan, 'CXXX')

    # Cabin별 값 개수 확인
    print(replace_test_df['Cabin'].value_counts(dropna=False))
    ```
    ![alt text](image-55.png)


## 추가
```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
print(df1)
```

```python
# 결측치가 있는 모든 행 제거
df1.dropna(how="any")

# 결측치를 5로 채우기
df1.fillna(value=5)
```