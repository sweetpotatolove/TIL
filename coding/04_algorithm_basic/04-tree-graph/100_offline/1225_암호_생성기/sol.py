import sys
sys.stdin = open("input.txt")
# from collections import deque


# tc 10개
for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))

    # data = deque(data)
    # 현재 진행중인 사이클에서 빼야할 값의 크기를 알고 있어야 한다.
    cnt = 1
    while data[-1] > 0:
        # 한 사이클은 5까지 빼는게 한 사이클이다.
        # 빼고자 하는 값의 크기가 5초과가 되면 다시 1로 돌아가야 한다.
        if cnt == 6:
            cnt = 1

        # 첫번째에 위치한 숫자 감소한 뒤, 맨 뒤로 보낸다.
        data.append(data.pop(0) - cnt)
        cnt += 1

    # 데이터 마지막 값은 0으로 고정 (음수 -> 0으로)
    data[-1] = 0

    print(f'#{tc}', end=' ')
    print(*data)