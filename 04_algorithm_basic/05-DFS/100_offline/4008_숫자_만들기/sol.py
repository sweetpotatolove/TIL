import sys
sys.stdin = open('input.txt')

'''
    oper_idx -> 0 ~ 3
    0: +
    1: -
    2: *
    3: /
'''
def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2

    if oper_idx == 1:
        return num1 - num2

    if oper_idx == 2:
        return num1 * num2

    if oper_idx == 3:
        return int(num1 / num2)


# 시작점: 첫 번째 숫자
# 끝점: 모든 수(연산자)를 사용할 때 까지
# 파라미터: 특정 시점에서 계산된 결과값
def search(level, total):
    global min_result, max_result

    if level == N:      # 모든 수를 다 사용했다면
        # 지금까지의 연산 결과로 최대, 최소 값 갱신
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 아직 모든 수를 다 쓰지 못했다면
    # 4개의 연산자를 확인
    for i in range(4):
        if opers[i] == 0:  # 남은 연산자가 없으면 통과
            continue
        # 있으면 그 연산자를 사용해서
        opers[i] -= 1
        # 사용한 수의 개수 + 1, 총합과 이번 수를 i 번째 연산자로 연산
        search(level + 1, cal(total, numbers[level], i))
        # 모든탐색을 마치고 돌아 왔다 -> 연산을 끝냈거나, 연산을 끝낼 조건을 만족하지 못하고 돌아왔다.
        # 이때, 이번 연산자를 사용하지 않았던 상황으로 되돌리고
        # 다음 연산자에 대해 동일한 조건 수행.
        opers[i] += 1


T = int(input())

for tc in range(1, T + 1):
    # N: 숫자의 개수
    N = int(input())
    # 연산자 정보 각각 +, -, *, / 의 개수를 의미
    # [2, 0, 1, 1] 인 경우 + 2개, *, / 가 1개씩 사용되어야 한다는 의미
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 1e9    # 충분히 큰값으로 점점 작아질 값
    max_result = -1e9   # 충분히 작은 값으로 점점 커질 값

    search(1, numbers[0])
    print(f'#{tc} {max_result - min_result}')
