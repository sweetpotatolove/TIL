# Classes
## 객체

### 클래스(class)
파이썬에서 타입을 표현하는 방법
- 객체 생성을 위한 설계도
- 데이터와 기능을 함께 묶는 방법 제공
```python
print(type('123')) # <class 'str'>
# 문자열 등 클래스에 속해있는 타입이라 생각할 수 있음
```

### 객체(Object)
클래스에 정의한 것을 토대로 메모리에 할당된 것
- **속성**과 **행동**으로 구성된 모든 것
    - ex. {직업, 생년월일, 국적} == 변수 -> 속성을 가진 class가 있고, 이 클래스에 여러 객체 존재 가능
    - ex. {랩(), 댄스()} == 메서드 -> class에 속한 동일한 행동을 하더라도 output은 달라질 수 있음


### 클래스와 객체
클래스로 만든 객체를 '인스턴스'라고 부름

ex. 가수 = class
1. 아이유는 객체다 (O)
2. 아이유는 인스턴스다 (?)
3. 아이유는 가수의 인스턴스다 (O)

    ※ 어떠한 클래스의 인스턴스임을 명시해야 함(타입 정보 중요 ex. 리스트 클래스, 문자열 클래스 ...)

- 클래스를 만든다 == 타입을 만든다
    - 조건문에 type에 따라 다르게 동작하게 코드 흐름 제어 가능
    - 조건문 없이 반복문 사용해서 코드 실행시키려고 하면
    - 순회 불가능한 타입은 에러 발생
    - 때문에 조건문에서 타입을 통해 에러 방지 하자

```python
name = 'Alice'
print(type(name))   # <class 'str`>
                    # 변수 name은 str 클래스의 인스턴스이다
                    # 문자열 타입(클래스)의 객체(인스턴스)
```

- 객체.행동() == 인스턴스.메서드()
    - 각 객체 타입이 가진 메서드 사용 가능
    - 리스트 타입의 메서드 sort -> [1,2,3].sort()
    - 문자열 타입의 메서드 upper -> "hello".upper()

- 객체 == 특정 타입의 인스턴스
    - 123, 900은 모두 int의 인스턴스
    - 'hello', 'bye'는 모두 string의 인스턴스
    - [2, 1], []은 모두 list의 인스턴스


### 객체 정리
- 타입(type)
    - 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute)
    - 어떤 상태(데이터)를 가지는가?
- 조작법(method)
    - 어떤 행위(함수)를 할 수 있는가?
- 즉, 객체들은 모두 어떠한 타입을 가지며, 타입이 가진 속성과 조작법을 함께 가지고 있다
- Object = Attribute + Method


## 클래스
- class 키워드
- 클래스 이름은 파스칼 케이스(Pascal Case) 방식으로 작성
```python
# Pascal Case: 공백을 기준으로 시작하는 첫 단어를 대문자로 적는 것
class MyClass: 
    pass
```


### 클래스 정의
- 속성 정의: 변수에 값 할당하는 것과 동일
- 조작법 정의: 함수 정의하는 것과 동일
```python
# 클래스 정의
class Person:
    blood_color = 'red'
    def __init__(self, name):
        self.name = name
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')  
# Person 타입의 인스턴스인 singer1 생성하여 인자를 넣어 함수 호출하듯 사용

