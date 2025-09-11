## Q1. TypeError: greet() got multiple values for argument 'age' 발생 이유?

```python
def greet(name, age, greeting='hello'):
    print(f'안녕하세요, {name}님! {age}살이시군요.{greetomg}')
greet(name='Dave', age=35)  # 정상작동
greet(name='Dave', 'hello', age=35) # 에러발생
# 위치 인자를 순서대로 지정하고, 키워드 인자를 그 위치 인자 뒤에 둠으로써 규칙은 지킴
# Dave -> name에, 35 -> age, hello -> greeting에 할당될 것처럼 보인다.
# 그러나 TypeError: greet() got multiple values for argument 'age'발생
# age에 여러 개의 값이 할당 되었다!
# 기본값을 가진 greeting의 값은 제일 뒤로 밀림
# 즉, Dave->name, age='hello', age=35->greeting에 넣으려고 시도된 것
# 그럼 왜 TypeError?
# age는 한 개의 인자를 받는 매개변수인데, 'hello'는 음??
# greeting조차 키워드 인자로 넣어야 함
greet('Dave', greeting='hello', age=35)
# 그럼 키워드 인자 형식으로 넘겨야 하는데 너무 복잡하고 많아짐
# 함수 설계가 잘못되었다
# 사용자가 greeting 매개변수에 값을 전달하지 않은 경우가 많다고 판정해 함수를 설계한 것임
# 평범한 위치 인자로 함수 만들어보자
def greet(name, age, greeting):
    print(f'안녕하세요, {name}님! {age}살이시군요.{greetomg}')
greet(name='Dave', 'hello', age=35) # 순서 안맞아서 안됨?
greet(name='Dave', age=35, 'hello') # 정상작동

# 키워드 인자는 언제 사용하는가? -> 매개변수가 여러개 있을 때 사용?
# 순서가 상관 없을 떄..
def greet(name, greeting, age, some):
    print(f'안녕하세요, {name}님! {age}살이시군요.{greetomg}')
greet('Dave', 'hello', some=11, age=35)
```


## Q2. map object
- map() 
    - **첫번째 인자: 함수**
    - 두번째 인자: 순회 가능한 문자열
    ```python
    obj = map(int, '123')
    print(obj)
    print(type(obj))    # <class 'map'> -> map객체다
    print(type('123'))  # <class 'str'> -> str 객체다
    # map object도 순회 가능한 객체이기 때문에 반복 가능
    for item in obj:
        print(type(item))   # <class 'int'>
        print(item) # 1 2 3
    # 이렇게 하면 출력 시 안예쁘게 출력됨

    # 이러한 경우 보통 list로 형 변환 후 사용 -> 명시적 형변환
    my_list = list(obj)
    print(my_list)  # [1, 2, 3]

    def func(num):
        return num**2
    obj2 = list(map(func, [1, 2, 3]))
    print(obj2) # [1, 4, 9]

    # 함수를 재사용할 일이 없다면 lambda 사용해서 익명 함수로 만들 수도 있다
    obj3 = list(map(lambda x: x**2, [1, 2, 3]))
    print(obj3)
    ```
    
- map 함수로 낸 결과는 하나의 '값' 이므로 변수에 할당 가능함

- 보통 사용자에게 받은 입력값(문자열)을 숫자로 뽑고 싶을 때
    ```python
    user = '1 2 3 4 5'
    arr = list(map(int, uset.split(' ')))
    for item in user:
        print(item ** 2)
    ```
    - .split(' '): 공백 기준으로 쪼개서 리스트로 만듬
    - map: 리스트로 만든 요소들을 int로 형변환


## Q3. global 키워드는 무엇을 위한 것이며 어떻게 사용하는가
- LEGB rule
    - Local: 함수 내뷰
    - En-Closed: 내부함수 기준으로 본인이 속해있는 상단 위치
    - Global: 파이썬 파일
    - Built-in: 

```python
                            # 글로벌
def outer():            # en closed
    x = 0                   
    def inner():    # 로컬
        x = 10      # 로컬
    inner()                 
                        # en closed
x = 10
                            # 글로벌
```

- 로컬에 출력하려는 변수가 없다면?
    - en closed에서 변수 찾아봄
    - en closed에도 없다면 global에서 변수 찾아봄
    ```python
    def outer():
        # 탐색 순서에 따라서, outer에 x가 없어서
        # global에 있는 x=100을 참조해서 100을 출력함
        # 그럼, 내가 x에 0을 할당했을 땐, 왜 global에는 영향을 안미치는가?
        # 나의 local 영역에 x라는 새로운 변수를 만든 것
            # 함부로, 내 상위의 변수를 바꿀 수 없다
            # LEGB 중 G와 B를 생각해보면
            # global과 built-in에서 이미 정의된 어떤 값들이, 다른곳에서 이미 사용되고 있을 수 있다.
            # 그런데, local 영역에서 그렇게 함부로 값을 바꿔서는 안되겠다
        # 그럼에도 불구하고, 내가 직접 global 영역에 있는 값에 영향을 끼치고 싶다면
        global x
        x = '안녕하세요'
        def inner():
            x = 10
            print(x)

        inner()
        print(x)

    x = 100
    outer()
    print(x)
    ``` 

- 권장하는 방법
    - global에 정의된 값을 사용하고 싶고, 그 값을 내가 바꾸거나 조작하고자 한다면
    - 매개변수로 만들어서, 인자로 전달하는 방식 사용
        ```python
        def some(y):
            y = '안녕하세요'
            return y
        y = 100
        # y = some(y) -> sume함수의 실행 결과를 y에 다시 할당하거나, 혹은 다른 변수에 할당해서 사용 가능
        z = some(y)
        print(y, z)
        ```
