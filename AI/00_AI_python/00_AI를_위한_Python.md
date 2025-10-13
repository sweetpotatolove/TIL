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

- 하지만, 협업 시 코드 가독성을 위해 **타입 힌트(type hint)** 를 권장
  ```python
  count: int = 10
  name: str = "철수"
  ```


## 🔹 `list`, `tuple`, `set`, `dict`
### 📋 List (리스트)
순서가 있고, 변경 가능한(mutable) 자료형

- 서로 다른 타입의 데이터를 함께 저장할 수 있음
- 예시:
  ```python
  my_list = [1, 2, 'apple', True]
  ```
- 리스트 특징
  - 인덱스로 접근 가능 (`my_list[0]`)
  - 수정, 추가, 삭제 가능
  - 슬라이싱(`my_list[1:3]`), 연결(`+`), 반복(`*`) 가능
- 리스트 메서드 및 함수
  | 함수/메서드                     | 설명              | 예시                            |
  | -------------------------- | --------------- | ----------------------------- |
  | `len(l)`                   | 리스트 길이          | `len([1,2,3]) → 3`            |
  | `x in l`                   | 값 포함 여부         | `3 in [1,2,3] → True`         |
  | `l.append(x)`              | 맨 뒤에 요소 추가      | `[1,2].append(3)` → `[1,2,3]` |
  | `l.extend(l2)` / `l += l2` | 리스트 병합          | `[1,2] + [3,4]` → `[1,2,3,4]` |
  | `l.insert(i, x)`           | 특정 위치에 삽입       | `l.insert(2, 5)`              |
  | `l.remove(x)`              | 첫 번째로 등장하는 x 삭제 | `[1,2,3].remove(2)`           |
  | `l.pop()`                  | 마지막 요소 제거 후 반환  |                               |
  | `l.index(x)`               | x의 인덱스 반환       |                               |
  | `l.count(x)`               | x 등장 횟수 반환      |                               |
  | `l.reverse()`              | 리스트 뒤집기         |                               |
  | `l.clear()`                | 모든 요소 제거        |                               |
  | `max(l), min(l)`           | 최댓값, 최솟값 반환     |                               |

### 📦 Tuple (튜플)
순서가 있지만 변경 불가능(immutable) 한 자료형

- 리스트보다 메모리 효율적이며, 안전하게 데이터 보관 가능
- 예시:
  ```python
  my_tuple = (10, 20, 'cherry')
  ```
- 튜플 특징
  - 인덱싱, 슬라이싱 가능
  - 단, 요소 수정·삭제 불가능
  - 리스트와 달리 `append`, `remove` 등의 메서드 없음
- 튜플 함수
  | 함수                   | 설명         | 예시                          |
  | -------------------- | ---------- | --------------------------- |
  | `len(t)`             | 원소 개수      | `len((1,2,3)) → 3`          |
  | `x in t`             | 포함 여부 확인   | `2 in (1,2,3) → True`       |
  | `t + t2`             | 튜플 병합      | `(1,2)+(3,4)` → `(1,2,3,4)` |
  | `t.count(x)`         | 특정 값 등장 횟수 | `(1,1,2).count(1)` → `2`    |
  | `t.index(x)`         | 특정 값의 인덱스  | `(1,2,3).index(2)` → `1`    |
  | `tuple(reversed(t))` | 뒤집은 튜플 생성  | `(1,2,3)` → `(3,2,1)`       |

### 🧮 Set (세트)
순서가 없고, 중복을 허용하지 않는 자료형

- 집합 연산(합집합, 교집합, 차집합 등)에 자주 사용됨
- 예시:
  ```python
  my_set = {1, 2, 3, 2, 1}
  # 결과: {1, 2, 3}
  ```
- 집합 특징
  - 인덱싱 불가 (순서 없음)
  - `+` 연산 불가능
  - 요소의 중복이 자동으로 제거됨
- set 메서드 및 연산
  | 함수/연산            | 설명          | 예시                            |        |                  |
  | ---------------- | ----------- | ----------------------------- | ------ | ---------------- |
  | `len(s)`         | 원소 수        | `len({1,2,3}) → 3`            |        |                  |
  | `x in s`         | 포함 여부       | `2 in {1,2,3}` → `True`       |        |                  |
  | `s.add(x)`       | 요소 추가       | `{1,2}.add(3)` → `{1,2,3}`    |        |                  |
  | `s.remove(x)`    | 요소 삭제       | `{1,2,3}.remove(2)`           |        |                  |
  | `s.clear()`      | 모든 요소 제거    |                               |        |                  |
  | `s & s2`         | 교집합         | `{1,2,3} & {2,3,4}` → `{2,3}` |        |                  |
  | `s ｜ s2`         | 합집합                           | `{1,2} ｜ {2,3}`→`{1,2,3}` |
  | `s - s2`         | 차집합         | `{1,2,3} - {2}` → `{1,3}`     |        |                  |
  | `s ^ s2`         | 대칭차집합       | `{1,2,3} ^ {2,3,4}` → `{1,4}` |        |                  |
  | `max(s), min(s)` | 최댓값, 최솟값 반환 |                               |        |                  |

