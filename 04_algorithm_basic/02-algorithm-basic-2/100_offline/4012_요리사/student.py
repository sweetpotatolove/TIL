import sys
sys.stdin = open('input.txt')

import itertools

#테스트 케이스 개수 받아서 그 동안 코드 돌리기
T = int(input())
for test_case in range(1, T + 1):
    # 아이템 개수와 콤비 보드 만들기
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    # 재료를 두 그룹으로 나누기
    # 이 때, comb에 뽑힌 재료는 마지막 재료와 같이 사용할 재료이다.
    ingredients = list(range(n))
    comb = list(itertools.combinations(range(n - 1), n // 2 - 1))
    result = -1
    for ing in comb:
        # A_combo는 마지막 재료가 없는 콤보, B_combo는 마지막 재료가 있는 콤보
        A_combo = ingredients[:]
        B_combo = list(ing)
        B_combo.append(n - 1)
        for i in B_combo:
            A_combo.remove(i)
        # 각 조합에 대해서 두개의 맛 콤보의 값을 다 더해 전체 콤보의 맛을 구한다.
        A_taste, B_taste = 0, 0
        for i, j in list(itertools.combinations(A_combo, 2)):
            A_taste += board[i][j] + board[j][i]
        for i, j in list(itertools.combinations(B_combo, 2)):
            B_taste += board[i][j] + board[j][i]
        # 합의 차를 계속 기록하고, 가장 작은 값을 저장한다.
        taste_diff = abs(A_taste - B_taste)
        if result == -1 or taste_diff < result:
            result = taste_diff

    print(f"#{test_case} {result}")