# 메서드 호출
print(singer1.singing())  
# 속성(변수) 접근
print(singer1.blood_color)
```


### 클래스 구성 요소
- 생성자 함수
    ```python
    def __init__(self, name):
        self.name = name
    ```
    - **객체 생성 시 자동 호출**하는 특별한 메서드
    - `__init__` 메서드로 정의
    - 객체 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정함
    - 왜 필요한가? 클래스로 이루어진 각 객체들은 이름은 같지만 서로 다른 속성(안에 든 값이 달라야 함)을 가져야 하므로, 인스턴스 생성 시 해당 인스턴스만이 가져야 할 값이 있다면 그 값의 정보를 올바르게 초기화 시키기 위함
    - self == 생성하려는 인스턴스 자체

- 인스턴스 변수
    ```python
        self.name = name
    ```
    - self가 가지는 변수
    - 인스턴스마다 별도로 유지되는 변수
    - 인스턴스마다 독립적인 값 가지며, 인스턴스 생성될 때마다 초기화됨

- 클래스 변수
    ```python
    blood_color = 'red'
    ```
    - 클래스 내부에 선언된 변수(클래스에 직접 정의)
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수

- 인스턴스 메서드
    ```python
    def singing(self):
        return f'{self.name}가 노래합니다.'
    ```
    - 각 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행


### 인스턴스 변수와 클래스 변수
```python
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1

person1 = Person('iu')
person2 = Person('BTS')
print(Person.count) # 2
```
- Person 클래스의 객체를 통해 만든 인스턴스가 있고, 몇 개의 객체들이 만들어졌는지 관리할 필요가 있을 때 '클래스 변수' 사용
    - 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 설정할 수 있음
- 서로 다른 값을 필요로 하는 속성은 인스턴스 변수에
- 동일하게 사용하는 속성은 클래스 변수에 넣자

※ 클래스 변수에 본인만의 독특한 값을 할당하고 싶다면?
```python
Class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r
c1 = Circle(5)
c1.pi = 1.14 # 인스턴스로 클래스 변수를 바꾸려고 했지만
             # 클래스 변수가 바뀌는 것이 아니라
             # c1 객체만의 새로운 인스턴스 변수 pi가 생김(본인 만의 값)
Circle.pi = 5   # 클래스 직접 써서 할당하면 클래스 변수 바꾸기 가능
```


## 메서드
1. 인스턴스 메서드
2. 클래스 메서드
3. 정적 메서드


### 인스턴스 메서드
클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
```python
class MyClass:
    def instance_method(self, arg1, ...):
        pass
```
- 인스턴스 상태 조작, 동작 수행
- **반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음**(호출 시 self은 생략 가능)
- self 동작 원리
    - `'hello'.upper()` -> upper 메서드로 대문자 변경하기
    - `str.upper('hello')` -> 실제 파이썬 내부 동작은 이렇게 진행됨
    - str 클래스가 upper 메서드 호출, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
    - 인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유
    - 'hello'라는 문자열 객체가 단순한 함수 인자가 아닌, 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것


#### 생성자 메서드
인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
```python
class Person:
    def __init__(self, name):
        self.name = name
        print('인스턴스가 생성되었습니다.')
    def greeting(self):    # 생성자 메서드
        print(f'안녕하세요. {self.name}입니다.')
person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
```
- 인스턴스 변수들의 초기값을 설정


### 클래스 메서드
클래스가 호출하는 메서드
```python
class MyClass:
    
    @ classmethod
    def class_method(cls, arg1, ...):
        pass
```
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- @classmethod 데코레이터를 사용하여 정의(나머지는 인스턴스 메서드 만드는 것과 동일)
- 호출 시, **첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달**됨

```python
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('iu')
person2 = Person('BTS')
Person.number_of_population() # 인구수는 2입니다.
```
- 이전에 클래스 변수를 직접 바꿨던 방법 보다는 '클래스 메서드'를 정의해서 이를 호출하여 값을 바꿔주는게 더 명시적임
    - 클래스 변수가 변하면 해당 클래스에 속한 객체가 무수히 많을 수 있으므로 클래스 변수를 참조하는 모든 객체들에게 영향이 감(뭐때매 값이 바꼈는지 추척 힘듦)
    - 클래스 변수를 바꿀 수 있는 클래스 메서드가 정의되어 있다면 '클래스 메소드의 이름'을 찾아봄으로써 코드의 어디에서 변수의 값이 바뀌었는지 추적 가능
    - 즉, 내가 참조하는 데이터가 어떻게 어디서 변경되었는지 추적 가능하다

※ 파이썬은 제약사항이 따로 존재하지 않기 때문에 클래스가 호출하지 않고 인스턴스가 호출할 수는 있음

-> 인스턴스는 '해당 클래스의 인스턴스'이므로 본인이 속한 클래스 정보가 존재하여 어떤 클래스인지 정보 전달 가능(그치만 안쓸거얌)


### 정적 메서드
클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
```python
class MyClass:

    @staticmethod
    def static_method(arg1, ...):
        pass
