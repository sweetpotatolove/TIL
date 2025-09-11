class ParentA:
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
        # super().init() # ParentA 클래스의 init 메서드 호출
        self.value_c = 'Child'
    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value() 
# AttributeError: 'Child' object has no attribute 'value_a'. Did you mean: 'value_c'?
# 속성 에러 (value_a가 없어서 너 c를 말하는거야? 하고 물어보는 거)
# Chile의 생성자가 부모 생성자를 덮어 씌운 것
# 만약 자식 생성자도 두고, 부모 생성자도 남겨두고 싶다면?
# super().__init__() 부모 생성자를 호출함으로써 value_a에 ParentA을 넣을 수 있음

# ---------------------------------------------------------------------------------------------------------------------------

# 단어 드래그 하거나 포커싱 한 다음
# ctrl + D 하면 (주의. 대소문자 구분 안됨)
# 동일한 글자 모두 다중 포커싱 됨~!!

# alt + 위아래 방향키로 줄바꿈
# alt + shift + 위아래: 위아래 복제
# ctrl + 좌우 : 단어 단위로 커서 이동
# ctrl + shift + 좌우: 단어 단위로 드래그
# ctrl + shift + home/end : 왼쪽 끝으로 드래그 / 오른쪽 끝으로 드래그

