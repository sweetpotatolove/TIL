import sys
sys.stdin = open('input.txt')

op_list = ['+', '-', '*', '/']

def operate(op_ind, n1, n2):
    # 연산자 인덱스로 계산값 반환하도록
    if op_ind == 0:
        return n1+n2
    elif op_ind == 1:
        return n1-n2
    elif op_ind == 2:
        return n1*n2
    elif op_ind == 3:
        return int(n1/n2)
    return 'error'

def dfs(s_num, op_ind, num_rest, op_rest):
    global maximum, minimum

    if sum(op_rest) == 0: # 더 이상 사용한 연산자가 없으면 계산값을 변수에 저장
        result = operate(op_ind, s_num, num_rest[0])
        if maximum < result: # 최댓값 여부 저장
            maximum = result
        if minimum > result: # 최솟값 여부 저장 # 처음에는 maximum 보다 minimum 이 클 수 있으니까 elif 아님!!
            minimum = result
    # 아직 사용 가능한 연산자가 있으면
    for i in range(len(op_list)):
        if op_rest[i] > 0: # 사용할 수 있는 연산자일 경우 재귀
            # main 문 처럼 복사한 연산자 배열로 연산자를 사용해가면서
            op_rest_copy = op_rest[:]
            op_rest_copy[i] -= 1
            # 연산 시작 숫자는, 인자로 받은 시작숫자와 연산자, 그리고 남은 숫자 리스트 중에서 맨 첫번째 숫자로 계산
            # 연산자 인덱스를 다음 재귀 연산자에 넣어줌
            dfs(operate(op_ind, s_num, num_rest[0]), i, num_rest[1:], op_rest_copy)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arith_in = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    maximum = -1000000000 # 최댓값 담을 변수를 문제 상에서 가장 작은수로 초기화
    minimum = 1000000000 # 최솟값 담을 변수를 문제 상에서 가장 큰 수로 초기화
    # 사칙연산 돌아보면서
    for i in range(len(op_list)):
        if arith_in[i] > 0: # 사용할 수 있는 연산자이면
            # 복사한 연산자 배열로 연산자를 사용해가면서
            arith = arith_in[:]
            arith[i] -= 1
            # 연산 시작 숫자, 연산자 인덱스, 남은 숫자들, 연산자 사용하고 남은 연산자 갯수
            dfs(numbers[0], i, numbers[1:], arith)

    print(f'#{tc} {maximum - minimum}')
