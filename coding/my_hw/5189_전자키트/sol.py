import sys
sys.stdin = open('input.txt')

import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = [num for num in range(1, N)]
    road = list(itertools.permutations(arr))

    min_sum = float('inf')
    for i in road:
        temp_sum = 0
        path = [0] + list(i) + [0]
        for j in range(N):
            temp_sum += matrix[path[j]][path[j+1]]
            if min_sum < temp_sum:
                break
        else:   # for문이 다 돌아간 경우!!!!
            min_sum = temp_sum

    print(f'#{test_case} {min_sum}')