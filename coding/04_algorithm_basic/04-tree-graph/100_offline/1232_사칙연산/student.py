import sys
sys.stdin = open('input.txt')


# 사칙연산 수행 함수
def operating(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x // y


# 연산자 확인 함수
def oper_check(data):
    op = {'+', '-', '*', '/'}
    return data in op


# 전위순회 함수
def preorder_traversal(idx):
    # 노드의 수만큼 실행
    if idx <= n:
        # 현재 값을 받을 변수
        value = tree[idx][1]
        # 현재값이 연산자일 때
        if oper_check(value):
            # 왼쪽 트리의 값 호출
            x = preorder_traversal(int(tree[idx][2]))
            # 오른쪽 트리 값 호출
            y = preorder_traversal(int(tree[idx][3]))
            # 연산 수행
            return operating(x, value, y)
        # 현재 값이 정수일대
        else:
            # 값 리턴
            return int(value)


for tc in range(1, 11):
    n = int(input())
    tree = [None] * (n + 1)

    for idx in range(1, n + 1):
        tree[idx] = list(input().strip().split())
    print(tree)
    result = preorder_traversal(1)

    print(f'#{tc} {result}')