### 🗂️ Dict (딕셔너리)
**키(key)** 와 **값(value)** 쌍으로 구성된 자료형

- 키는 중복 불가, 값은 중복 가능
- Python 3.7 이후부터는 삽입 순서 유지
- 예시:
  ```python
  my_dict = {'name': '김영희', 'age': 25, 'city': '서울'}
  ```
- 딕셔너리 주요 기능
  | 함수/메서드                | 설명                   | 예시                        |
  | --------------------- | -------------------- | ------------------------- |
  | `len(d)`              | 원소 개수                | `len({'a':1,'b':2}) → 2`  |
  | `d.keys()`            | 모든 키 반환              |                           |
  | `d.values()`          | 모든 값 반환              |                           |
  | `d.items()`           | (키, 값) 쌍 반환          |                           |
  | `x in d`              | 키 존재 여부 확인           | `'a' in {'a':1}` → `True` |
  | `d.get(key, default)` | 키가 없을 때 오류 대신 기본값 반환 | `d.get('x', 0)`           |
  | `d.pop(key)`          | 키-값 삭제 후 값 반환        |                           |
  | `d.clear()`           | 모든 항목 삭제             |                           |
  | `{**d1, **d2}`        | 두 딕셔너리 병합            |                           |

### 💡 딕셔너리 확장
- `defaultdict`
  - 키가 없을 때 자동으로 기본값을 생성하는 딕셔너리
  - 예시:
    ```python
    from collections import defaultdict
    dd = defaultdict(int)
    dd['apple'] += 1  # KeyError 없이 동작
    ```

- `Counter`
  - 반복 가능한 객체에서 요소의 빈도수를 세어주는 딕셔너리
  - 예시:
    ```python
    from collections import Counter
    fruits = ['apple', 'banana', 'apple', 'banana']
    Counter(fruits)  # {'apple': 2, 'banana': 2}
    ```

## 🔹 조건문 / 반복문
### ✅ 조건문 `if`
조건문은 특정 조건이 참(True)일 때만 코드를 실행함

- 조건에는 `boolean` 값으로 평가될 수 있는 표현식이 들어가야 함
- 예시:
  ```python
  score = 85

  if score >= 90:
      print("학점: A")
  elif score >= 80:
      print("학점: B")
  elif score >= 70:
      print("학점: C")
  else:
      print("학점: D")
  ```
- 핵심 문법
  - `if 조건:` : 조건이 True일 때 실행
  - `elif 조건:` : 위 조건이 False이고, 새로운 조건이 True일 때 실행
  - `else:` : 위의 모든 조건이 False일 때 실행
- 논리 연산자
  | 연산자   | 의미         | 예시                       |
  | ----- | ---------- | ------------------------ |
  | `and` | 두 조건이 모두 참 | `age >= 19 and has_card` |
  | `or`  | 하나라도 참     | `a > 10 or b < 5`        |
  | `not` | 조건 반전      | `not True` → `False`     |

