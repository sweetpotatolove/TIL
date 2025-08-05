import sys
sys.stdin = open('input.txt')

# 시간초과 발생
def goby_bus(road, now, count, battery):
    global res

    # 만약 배터리가 없다면 돌아감
    if battery < 0 or res <= M:
        return

    # 배터리가 모두 닳지 않았으며 현재 위치가 종점이라면
    if now == N:
        if res > count:
            res = count
        return True

    # 만약 현재 위치에 충전소가 없다면
    if road[now] == 0:
        # 앞으로 전진만 할 수 있음
        if goby_bus(road, now + 1, count, battery - 1):
            return True
    # 만약 현재 위치에 충전소가 있다면
    else:
        # 앞으로 전진
        if goby_bus(road, now + 1, count, battery - 1):
            return True
        # 충전 후 전진
        if goby_bus(road, now + 1, count + 1, K - 1):
            return True


T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    road = [0] * (N + 1)
    chargers = list(map(int, input().split()))
    # chargers의 경로를 road에 저장함
    for idx in chargers:
        road[idx] = 1
    res = M + 1
    goby_bus(road, 0, 0, K)

    print(f'#{tc}', end=' ')
    if res > M:
        print(0)
    else:
        print(res)