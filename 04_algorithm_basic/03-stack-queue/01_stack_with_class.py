class Stack:
    # 생성자 함수: 스택 자료구조 인스턴스 생성 시, 이 자료구조의 최대 크기도 함께 넘겨줘야 함
    def __init__(self, capacity=10):
        self.capacity = capacity    # 이 자료구조의 최대 수용 가능 공간(기본값 10)
        self.items = [None] * capacity   # 내 최대 크기만큼 리스트를 None으로 채운다
        self.top = -1   # 왜 top이 0이 아닌 -1로 초기화 하느냐?
                        # 여기서 -1은 리스트의 마지막을 의미하는 것이 아닌
                        # push 연산 진행 시, top의 값을 1 증가시키고 그곳에 값을 삽입할 예정

    # 삽입할 수 있는 공간을 생성자 함수로 만들어 놨으니, 이제 값을 삽입하자
    # 주어진 값을 삽입
    def push(self, item):
        # push를 계속 해서 스택이 가득 찼을 때 또 삽입하면 IndexError 발생
        # 스택이 가득 찼음을 확인해야 함 -> 예외처리
        if self.is_full():
            print('Stack is Full!!')
            return
            # 또는 에러 직접 발생시키기 가능 -> raise IndexError('Stack is Full')
        self.top += 1   # 올바른 삽입 위치 찾기(top의 위치를 옮긴 후 그 자리에 삽입)
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            print('Stack is Empty!!')
            return
        item = self.items[self.top]     # 제거할 값은 top위치에 있음
        self.items[self.top] = None     # 왜 그런지 설명쓰...
        self.top -= 1
        return item

    def is_full(self):
        # stack이 가득 찼음을 어떻게 알 수 있을까?
        return self.capacity -1 == self.top     # top의 최대 위치가 어디인지 확인해 봤을 때
                                                # 최대 용량의 -1에 top이 도달했다면 full?
    # 스택이 비었는지 확인
    # top이 -1일 때 스택이 비어있다고 판단할 수 있음
    def is_empty(self):
        return self.top == -1



    
stack = Stack()
# print(stack.item)

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
#print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