### 🔁 반복문 `for`, `while`
- `for` 루프
  - **순회 가능한 객체(iterable)** (리스트, 문자열 등)을 대상으로 반복
  - 인덱스 없이 바로 요소를 꺼내서 사용 가능
  - 예시:
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    ```

- `range()`와 함께 사용하기
  - 일정 횟수만큼 반복할 때 유용
  - `range(start, stop, step)`
  - 예시:
    ```python
    for i in range(5):      # 0~4
        print(i)

    for i in range(2, 11, 2):  # 2, 4, 6, 8, 10
        print(i)
    ```

- `while` 루프
  - 조건이 `True`인 동안 계속 반복
  - 반드시 종료 조건 필요 (무한루프 방지)
  - 예시:
    ```python
    count = 5
    while count > 0:
        print(count)
        count -= 1
    print("발사!")
    ```

### 🚦 반복 제어문 `break`, `continue`
| 키워드        | 설명                     | 예시                    |
| ---------- | ---------------------- | --------------------- |
| `break`    | 반복문을 즉시 종료             | `if i == 7: break`    |
| `continue` | 현재 반복만 건너뛰고 다음 반복으로 이동 | `if i == 3: continue` |

- 예시:
  ```python
  for i in range(10):
      if i == 3:
          continue  # 3은 건너뜀
      if i == 7:
          break     # 루프 종료
      print(i)
  ```

### 🧩 리스트 컴프리헨션 (List Comprehension)
**반복문을 한 줄로 간결하게 표현**할 수 있는 파이썬 문법

- 형식
  ```python
  [표현식 for 변수 in 반복가능객체 if 조건]
  ```
- 예시1:
  ```python
  squares = [x**2 for x in range(10)]
  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  even_numbers = [x for x in range(20) if x % 2 == 0]
  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
  ```
  - 예시2:
    | 목적         | 예시                                         |
    | ---------- | ------------------------------------------ |
    | 제곱 리스트 만들기 | `[x**2 for x in range(10)]`                |
    | 짝수만 필터링    | `[x for x in range(10) if x % 2 == 0]`     |
    | 문자열 길이 구하기 | `[len(word) for word in ["hi", "python"]]` |

### 🔗 `itertools`
itertools는 반복(Iteration)을 다루는 표준 라이브러리

- 조합, 순열, 누적합 등 복잡한 반복 패턴을 간단히 구현할 수 있음
- 주요 함수
  | 함수               | 설명             | 예시                                                                 |
  | ---------------- | -------------- | ------------------------------------------------------------------ |
  | `product()`      | 데카르트 곱 (모든 조합) | `product([1,2], ['A','B'])` → `(1,'A'), (1,'B'), (2,'A'), (2,'B')` |
  | `permutations()` | 순열 (순서 있음)     | `permutations([1,2,3], 2)` → `(1,2), (1,3), ...`                   |
  | `combinations()` | 조합 (순서 없음)     | `combinations([1,2,3], 2)` → `(1,2), (1,3), (2,3)`                 |
  | `accumulate()`   | 누적 연산 (합, 곱 등) | `accumulate([1,2,3]) → [1,3,6]`                                    |
  | `groupby()`      | 조건에 따라 그룹화     | `groupby(data, key=...)`                                           |
- 예시:
  ```python
  from itertools import product, permutations, combinations, accumulate
  import operator

  # 모든 조합
  list(product([1, 2], ['A', 'B']))  # [(1,'A'), (1,'B'), (2,'A'), (2,'B')]

  # 순열
  list(permutations([1, 2, 3], 2))   # [(1,2), (1,3), (2,1), (2,3), ...]

  # 조합
  list(combinations([1, 2, 3], 2))   # [(1,2), (1,3), (2,3)]

  # 누적합 / 누적곱
  list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
  list(accumulate([1, 2, 3, 4], func=operator.mul))  # [1, 2, 6, 24]
  ```


## 🔹 함수 사용하기 (Function)
### 🔸 기본 함수 정의 & 호출
- `def` 키워드를 사용하여 함수를 정의함
- 함수 이름 뒤에 괄호 `()`와 콜론 `:`을 붙여야함
- 내부 코드는 **들여쓰기(tab)** 로 구분
- 예시:
  ```python
  def greet():
      """간단한 환영 메시지를 출력하는 함수"""
      print("안녕하세요!")

  greet()
  ```

### 🔸 매개변수(Parameter)와 인자(Argument)
- 함수 호출 시 인자를 전달하면 매개변수가 그 값을 받음
- 예시:
  ```python
  def greet_name(name):
      """이름을 받아 환영 메시지를 출력"""
      print(f"안녕하세요, {name}님!")

  greet_name(name="제니")
  ```
  - Keyword argument 방식(ex. `name="제니"`)은 코드 가독성을 높임

### 🔸 반환값(Return)
- `return` 키워드를 사용하면 함수가 계산 결과를 호출한 곳으로 반환함
- 예시:
  ```python
  def add(a, b):
      return a + b

  result = add(5, 3)
  print(result)  # 8
  ```

### 🔸 기본 매개변수(Default Parameter)
- 매개변수에 기본값을 지정하면, 호출 시 생략해도 그 값을 사용함
- 예시:
  ```python
  def greet_language(name, lang="Python"):
      print(f"{lang}을 사용하시는 {name}님, 안녕하세요!")

  greet_language(name="KIM")           # 기본값 사용
  greet_language(name="CHOI", lang="Java")  # 값 재정의
  ```

### 🔸 가변 인자 `*args`
- 개수가 정해지지 않은 인자를 받을 때 사용
- 모든 인자가 **튜플(tuple)** 형태로 전달
- 예시:
  ```python
  def sum_all(*args):
      total = 0
      for num in args:
          total += num
      return total

  sum_all(1, 2, 3)  # 6
  sum_all(1, 2, 3, 4, 5)  # 15
  ```

### 🔸 키워드 인자 `**kwargs`
- 이름이 지정된 인자를 딕셔너리 형태로 받음
- 예시:
  ```python
  def print_info(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")

  print_info(name="LEE", age=2, city="LA")

  # 출력
  # name: LEE  
  # age: 2  
  # city: LA
  ```

### 🔸 람다 함수 (Lambda Function)
- 이름이 없는 익명 함수
- 간단한 연산이나 함수를 한 줄로 표현할 때 사용
- 예시:
  ```python
  square = lambda x: x * x
  print(square(5))  # 25
  ```

### 🔸 중첩 함수(Nested Function)와 클로저(Closure)
- 함수 안에 또 다른 함수를 정의 가능
- 내부 함수는 외부 함수의 변수에 접근할 수 있음
- 예시:
  ```python
  def outer_function(x):
      def inner_function(y):
          return x + y
      return inner_function

  add_five = outer_function(5)
  print(add_five(3))  # 8
  ```
  - `inner_function`은 `x`의 값을 기억하므로 이를 **클로저(closure)** 라고 함

### 🔸 Docstring (함수 설명 문서)
- 함수 바로 아래에 `"""` 삼중 따옴표로 설명을 작성
- `__doc__` 속성을 통해 확인 가능
- Java의 Javadoc과 유사한 문서화 방식임
- 예시:
  ```python
  def multiply(a, b):
      """
      두 숫자를 곱하는 함수.

      Args:
          a: 첫 번째 숫자
          b: 두 번째 숫자
      Returns:
          두 숫자의 곱
      """
      return a * b

  print(multiply.__doc__)
  ```

### 🧾 PEP 8 (Python Enhancement Proposals)
파이썬 코드 스타일 가이드로, “가독성 좋은 코드”를 위한 권장 표준

1. 띄어쓰기(공백)
    ```python
    # ❌
    a=1
    a+=1
    x=a * 2-1

    # ✅
    a = 1
    a += 1
    x = a * 2 - 1
    ```

2. 줄바꿈 위치 (Line Break)
    ```python
    # ❌
    income = (gross_wages +
              taxable_interest +
              (dividends - qualified_dividends) -
              ira_deduction -
              student_loan_interest)

    # ✅
    income = (gross_wages
              + taxable_interest
              + (dividends - qualified_dividends)
              - ira_deduction
              - student_loan_interest)
    ```

3. 키워드 인자 사용
    ```python
    # 함수 호출 시 인자 이름을 명시적으로 써줘야 가독성 높아짐
    def do_something(user_id, verbose):
        ...

    # ❌
    do_something(42, True)

    # ✅
    do_something(user_id=42, verbose=True)
    ```

### 💡 예제 응용: 문자열 속 숫자 합 구하기
```python
def sum_of_digits_in_string(s: str) -> int:
    """문자열에 포함된 숫자(digit)들의 합 반환"""
    return sum(int(ch) for ch in s if ch.isdigit())

sum_of_digits_in_string("a1b2c3")  # 6
```


## 🔹 Python을 이용한 객체지향 프로그래밍 (OOP)
### 🔸 클래스(Class) 기본 구조
클래스는 속성(변수)과 메서드(함수)를 묶은 설계도

- Python에서 객체(Object)는 클래스(Class) 로 정의함
- 기본 구조
  ```python
  class Dog:
      def __init__(self, name, breed):
          self.name = name      # 인스턴스 변수
          self.breed = breed    # 인스턴스 변수

      def bark(self):
          print(f"{self.name}가 멍멍 짖습니다!")

      def __str__(self):
          return f"이름: {self.name}, 품종: {self.breed}"
  ```
  - 핵심 개념 요약
    | 용어         | 설명                                   |
    | ---------- | ------------------------------------ |
    | `__init__` | 생성자 (객체 초기화 시 자동 호출)                 |
    | `self`     | 인스턴스 자신을 가리킴 (`this`와 유사한 개념)        |
    | 인스턴스 변수    | `self.`로 선언된 속성                      |
    | 메서드        | 클래스 내부의 함수                           |
    | `__str__`  | 객체를 문자열로 표현할 때 호출 (`print()`시 자동 실행) |
- 사용 예시:
  ```python
  my_dog = Dog(name="바둑이", breed="진돗개")
  my_dog.bark()
  print(my_dog)   # → 이름: 바둑이, 품종: 진돗개
  ```

### 🔸 상속 (Inheritance)
기존 클래스를 확장해 새로운 클래스를 만드는 방식

- `super()` 를 통해 부모 클래스의 속성과 메서드를 호출 가능
- 기본 구조
  ```python
  class Puppy(Dog):
      def __init__(self, name, breed, age):
          super().__init__(name, breed)  # 부모 생성자 호출
          self.age = age

      def bark(self):  # 메서드 오버라이딩
          print(f"{self.name}가 낑낑거립니다!")

      def __str__(self):
          return f"이름: {self.name}, 품종: {self.breed}, 나이: {self.age}개월"
  ```
  - 핵심 개념
    | 개념                | 설명                            |
    | ----------------- | ----------------------------- |
    | 상속(Inheritance)   | 부모 클래스의 속성과 메서드를 자식 클래스가 물려받음 |
    | `super()`         | 부모 클래스의 메서드나 생성자 호출           |
    | 오버라이딩(Overriding) | 부모 메서드를 재정의하여 자식에 맞게 수정       |

### 🔸 캡슐화 (Encapsulation)
데이터 보호를 위한 개념

- Python에는 `private` 키워드가 없지만, **이름 앞에 `_` 또는 `__`** 를 붙여 비공개 속성을 표현함
- 사용 예시:
  ```python
  class BankAccount:
      def __init__(self, balance):
          self.__balance = balance  # private 변수

      def deposit(self, amount):
          if amount > 0:
              self.__balance += amount

      def withdraw(self, amount):
          if 0 < amount <= self.__balance:
              self.__balance -= amount

      def get_balance(self):
          return self.__balance
  ```
  - 핵심 개념
    | 기호            | 의미                         |
    | ------------- | -------------------------- |
    | `_var`        | 내부 사용용 변수 (비공식적 접근 금지)     |
    | `__var`       | 강한 캡슐화 (이름 맹글링, 외부 접근 어려움) |
    | getter/setter | 값 접근/수정용 메서드 제공            |

### 🔸 매직 메서드 (Magic Method)
이름 앞뒤에 `__`가 붙은 메서드로, 연산자나 내장 함수의 동작을 정의함

| 메서드           | 설명              | 예시            |
| ------------- | --------------- | ------------- |
| `__init__`    | 생성자             | 객체 생성 시 자동 호출 |
| `__str__`     | 문자열 표현          | `print(obj)`  |
| `__add__`     | `+` 연산자 정의      | `obj1 + obj2` |
| `__len__`     | `len()` 호출 시 동작 |               |
| `__getitem__` | 인덱싱 시 동작        | `obj[key]`    |
| `__eq__`      | `==` 연산자 정의     |               |

- 예시:
  ```python
  class Vector:
      def __init__(self, x, y):
          self.x = x
          self.y = y

      def __add__(self, other):
          return Vector(self.x + other.x, self.y + other.y)

      def __str__(self):
          return f"({self.x}, {self.y})"

  v1 = Vector(1, 2)
  v2 = Vector(3, 4)
  print(v1 + v2)  # (4, 6)
  ```

### 💡 Python에서 "모든 것은 객체"
Python의 모든 데이터는 클래스의 인스턴스 !!
```python
print(type(10))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
```
- 즉, `int`, `str`, `list`, `dict` 등은 전부 클래스
  - 내부에 특수 메서드(Magic Method) 가 정의되어 있음


# 데이터 분석 도구: NumPy & Pandas
## 🔹 NumPy
NumPy(Numerical Python)는 대규모 수치 데이터를 빠르게 처리하기 위한 배열 기반 라이브러리

- Python의 `list`보다 연산 속도가 매우 빠름
- 벡터, 행렬, 통계 연산 등 데이터 분석 및 머신러닝의 기초 라이브러리

### 🔸 배열 생성
| 함수                                   | 설명              | 예시                           |
| ------------------------------------ | --------------- | ---------------------------- |
| `np.array()`                         | 리스트나 튜플을 배열로 변환 | `np.array([1,2,3])`          |
| `np.zeros()`                         | 0으로 채워진 배열 생성   | `np.zeros((2,3))`            |
| `np.ones()`                          | 1로 채워진 배열 생성    | `np.ones((3,3))`             |
| `np.eye()`                           | 단위행렬 생성         | `np.eye(3)`                  |
| `np.arange(start, stop, step)`       | 일정 간격으로 수 생성    | `np.arange(0,10,2)`          |
| `np.linspace(start, stop, num)`      | 구간을 균등분할        | `np.linspace(0,1,5)`         |
| `np.random.randint(low, high, size)` | 정수 난수 생성        | `np.random.randint(0,100,5)` |
| `np.random.randn(m, n)`              | 표준정규분포 난수 생성    | `np.random.randn(3,3)`       |

### 🔸 배열 연산
- NumPy 배열은 벡터화 연산(Vectorized Operation) 을 지원함
- 즉, 반복문 없이 한 번에 연산이 가능

| 연산                  | 설명        | 예시                  |
| ------------------- | --------- | ------------------- |
| `+`, `-`, `*`, `/`  | 원소별 사칙연산  | `a + b`, `a * 2`    |
| `np.dot(A, B)`      | 행렬곱       | `np.dot(A, B)`      |
| `A.T`               | 전치행렬      | `A.T`               |
| `A.astype(dtype)`   | 자료형 변환    | `A.astype(bool)`    |
| `np.allclose(a, b)` | 두 배열 값 비교 | `np.allclose(a, b)` |

### 🔸 주요 속성
| 속성      | 설명        |
| ------- | --------- |
| `shape` | 배열의 차원 크기 |
| `dtype` | 데이터 타입    |
| `ndim`  | 차원 수      |
| `size`  | 전체 원소 수   |

### 🔸 배열 조작
| 함수                           | 설명                |
| ---------------------------- | ----------------- |
| `np.reshape()`               | 배열 형태 변경          |
| `np.flatten()`               | 다차원 배열 → 1차원으로 변환 |
| `np.concatenate()`           | 배열 연결             |
| `np.tile(x, (m, n))`         | 배열 반복             |
| `np.vstack()`, `np.hstack()` | 세로/가로 방향으로 배열 연결  |

- 예시:
  ```python
  v = np.array([1, 2, 3])
  V = np.tile(v, (3, 1))   # [[1,2,3],[1,2,3],[1,2,3]]
  V_vector = V.flatten()   # [1,2,3,1,2,3,1,2,3]
  ```

### 🔸 수학 및 통계 함수
| 함수                                 | 설명        |
| ---------------------------------- | --------- |
| `np.sum()`, `np.mean()`            | 합계, 평균    |
| `np.std()`, `np.var()`             | 표준편차, 분산  |
| `np.min()`, `np.max()`             | 최소값, 최대값  |
| `np.sin()`, `np.cos()`, `np.tan()` | 삼각함수      |
| `np.exp()`, `np.log()`             | 지수, 로그 함수 |

- 예시:
  ```python
  theta = np.linspace(0, 2*np.pi, 100)
  sin_theta = np.sin(theta)
  ```
  - `np.linspace()`
    - 시작값부터 끝값까지 균등한 간격으로 지정한 개수만큼의 숫자를 생성하는 함수
    - 즉, "start부터 stop까지 num개의 점을 일정 간격으로 찍는" 역할
    - 구조
      ```python
      np.linspace(start, stop, num=50, endpoint=True, dtype=None)
      ```
    - 주요 파라미터:
      - `start` : 시작값
      - `stop` : 끝값
      - `num` : 생성할 숫자의 개수 (기본값: 50)
      - `endpoint` : True면 stop을 포함, False면 stop 직전까지 (기본값: True)
      - `dtype : 반환할 배열의 자료형 지정 (생략 시 자동 추론)


## 🔹 Pandas
Pandas는 Python에서 **표 형태(행과 열)** 의 데이터를 다루기 위한 핵심 라이브러리

- "Panel + Data"의 합성어
- 데이터를 생성·탐색·분석·정제(전처리)하는 데 매우 유용
- 엑셀, CSV, SQL DB, 웹 등 다양한 데이터 포맷 지원
- 행과 열로 구성된 DataFrame 구조 제공
- NumPy 기반으로, 고성능 수치 계산 지원

### 🔸 기본 구조
| 자료형         | 설명                | 예시                   |
| ----------- | ----------------- | -------------------- |
| `Series`    | 1차원 데이터 (인덱스 + 값) | `df["Age"]`          |
| `DataFrame` | 2차원 데이터 (행 + 열)   | `pd.DataFrame(data)` |

### 🔸 DataFrame 생성
1. 딕셔너리(Dictionary) 기반 생성
    - 가장 일반적
    - 가독성 좋음
    ```python
    import pandas as pd

    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "Score": [85.5, 90.3, 78.9]
    }
    df = pd.DataFrame(data)

    # | Name    | Age | Score |
    # | ------- | --- | ----- |
    # | Alice   | 25  | 85.5  |
    # | Bob     | 30  | 90.3  |
    # | Charlie | 35  | 78.9  |
    ```

2. List[Dict] 기반 생성
    - 각 행을 하나의 dict로 구성
    - JSON, API 응답 데이터 형태와 동일하기 때문에 가장 실무 친화적임
    ```python
    rows = [
        {"Name": "Alice", "Age": 25, "Score": 85.5},
        {"Name": "Bob", "Age": 30, "Score": 90.3},
        {"Name": "Charlie", "Age": 35, "Score": 78.9}
    ]
    df_1 = pd.DataFrame(rows)
    ```

3. List[List] + columns 기반 생성
    - 순수한 리스트 데이터로부터 생성할 수 있음
    - 열 이름을 columns로 별도 지정해야함
    ```python
    data = [
        ["Alice", 25, 85.5],
        ["Bob", 30, 90.3],
        ["Charlie", 35, 78.9]
    ]
    columns = ["Name", "Age", "Score"]

    df_2 = pd.DataFrame(data, columns=columns)
    ```

4. NumPy 배열(ndarray) 기반 생성
    - NumPy로 만든 수치 데이터를 DataFrame으로 변환 가능
    - 머신러닝 데이터셋 전처리 시 가장 자주 등장하는 방식
    ```python
    import numpy as np

    nums = np.array([
        [25, 85.5],
        [30, 90.3],
        [35, 78.9]
    ])
    names = ["Alice", "Bob", "Charlie"]

    df_3 = pd.DataFrame(nums, columns=["Age", "Score"])
    df_3.insert(0, "Name", names)
    df_3["Age"] = df_3["Age"].astype("int64")
    # | Name    | Age | Score |
    # | ------- | --- | ----- |
    # | Alice   | 25  | 85.5  |
    # | Bob     | 30  | 90.3  |
    # | Charlie | 35  | 78.9  |
    ```

### 🔸 데이터 탐색 (탐색적 분석 기초)
| 기능             | 코드                    | 설명                   |
| -------------- | --------------------- | -------------------- |
| **요약 정보 보기**   | `df.info()`           | 데이터 타입, 결측치, 메모리 사용량 |
| **통계 요약**      | `df.describe()`       | 평균, 표준편차, 분위수 등      |
| **크기 확인**      | `df.shape`            | (행, 열) 구조            |
| **컬럼명 확인**     | `df.columns.tolist()` | 모든 열 이름 리스트          |
| **인덱스 확인**     | `df.index`            | 행 인덱스 정보             |
| **상위 n행 미리보기** | `df.head(n)`          | 기본값 n=5              |

- 예시:
  ```python
  print(df.info())
  print(df.describe())
  print(df.shape)
  print(df.head(2))
  ```

### 🔸 데이터 접근
- 열(Column) 접근
  ```python
  df["Name"]               # 단일 컬럼
  df[["Name", "Score"]]    # 여러 컬럼
  ```
- 행(Row) 접근
  - `loc`
    - 인덱스 이름(Label) 기반 접근
    - 라벨(label) 을 기준으로 행과 열을 선택함
    - 즉, "이름으로 지정된 인덱스나 컬럼명" 사용
    - 특징
      - ① 인덱스가 문자열이더라도 접근 가능 (`df.loc["Alice"]`)
      - ② 슬라이싱 시 끝값 포함 (`0:1` → 0, 1 모두 포함)
    - 예시:
      ```python
      df.loc[0]                    # 인덱스 이름이 0인 행 전체
      df.loc[0, "Name"]            # 0행의 Name 컬럼
      df.loc[0:1, ["Name", "Age"]] # 0~1행, Name/Age 컬럼만
      ```
  
  - `iloc`
    - 정수 위치(Position) 기반 접근
    - 순서(index 위치 번호) 로 행과 열을 선택
    - 특징
      - ① 파이썬의 기본 인덱싱 규칙과 동일 (끝값 미포함)
      - ② 정수 위치 기반이므로, 인덱스 이름과 관계없이 동작함
    - 예시:
      ```python
      df.iloc[0]           # 첫 번째 행
      df.iloc[0, 1]        # 0행 1열 값
      df.iloc[0:2, 0:2]    # 0~1행, 0~1열 범위
      ```

- 값 단위 접근
  - `at`
    - 단일 셀(Label 기반, 고속)
    - `loc`과 동일하게 이름(label) 기준으로 접근하지만, 단일 값 하나만 가져올 때 훨씬 빠름
    - 특징
      - ① 단일 셀 전용 (슬라이싱 불가능)
      - ② loc보다 빠른 속도 (C-level 접근)
    - 예시:
      ```python
      df.at[0, "Age"]     # 인덱스 이름 0, 컬럼명 "Age" 위치의 값
      df.at[2, "Score"]   # 2행 Score 값
      ```
  
  - `iat`
    - 단일 셀(Position 기반, 고속)
    - `iloc`과 동일하지만, 역시 단일 값 전용으로 훨씬 빠름
    - 특징
      - ① 정수 인덱스 + 단일 셀 접근 전용
      - ② iloc보다 빠름
      - ③ 반복문 내 성능 최적화에 유리
    - 예시:
      ```python
      df.iat[1, 2]   # 1행 2열 위치의 단일 값
      ```

### 🔸 정렬, 필터링, 계산
| 기능         | 코드                                | 설명                 |
| ---------- | --------------------------------- | ------------------ |
| **조건 필터링** | `df[df["Score"] > 80]`            | Score가 80 이상인 행 선택 |
| **정렬**     | `df.sort_values(by="Age")`        | Age 기준 오름차순 정렬     |
| **평균 계산**  | `df["Score"].mean()`              | 특정 열의 평균           |
| **새 열 추가** | `df["Passed"] = df["Score"] > 80` | 논리 조건 기반 열 추가      |


### 🔸 자주 쓰이는 DataFrame 메서드
| 목적         | 메서드                             | 설명              |
| ---------- | ------------------------------- | --------------- |
| **데이터 확인** | `head()`, `tail()`              | 상·하위 n개 행 미리보기  |
| **요약/통계**  | `info()`, `describe()`          | 구조 및 통계 정보      |
| **선택/필터링** | `loc[]`, `iloc[]`, `query()`    | 행·열 조건 지정       |
| **정렬**     | `sort_values()`, `sort_index()` | 열값 또는 인덱스 기준 정렬 |
| **결측치 처리** | `dropna()`, `fillna()`          | 결측 데이터 제거/대체    |
| **집계/그룹화** | `groupby()`, `agg()`            | 그룹별 연산          |
| **파일 입출력** | `read_csv()`, `to_csv()`        | 파일로 저장·불러오기     |
| **타입 변환**  | `astype()`                      | 열 자료형 변경        |

### 🔸 Pandas + NumPy 연계
Pandas는 내부적으로 NumPy 배열을 기반으로 작동힘

- 따라서, 수치 계산 시 두 라이브러리를 함께 사용 가능
  ```python
  import numpy as np
  df["Normalized_Score"] = (df["Score"] - np.mean(df["Score"])) / np.std(df["Score"])
  ```

### 🔸 DataFrame 생성 방법 비교
| 입력 형식           | 코드 예시                            | 비고              |
| --------------- | -------------------------------- | --------------- |
| `dict`          | `pd.DataFrame({...})`            | 가장 흔한 방식        |
| `list[dict]`    | `[{"Name": "A"}, {"Name": "B"}]` | JSON 형식과 유사     |
| `list[list]`    | `[[A, B, C], [D, E, F]]`         | columns 지정 필수   |
| `numpy.ndarray` | `np.array([[1,2,3], [4,5,6]])`   | NumPy 기반 데이터 호환 |

- 예시:
  ```python
  # 1️⃣ List[Dict]
  df_1 = pd.DataFrame([
      {"Name": "Alice", "Age": 25, "Score": 85.5},
      {"Name": "Bob", "Age": 30, "Score": 90.3},
      {"Name": "Charlie", "Age": 35, "Score": 78.9}
  ])

  # 2️⃣ List[List]
  data = [
      ["Alice", 25, 85.5],
      ["Bob", 30, 90.3],
      ["Charlie", 35, 78.9]
  ]
  columns = ["Name", "Age", "Score"]
  df_2 = pd.DataFrame(data, columns=columns)

  # 3️⃣ NumPy ndarray
  import numpy as np
  nums = np.array([
      [25, 85.5],
      [30, 90.3],
      [35, 78.9]
  ])
  names = ["Alice", "Bob", "Charlie"]
  df_3 = pd.DataFrame(nums, columns=["Age", "Score"])
  df_3.insert(0, "Name", names)
  df_3["Age"] = df_3["Age"].astype("int64")
  ```


## 🔹 데이터 형태 변환 (Wide ↔ Long)
Pandas의 `pivot` 과 `melt` 는 데이터를 "넓게(Wide)" 혹은 "길게(Long)" 바꾸는 데 사용되는 두 가지 대표적인 형태 변환 함수

※ 데이터 분석과 시각화의 핵심은 "데이터 구조를 상황에 맞게 바꾸는 것" 이기 때문에 이 두 함수는 매우 자주 등장함

### 🔸 `pivot` : Long → Wide 변환
`pivot()`은 "길게 늘어진 데이터(Long-format)"를 가로로 펼쳐진 표 형태(Wide-format) 로 바꿈

-> 즉, 열(column) 으로 사용할 변수를 지정해
행·열의 조합으로 표를 재구성

- 기본 문법
  ```python
  DataFrame.pivot(index=None, columns=None, values=None)
  ```
  - 주요 파라미터:
    - `index` : 행으로 사용할 컬럼
    - `columns` : 열로 사용할 컬럼
    - `values` : 값으로 채울 컬럼

- 예시
  ```python
  import seaborn as sns
  import pandas as pd

  df = sns.load_dataset("tips")

  pivot_df = df.groupby(["sex", "day"], observed=False)["tip"].mean().reset_index()
  pivot_table = pivot_df.pivot(index="sex", columns="day", values="tip")

  # | sex    | Thur |  Fri |  Sat |  Sun |
  # | ------ | ---: | ---: | ---: | ---: |
  # | Female | 2.58 | 2.78 | 2.83 | 3.36 |
  # | Male   | 2.98 | 2.73 | 3.08 | 3.22 |
  ```
  - `pivot()`은 행(index), 열(columns), 값(values) 을 지정해야 함
  - 중복 조합이 존재하면 에러 발생 → 이때는 `pivot_table()` 사용
  - `pivot_table()`은 aggfunc로 집계 가능 (mean, sum, 등)

- 💡 참고: `pivot` vs `pivot_table`
  | 함수              | 중복 데이터 처리 | 주요 용도           |
  | --------------- | --------- | --------------- |
  | `pivot()`       | ❌ 중복 불가   | 단순 형태 변환        |
  | `pivot_table()` | ✅ 집계 가능   | 그룹별 평균, 합계 계산 등 |
  ```python
  pd.pivot_table(df, index="sex", columns="day", values="tip", aggfunc="mean")
  ```

### 🔸 `melt` : Wide → Long 변환
`melt()`는 `pivot()`의 반대

-> 즉, 여러 열에 흩어진 데이터를 세로로 녹여서(Long-format) 정리함

-> 쉽게 말하면 "엑셀의 여러 열을 하나로 합치는(flatten)" 기능

- 기본 문법
  ```python
  pd.melt(
      frame,
      id_vars=None,
      value_vars=None,
      var_name=None,
      value_name="value"
  )
  ```
  - 주요 파라미터:
    - `id_vars` : 녹이지 않고 그대로 유지할 컬럼
    - `value_vars` : 녹일 대상 컬럼 (리스트로 지정)
    - `var_name` : 녹인 후의 변수 이름
    - `value_name` : 녹인 후 값의 컬럼 이름

- 예시
  ```python
  melted = pd.melt(
      df,
      id_vars=["size"],                  # 유지할 컬럼
      value_vars=["total_bill", "tip"],  # 녹일 컬럼
      var_name="item",                   # 녹인 변수 이름
      value_name="amount"                # 녹인 값 이름
  )

  # | size | item       | amount |
  # | ---- | ---------- | -----: |
  # | 2    | total_bill |  16.99 |
  # | 3    | total_bill |  10.34 |
  # | …    | …          |      … |
  # | 3    | tip        |   5.92 |
  # | 2    | tip        |   2.00 |
  ```
  - `melt()`는 시각화나 groupby 전처리 전 필수 과정
  - Seaborn, Plotly 등은 대부분 Long-format 데이터를 요구함
    - ex. `sns.barplot(data=melted, x='size', y='amount', hue='item')`

### 🔸 `pivot` vs `melt` 비교
| 비교 항목    | `pivot()`                    | `melt()`                                          |
| -------- | ---------------------------- | ------------------------------------------------- |
| 변환 방향    | Long → Wide                  | Wide → Long                                       |
| 결과 형태    | 표 형식 (가로로 펼침)                | 세로로 늘어진 데이터                                       |
| 사용 목적    | 요약 결과를 보기 좋게 정리              | 시각화, 분석 전 데이터 정리                                  |
| 유지 컬럼    | `index`                      | `id_vars`                                         |
| 펼칠/녹일 컬럼 | `columns`                    | `value_vars`                                      |
| 주요 파라미터  | `index`, `columns`, `values` | `id_vars`, `value_vars`, `var_name`, `value_name` |
| 중복 허용    | ❌ (→ pivot_table)            | ✅ 가능                                              |
| 반대 관계    | ↔                            | ↔                                                 |


