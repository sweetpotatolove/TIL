import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n_list = [list(map(int, input())) for _ in range(N)]

    center = N // 2
    result = 0
    for i in range(0, center+1):
        for j in range(i, N-i):
            if i == 0:
                result += n_list[center][j]
            else:
                result += n_list[center+i][j]
                result += n_list[center-i][j]
    print(f'#{test_case} {result}')

