import sys
sys.stdin = open('input.txt')

def postorder(node_idx):
    global expression
    # 0번 노드 사용하지 않음.
    if 0 < node_idx <= N:   # 조회 해야 하는 index 번호가 tree의 전체길이보다 작은 동안에만
        postorder(int(tree[node_idx][2]))     # 현재 tree의 각 자식 정보가 문자열로 되어 있으므로
        postorder(int(tree[node_idx][3]))     # 정수형으로 변경하여 자식 정보 조회하러 이동
        # 끝까지 다 조사했으면, 현재 값을 표현식에 저장
        expression.append(tree[node_idx][1])

# 중위 표기법에 따라 연산
def calc(expression):
    stack = []  # 연산 식이 들린 켱우는 없으므로 특별한 조건 없이 실행
    for char in expression:
        # 정수면 피연산자 -> stack에 삽입 (정수로 변환후)
        if char.isnumeric(): stack.append(int(char))
        else:
            y = stack.pop()
            x = stack.pop()
            if char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
            elif char == '*':
                stack.append(x * y)
            elif char == '/':           # 나눗셈인 경우 몫만 계산
                stack.append(x // y)
    print(stack)
    return stack[0]

for tc in range(1, 11):
    result = 0
    N = int(input())
    # 입력 받는 값을 tree로 그대로 활용
    tree = [input().split() for _ in range(N)]
    # 0번 인덱스는 사용하지 않을 예정.   => 리스트의 index를 노드의 번호로 쓰기 위함.
    tree.insert(0, 0)
    # 각 노드간의 정보의 길이가 일치하지 않아, 순회시 indexError가 발생함
    # 길이를 모두 하나로 동일하게 변환 (0번 노드는 쓰지 않음)
    for idx in range(1, len(tree)):
        while len(tree[idx]) < 4:
            tree[idx].append('0')
    print(tree) # 결과 출력
    expression = []     # 후위 표기법 값들을 저장할 리스트
    # 후위 순회 시작
    inorder(1)      # 1번노드가 root노드
    print(expression)   # 만들어진 중위 표현식 확인
    print(f'#{tc} {calc(expression)}')

