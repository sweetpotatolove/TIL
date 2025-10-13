# 기초 Python
## 🔹 `int`, `float`, `None`, `bool`, `str`
### 🔢 int (정수형)
정수 값을 저장하는 자료형

- 양수, 음수, 0 모두 표현 가능
- 크기 제한 없음XX
- 예시:
  ```python
  age = 30
  type(age)  # <class 'int'>
  ```
- 자주 사용하는 내장 함수
  | 함수          | 설명          | 예시                 |
  | ------------- | ----------- | ------------------ |
  | `abs(x)`      | 절댓값 반환      | `abs(-5)` → `5`    |
  | `round(x)`    | 반올림하여 정수 반환 | `round(3.6)` → `4` |
  | `pow(x, y)` 또는 `x ** y` | 거듭제곱 계산     | `2 ** 3` → `8`     |

### 🔣 float (부동소수점형)
소수점을 포함한 숫자

- 파이썬의 `float`는 기본적으로 `double`(배정밀도) 수준의 정밀도를 가짐
- 예시:
  ```python
  height = 175.5
  type(height)  # <class 'float'>
  ```
- 유용한 내장 함수 / 모듈
  | 함수                                 | 설명            | 예시                                     |
  | ---------------------------------- | ------------- | -------------------------------------- |
  | `round(x, n)`                      | 소수점 n자리까지 반올림 | `round(3.14159, 2)` → `3.14`           |
  | `math.isclose(a, b, rel_tol=1e-5)` | 두 실수가 근사한지 비교 | `math.isclose(3.14, math.pi)` → `True` |
  | `math.sqrt(x)`                     | 제곱근 계산        | `math.sqrt(9)` → `3.0`                 |

### 🚫 None (값 없음)
값이 없음을 명시적으로 나타내는 객체

- 조건문에서 False로 평가됨
- 반환값이 없는 함수의 결과도 None
- 예시:
  ```python
  nothing = None
  print(type(nothing))  # <class 'NoneType'>
  ```

### ☝️ bool (불리언형)
논리형(True/False) 값을 표현

- 조건문, 비교연산, 논리연산 등에 사용
- 예시:
  ```python
  is_student = True
  type(is_student)  # <class 'bool'>
  ```
- 자주 사용하는 연산자
  | 연산자   | 설명                    | 예시                         |
  | ----- | --------------------- | -------------------------- |
  | `and` | 두 조건이 모두 True일 때 True | `True and False` → `False` |
  | `or`  | 하나라도 True면 True       | `True or False` → `True`   |
  | `not` | 반대값 반환                | `not True` → `False`       |

### 📝 str (문자열형)
문자들의 집합

- `' '` 또는 `" "`로 감싸서 표현
- 파이썬의 문자열은 `immutable`(불변) 객체임
- 예시:
  ```python
  name = "김철수"
  greeting = '안녕하세요!'
  type(name)  # <class 'str'>
  ```
- 문자열 관련 주요 메서드
  | 메서드                 | 설명                  | 예시                             |
  | ------------------- | ------------------- | ------------------------------ |
  | `str.lower()`       | 모든 문자를 소문자로         | `"Hello".lower()` → `"hello"`  |
  | `str.upper()`       | 모든 문자를 대문자로         | `"Hello".upper()` → `"HELLO"`  |
  | `str.endswith(sub)` | 특정 문자열로 끝나는지 확인     | `"Hi!".endswith("!")` → `True` |
  | `str.isdigit()`     | 문자열이 숫자로만 구성되었는지 확인 | `"123".isdigit()` → `True`     |
  | `+`                 | 문자열 연결              | `"Hi" + "!"` → `"Hi!"`         |
  | `*`                 | 문자열 반복              | `"Hi" * 3` → `"HiHiHi"`        |

### 💡 참고: 동적 타이핑과 타입 힌트
- 파이썬은 변수 선언 시 자료형을 명시하지 않음
  ```python
  count = 10  # 자동으로 int로 인식
  ```

- 하지만, 협업 시 코드 가독성을 위해 **타입 힌트(type hint)**를 권장
  ```python
  count: int = 10
  name: str = "철수"
  ```