```
- 주로 클래스와 관련 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
- 즉, 클래스가 가진 속성&메서드, 인스턴스가 가진 변수&메서드에 접근할 필요는 없지만 (특정 객체만의 속성에 접근할 필요는 없지만) 클래스 자체의 전체 모둠들이 공통적으로 동작할 때 필요한 것을 만들 때 '정적 메서드' 사용
- @staticmethod 데코레이터 사용하여 정의
- 호출 시 필수적으로 작성해야 할 매개변수가 없음

- 예시
    ```python
    class StringUtils:
        @staticmethod
        def reverse_string(string):
            return string[::-1]
        @staticmethod
        def capitalize_string(string):
            return string.capitalize()

    text = 'hello, world'
    reversed_text = StringUtils.reverse_string(text)
    print(reversed_text)  # dlrow ,olleh
    capitalized_text = StringUtils.capitalize_string(text)
    print(capitalized_text)  # Hello, world
    ```
    - 문자열 data type은 이미 존재
    - 문자열 데이터 타입을 잘 조작하기 위한 클래스 생성
    - 오로지 문자열을 복잡한 로직으로 조작하기 위해 만든 유틸성 클래스라면 인스턴스에 직접적으로 접근할 인스턴스 메서드 필요 없음
    - 이미 인스턴스 접근 방법은 문자열 클래스에 정의되어 있음(속성도 문자열 클래스에 있을 것임)
    - 문자열들을 가지고 어떤 로직을 진행할 때 로직을 여러번 사용해야 하는 유틸성으로서 만들 때에는 정적 메소드를 사용할 수 있다~


### 인스턴스와 클래스 간의 이름 공간
1. 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
2. 인스턴스를 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성
3. 인스턴스에서 특성 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색하게 됨
    - LEGB랑 다른거임!!
    - 메서드 내부에서는 LEGB 룰을 따라가겠지만 그것과는 별개

    ![이름 공간](이름공간.png)
    - 클래스 변수의 속성에 접근하는 상황
    - 각각의 인스턴스 공간에 각각의 이름 속성에 값을 넣었을 때
    - `Person('iu').blood_color` 라고 하면 인스턴스 공간 내부에서 blood_color를 먼저 찾아봄
    - 찾아보고 없으면 자기가 속해있는 class로 가서 찾아보고 가져옴
    - `Person('iu').blood_color = blue` 라고 작성하면 클래스의 blood_color='red'에 영향을 미치는 것이 아닌, 내 공간(iu 인스턴스 공간)에 변수 만들어져서 blue가 들어감


## 상속
※ 클래스 이름을 정의하는 이유: 동일한 속성, 메서드를 가진 객체끼리 묶어주기 위해 클래스 정의함

-> Person이라는 클래스 만들었을 때, 인간을 person 클래스에 다 넣기엔 '직업'이 다르면 행동이 다를 수 있음

- 상속 없이 구현하는 경우
    - ex. 학생/교수 정보를 별도로 표현하기 어려움
    - ex. 학생/교수 클래스로 분리했지만 메서드가 중복으로 정의될 수 있음

- 상속 받으면 동일한 메서드를 한번만 구현해도 됨
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def talk(self):  # 메서드 재사용 -> 자식 클래스(Professor, Student 클래스에 상속됨)
            print(f'반갑습니다. {self.name}입니다.')
    class Professor(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

    p1 = Professor('박교수', 49, '컴퓨터공학과')
    s1 = Student('김학생', 20, 3.5)
    # 부모 Person 클래스의 talk 메서드를 상속 받았으므로 호출 가능
    p1.talk()  # 반갑습니다. 박교수입니다.
    s1.talk()  # 반갑습니다. 김학생입니다.
    ```
    
    ![상속 구조](상속구조.png)

