import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    queue = deque()

    if M == 0:
        print(f'#{tc} OFF')
        continue

    # M을 2진수 변환 (큐 활용)
    while M:
        queue.appendleft(M % 2)  # 왼쪽으로 삽입하여 순서 유지
        M //= 2

    # 필요한 만큼 0을 채워 맞춘 후 뒤에서 N개를 확인
    while len(queue) < N:
        queue.appendleft(0)

    # 마지막 N개가 모두 1인지 확인
    result = 'ON'
    for _ in range(N):
        if queue.pop() == 0:
            result = 'OFF'
            break

    print(f'#{tc} {result}')

