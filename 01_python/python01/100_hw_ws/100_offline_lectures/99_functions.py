# Keyword Arguments
def greet(name, greeting, age, some):
    print(f'안녕하세요, {name}님! {age}살이시군요.{greeting}')
# greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
# 위치 인자를 순서대로 지정하고, 키워드 인자를 그 위치 인자 뒤에 둠으로써 규칙은 지켰다.
# Dave -> Name에, 35 -> Age, hello -> greeting에 할당 될 것 처럼 보인다.
# greet('Dave','hello',age=35) # TypeError: greet() got multiple values for argument 'age'
# greeting 조차 키워드 인자로 넣어야 한다.
# 그럼, 키워드 인자 형식으로 넘겨야 하는게 너무 복잡하고 많아진다... 
    # 함수 설계가 잘못됐다.
    # 사용자가 greeting 매개변수에 값을 전달하지 않을 경우가 많다고 판정
greet('Dave', 'hello', some=11, age=35)