- 만약 부모-자식간 동일한 메서드가 존재한다면?
    ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    class Professor(Person):
        def __init__(self, name, age, department):
            self.name = name
            self.age = age
            self.department = department
        def talk(self):  # 메서드 재사용
            print(f'반갑습니다. {self.name}교수 입니다.')
    class Student(Person):
        def __init__(self, name, age, gpa):
            self.name = name
            self.age = age
            self.gpa = gpa

    p1 = Professor('박교수', 49, '컴퓨터공학과')
    s1 = Student('김학생', 20, 3.5)
    ```
    - p1이 호출되면 본인 클래스(Professor)의 talk 메서드가 호출됨
    - 즉, 본인이 원하는대로 커스텀 가능
    - s1이 호출되면 본인의 talk 클래스가 없으므로 상속받은 Person클래스의 talk가 호출됨


### 다중 상속
둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
- 상속받은 모든 클래스의 요소를 활용할 수 있음
- **상위 클래스끼리 중복 속성이나 메서드가 있는 경우 '상속 순서에 의해 결정'됨**


- 다중 상속은 덮어쓰기 방식XX
    ```python
    a = 10
    a = 20
    print(a)    #20
    ```
    - 이런 방식이 아니다

- 다이아몬드 문제(상속 순서에 관한 문제)

    ![다이아몬드 문제](다이아몬드문제.png)

    - D의 입장에서 어떤 부모의 메서드를 가져올지에 대한 모호함 발생
    - 파이썬에서의 해결책
        - MRO(Method Resolution Order) 알고리즘을 사용하여 클래스 목록 생성
        - 부모 클래스로부터 상속된 속성들의 검색을 C3 선형화 규칙에 맞춰 진행
        - 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지XX
        - 속성이 D에서 발견되지 않으면 B에서 찾고, 거기도 없으면 C에서 찾는 순으로 진행됨
            ```python
            class D(B, C):
                pass
            ```

- 상속 예시

    ![상속예시](상속예시.jpg)
    - O, D, E, F, B, C에 모두 동일한 속성이 존재한다면, A는 어떤 부모의 속성을 물려받을까?
        ```python
        O = object
        class D(O): pass
        class E(O): pass
        class F(O): pass
        class B(D, E): pass
        class C(F, D): pass
        class A(B, C): pass

        # A클래스의 상속 탐색 순서 출력
        print(A.__mro__)

        # <class '__main__.A'>
        # <class '__main__.B'>
        # <class '__main__.C'>
        # <class '__main__.F'>
        # <class '__main__.D'>
        # <class '__main__.E'>
        # <class 'object'>
        ```

    - C3 선형화 규칙
        - 각각의 클래스 순서를 적어보자
        - O는 O
        - D는 D O (자기 자신 -> 부모 순서)
        - E는 E O
        - F는 F O
        - B는 B D E O (D,E 중 먼저 상속받는 D를 우선적으로 찾아가고, 그 다음 D의 부모 O가 아닌!! D와 같이 상속 받고있는 E를 찾아감)
        - C는 C F D O
        - A는 A B C F D E O
            ```markdown
            1. B와 C 중에서 먼저 상속 받는 B를 찾아간다
            (머리)
            ↓
            B D E O  
            C F D O
            -> B는 B D E O 중 가장 앞(머리)에 위치함
            -> 또, B는 다른 상속 대상(C F D O)에 포함되어 있지XX
            -> 그럼 A 다음 상속 받는건 B 확정!

            2. 상속받은 B를 지우면 그 다음 탐색 대상은 D
              ↓
              D E O
            C F D O
            -> D가 현재 탐색 대상의 머리에 위치함
            -> 다른 탐색 대상(C F D O)의 MRO 순으로 보면 D가 '머리가 아닌' 위치에 있음
            -> 때문에 D가 무시됨
            -> D를 무시하고 E를 탐색하려니까 E는 머리가 아님! 즉, E 탐색 불가
            -> 다음 머리인 C를 탐색하자

            3. 다음 탐색 대상 C 확인
            ↓    
              D E O
            C F D O
            -> C는 어떠한 MRO(C F D O)의 머리에 위치하고 있으면서, 다른 탐색 대상(D E O)에 포함되지XX
            -> 그럼 B 다음 상속 받는건 C 확정!

            4. 상속받은 C를 지우고 머리부분 확인
              ↓
              D E O
              F D O    
            -> D는 다른 탐색 대상(F D O)의 머리가 아닌 위치에 존재하므로 무시
            -> E는 머리가 아니므로 다른 머리인 F를 탐색
            -> F는 다른 탐색 대상(D E O)에 포함되지XX
            -> 그럼 C 다음 상속 받는건 F 확정!

            5. 상속받은 F 지우고 머리부분 확인
              ↓
              D E O
                D O
            -> D가 머리에 위치함. 다른 탐색 대상의 머리도 D
            -> 따라서 F 다음 상속 받는건 D 확정!

            6. 상속받은 D 지우고 머리 확인
                ↓
                E O
                  O
            -> D 다음 E 확정, E 다음 O 확정!
            ```
    - `print(A.__mro__)`로 확인 가능
    - 그치만 처음 계산할 때 C3 선형화 규칙 생각해서 MRO 잘 계산하고 코드 작성하는게 좋다
    - 나중에 바꾸려고 하면 큰일쓰

- `super()`
    - 부모 클래스(상위 클래스)의 메서드 호출을 위해 사용하는 내장 함수
    - 다중 상속 시 MRO(메서드 결정 순서)를 기반으로 현재 클래스가 상속하는 모든 부모 클래스 중 다음에 호출될 메서드를 결정하여 자동으로 호출
    - 주로 생성자 메서드에서 사용
    ```python
    # super 사용 전
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email

    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            self.name = name        # 중
            self.age = age          # 복
            self.number = number    # 중
            self.email = email      # 복
            self.student_id = student_id    

    # super 사용 후
    class Person:
        def __init__(self, name, age, number, email):
            self.name = name
            self.age = age
            self.number = number
            self.email = email

    class Student(Person):
        def __init__(self, name, age, number, email, student_id):
            # Person의 init 메서드 호출
            super().__init__(name, age, number, email)
            self.student_id = student_id # Student만의 속성 추가로 정의
    ```

#### MRO가 필요한 이유
- 부모 클래스들이 여러번 액세스 되지 않도록 각 클레스에서 지정된 '왼쪽->오른쪽'으로 가는 순서를 보존함
- 각 부모를 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적인 구조 형성함
- 위 예시와 같이 super()로 부모 클래스 호출할 때 누가 호출되는지 알아야 함
- 즉, 클래스 간 메서드 호출 순서가 예측 가능하게 유지되며, 코드의 재사용성&유지보수성이 향상됨

#### super의 사용 사례 2가지
1. 단일 상속 구조
    - 명시적으로 이름 지정하지 않고 부모 클래스 참조 가능 -> 코드 유지 관리 쉬움
    - 클래스 이름 변경되거나 부모 클래스가 교체되어도 super() 사용하면 코드 수정이 더 적게 필요
2. 다중 상속 구조
    - MRO에 따른 메서드 호출
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제 방지


## 클래스 참고
### 메서드 주의사항
- 클래스가 사용해야 할 것: 클래스 메서드, static 메서드
    - 클래스는 모든 메서드 호출 가능하지만, 위 2개만 사용하기로 약속☆
    - 할수 있다 != 써도 된다
- 인스턴스가 사용해야 할 것: 인스턴스 메서드


### 매직 메서드
특정 상황에 자동으로 호출되는 메서드

※ 매직 메서드는 인스턴스 메서드! 단, 직접 정의하지 않고 제공받는 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 또는 매직 메서드로 부름
- 예시
    - `__str__(self)`, `__len__(self)`, `__lt__(self, other)`, `__eq__(self, other)` 등등
    - `__str__(self)` : 내장함수 print에 의해 호출되어 객체 출력을 문자열 표현으로 변경
        ```python
        class Circle:
            def __init__(self, r):
                self.r = r
            def __str__(self):
                return f'원 반지름: {self.r}'
        
        c1 = Circle(10)
        print(c1)   # 원 반지름: 10
        ```


### 데코레이터(Decorator)
다른 함수의 코드를 유지한 채로 수정되거나 확장하기 위해 사용되는 함수

- 데코레이터 정의
    ```python
    def my_decorator(func):
        def wrapper():
            # 함수 실행 전에 수행할 작업
            print('함수 실행 전')
            # 원본 함수 호출
            result = func()
            # 함수 실행 후에 수행할 작업
            print('함수 실행 후')
            return result
        return wrapper
    ```
    - 함수 내에 함수 정의
    - 즉, 함수를 인자로 받는 함수 정의
    - 내부에 실제로 동작하고자 하는 함수를 정의하고, 넘겨받은 함수를 내부에서 호출하여 어떤 동작을 시킬 것임

- 데코레이터 사용
    ```python
    @my_decorator
    def my_function():
        print('원본 함수 실행')
    my_function()
    """
    함수 실행 전
    원본 함수 실행
    함수 실행 후
    """
    ```
    - my_function() == **my_function = my_decorator(my_function)**
    - 즉, my_funcion()을 호출하면 my_decorator가 리턴한 wrapper() 함수가 실행됨
    - 그럼 my_function = wrapper
    - wrapper() 내부에서 print("함수 실행 전") 실행
    - func() -> 원래의 my_function() 실행
    - 이후 print("함수 실행 후") 실행

- 추가 설명(클래스 메서드의 첫번째 인자가 self가 아닌, cls인 이유)
    1. 인스턴스 메서드
        ```python
        class MyClass:
            def hello(self):
                ...
        ```
        - 인스턴스를 통해 호출되므로 첫 번째 인자는 self
    2. 클래스 메서드
        ```python
        class MyClass:
            @classmethod
            def hello(cls):
                ...
        ```
        - 클래스를 통해 호출되므로 첫 번째 인자는 cls
        - 왜 cls가 들어오는가? -> @classmethod는 내부적으로 classmethod라는 클래스를 사용하여 함수를 감싼다
        - 데코레이터 사용 안하고 수동으로 처리하면 아래와 같음
        ```python
        class MyClass:
            def hello(cls):
                ...
            hello = classmethod(hello) # hello 메서드를 클래스 메서드로 변환
        ```
        - classmethod()는 파이썬 내부에서 클래스가 자동으로 첫 번째 인자로 전달되도록 처리된 함수 객체를 만들어줌
        - 클래스 메서드 내부에 머 이런저런 이유로 첫 번째 인자가 class가 되는데
        - 어려우니까 classmethod(hello)를 사용하면 hello함수가 클래스 메서드로 변환되고, 클래스 메서드는 첫 인자로 cls를 자동으로 받는 특징이 있어서 hello함수도 클래스를 인자로 받게 된다고 이해하자
        - classmethod()로 감싸는걸 @classmethod로 간단하게 쓰는게 데코레이터


## 참고
### 제너레이터
- Iterator(이터레이터)
    - 반복 가능한 객체의 요소를 하나씩 반환하는 객체

- python 내부적으로 반복이 동작하는 원리
    1. for문 동작 시 내부적으로 반복 가능한 객체에 대해 iter() 호출
    2. iter() 함수는 메서드 __next()를 정의하는 이터레이터 객체를 돌려줌
    3. __next() 메서드는 반복 가능한 객체들의 요소를 한 번에 하나씩 접근
    4. 남은 요소가 없으면 StopIteration 예외를 일으켜서 for 반복 종료
    ```python
    my_str = 'abc'
    my_iter = iter(my_str)
    print(next(my_iter)) # a
    print(next(my_iter)) # b
    print(next(my_iter)) # c
    print(next(my_iter)) # StopIteration

