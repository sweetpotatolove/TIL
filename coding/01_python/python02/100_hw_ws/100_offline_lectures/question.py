class ParentA:
    # 단어를 드래그하거나 포커싱을 한다음
    # ctrl + D 를 하면 (주의. 대소문자 구분 안됨) 동일한 글자 모두 다중 포커싱
    # alt + 위아래 방향키로 줄바꿈
    # alt shif + 위아래로 복제
    # ctrl + 좌우 : 단어 단위로 커서 이동
    # ctrl + shift + 좌우: 단어 단위로 드래그
    # ctrl + shift + home/end: 왼쪽 끝으로 그래그 / 오른쪽 끝으로 드래그
    # 'ctrl + k' 'ctrl + s' : VSCode shortcut 설정
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_a = 'Child'

    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value() 

'''
1. 다중 상속 super() 사용 예시
    __init__에 super()를 사용해서 부모 클래스를 호출한 이유가 궁금해요
    해당 코드가 없으면 아래에 있는 child.show_value() 진행 시 
    AttributeError: 'Child' object has no attribute 'value_a'. Did you mean: 'value_c'?
    오류가 발생합니다. 부모 클래스는 해당 클래스 내에서 
    __init__ 함수로 초기화가 되어있으므로 사용이 가능한거 아닌가요,,,
'''