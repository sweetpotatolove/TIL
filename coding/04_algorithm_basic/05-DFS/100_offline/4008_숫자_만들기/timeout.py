import sys
sys.stdin = open('input.txt')

'''
    시간 초과 발생
    순열을 구하면 풀 수 있을 것 같지만... -> 실제로 풀 수는 있다.
    그러나 만능인줄 알았던 itertools 마저... 엄청난 순열의 경우의 수는 견디지 못했다.
'''
import itertools


def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2
    if oper_idx == 1:
        return num1 - num2
    if oper_idx == 2:
        return num1 * num2
    if oper_idx == 3:
        return int(num1 / num2)

def search(level, total):
    global min_result, max_result

    if level == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 순서대로 연산자 적용
    op = operators_permutation[level - 1]  # 해당 level에서 사용할 연산자
    search(level + 1, cal(total, numbers[level], op))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = 1e9
    max_result = -1e9

    operators = []
    for i in range(4):
        operators.extend([i] * opers[i])  # 연산자별 개수만큼 연산자를 리스트에 추가

    # 연산자 순열을 구한 후, 순열을 이용하여 계산
    for operators_permutation in set(itertools.permutations(operators)):
        search(1, numbers[0])

    print(f'#{tc} {max_result - min_result}')
