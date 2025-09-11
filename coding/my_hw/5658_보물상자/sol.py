import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())
    change = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    change_num = deque()
    for i in range(len(numbers)):
        if numbers[i] in change.keys():
             change_num.append(change[numbers[i]])
        else:
            change_num.append(int(numbers[i]))

    total_num = set()
    for j in range(N // 4):
        for m in range(0, N, N // 4):
            val = 0
            for k in range(N // 4):
                val += change_num[m + k] * (16 ** (N // 4 - k - 1))
            total_num.add(val)
        temp = change_num.pop()
        change_num.appendleft(temp)

    sort_total_num = sorted(total_num, reverse=True)

    print(f'#{test_case} {sort_total_num[K-1]}')

d