#### Generator(제너레이터)
이터레이터를 간단하게 만드는 함수

- 제너레이터 사용 이유
    1. 메모리 효율성
        - 한번에 한 개의 값만 생성하여 반환하므로, 전체 시퀀스를 한 번에 메모리에 로드하지 않아도 됨
        - 대용량 데이터셋을 처리할 때 메모리 사용 최소화 가능
            - ex. 파일의 각 줄을 한 번에 하나씩 읽어 처리 가능

    2. 무한 시퀀스 처리
        - 무한 루프를 통해 무한 시퀀스 생성 가능(종료 지점을 만들지X)
        - 끝이 없는 데이터 스트림 처리할 때 유용함

- 제너레이터 구조
    - 일반 함수처럼 작성
    - yield문을 사용하여 값 반환
        ```python
        def generate_numbers():
            for i in range(3):
                yield i

        for number in generate_numbers():
            print(number)  # 0 1 2
        ```
        - 함수는 return문을 작성함으로써 함수의 역할이 끝남을 알림
        - 제너레이터는 yield문 사용해서 값을 하나 불러오고, 끝난게 아니라 순회해야 할 다음 요소가 더 있다면 한번 더 불러와서 다음 요소를 불러옴

- `return`과 `yield`의 차이
    - return
        - 값을 반환하고 함수 실행 종료
        - 함수 호출 시마다 전체 함수 실행
        - 함수 상태는 호출 후 유지되지 않음
        ```python
        def return_ex():
            return 'a'
            return 'b'
        print(return_ex())  # a
    
    - yield
        - 값을 반환하지만 함수 실행을 종료하지 않음
        - 함수의 현재 상태를 유지하여, 이후 호출 시 중단된 시점부터 실행됨
        - 제너레이터 객체를 반환하며, 반복문을 통해 순차적으로 값 반환 가능
        ```python
        def yield_ex():
            yield 'a'
            yield 'b'
        gen = yield_ex()
        print(next(gen))    # a
        print(next(gen))    # b
        ```

- 제너레이터 활용
    1. 무한 시퀀스 생성
        - 필요할 때마다 값을 생성하여 무한 반복 가능
        - 05-generator.py 참고    
    2. 대용량 데이터 처리
        - 파일에서 한 줄씩 읽어와 처리
        - 메모리에 전체 파일 로드하지 않고, 한 줄씩 처리하여 메모리 사용 절약
        - 제너레이터 사용하지 않으면 메모리에 전체 파일 내용을 저장하므로, 대용량 파일의 경우 메모리 과부화 발생

### 에러와 예외
1. 문법 에러(Syntax Error): 프로그램 구문이 올바르지 않은 경우 발생(문법 오류)
2. 예외(Exception): 프로그램 실행 중 감지되는 에러

- 에러는 공식 문서를 확인할 것! (최신버전 반영된거~)


### 예외처리
예외가 발생했을 때 프로그램이 비정상적으로 종료되지 않고, 적절하게 처리할 수 있도록 하는 방법

- try-except 구조
    ```python
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
        result = 100 / num
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except ValueError:
        print('유효한 숫자가 아닙니다.')
    except: # ValueError, ZeroDivisionError 둘 다 아닌데 에러 발생하면 실행
        print('에러가 발생하였습니다.')
    else:
        print(f'결과: {result}')
    finally:
        print('프로그램이 종료되었습니다.')
    ```
    - `try` : 예외가 발생할 수 있는 코드 작성
    - `except` : 예외가 발생했을 때 실행할 코드 작성
    - `else` : 예외가 발생하지 않았을 때 실행할 코드 작성
    - `finally` : 예외 발생 여부와 상관없이 항상 실행할 코드 작성

**※ `raise` : 예외 상황을 발생시킴**

-> ex. 조건문을 만족하면 예외 상황(ValueError 등)을 발생시킨다

- 예외처리 시 주의사항
    - 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except절로 나눌 시 **반드시 하위 클래스를 먼저 확인할 수 있도록 작성**

    ![예외처리 주의사항](예외처리_주의사항.jpg)
    - 만약 상위 클래스를 먼저 확인하면 하위 클래스 except절에 도달하지 못함


### 모듈(Module)
한 파일로 묶인 변수와 함수의 모음
- 특정 기능을 하는 코드가 작성된 파이썬 파일(.py)
- 모듈 가져오는 방법
    - import 문 사용
        ```python
        import math
        print(math.sqrt(4))
        ```

    - from절 사용
        ```python
        from math import sqrt
        print(sqrt(4))
        ```

- 모듈 사용하기
    - `. (dot)` 연산자
    - 점의 왼쪽 객체에서 점의 오른족 이름을 찾으라는 의미
        ```python
        # 모듈명.변수명
        print(math.pi)

        # 모듈명.함수명
        print(math.sqrt(4))
        ```

- 모듈 주의사항
    - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
    - 마지막에 import된 이름으로 대체됨
        ```python
        from math import pi, sqrt
        from my_math import sqrt
        # 그래서 모듈 내 모든 요소를 한번에 import하는 * 표기는 권장XX
        from math import *
        ```
    - as 키워드로 별칭(alias) 부여하여 이름 충돌을 해결하자
        ```python
        from math import sqrt
        from my_math import sqrt as my_sqrt
        ```

※ 사용자 정의 모듈: 내가 모듈 직접 정의 가능(당연함)

※ 파이썬 표준 라이브러리: 파이썬에서 제공하는 다양한 모듈과 패키지 모음

### 패키지(Package)
연관된 모듈들을 하나의 디렉토리에 모아놓은 것

1. PSL 내부 패키지
    - 설치 없이 import

        ![패키지 예시](패키지예제.jpg)
        - 패키지 3개: my_package, math, statistics
        - 모듈 2개: my_math, tools
        ```python
        from my_package.math import my_math
        from my_package.statistics import tools
        print(my_math.add(1, 2)) # 3
        print(tools.mod(1, 2)) # 1
        ```

2. 외부 패키지
    - pip를 사용하여 설치 후 import
    - `pip` : 외부 패키지들을 설치하도록 도와주는 파이썬 패키지 관리 시스템

- 패키지 사용 목적
    - 모듈의 이름 공간을 구분하여 충돌 방지
    - 모듈을 효율적으로 관리, 재사용할 수 있도록 돕는 역할
    

### 정규 표현식(★★★)
문자열에서 특정 패턴을 찾기 위해 사용되는 기법

- 복잡한 문자열 속 특정한 규칙으로 된 문자열을 검색, 치환, 추출 등을 간결하게 수행할 수 있음
- 절대 외우지 말고, 표 보고 작성하거나 생성형 AI로 작성 후 디버깅 하면서 표로 공부하세용

- 예시
    ```python
    import re
    pattern = r'\d+' # 숫자가 하나 이상인 패턴
    text = 'There are 24 apples and 42 oranges.'
    matches = re.findall(pattern, text)
    print(matches) # ['24', '42']
    ```
    - re 모듈: 정규식 일치 연산을 제공하는 파이썬 내장 모듈

- 정규 표현식 문자열 앞에 'r'을 붙여야 함
    - 문자열을 "raw string"으로 취급하여 역슬래시(`\`)를 이스케이프 문자로 처리하지 않도록 하기 위함

- 특수 문자

    ![정규표현식 특수문자](정규표현식_특수문자.jpg)

- 특수 시퀀스

    ![정규표현식 특수시퀀스](정규표현식_특수시퀀스.jpg)

- 메서드

    ![정규표현식 메서드](정규표현식_메서드.jpg)
