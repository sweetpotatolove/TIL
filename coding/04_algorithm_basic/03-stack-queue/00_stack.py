# list를 사용하여 자료구조 stack을 구현하자
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack[-1])    # stack 리스트의 마지막을 확인함으로써 pop()을 사용했을 때 뭐가 나올지 알 수 있음
print(len(stack))
print(stack.pop())
print(stack.pop())
