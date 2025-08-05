import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 정류소 도표화
    station = [0 for _ in range(N+1)]
    # 충전소 위치 표시
    for i in data:
        station[i] = 1
    print(station)

    count = 0
    now = K     # 현재 위치 -> 처음 = 0 + 최대 이동 가능 거리
    charge = 0  # 마지막 충전 위치 -> 처음 = 0
    while now < N:
        if station[now] == 1:   # 현재 위치에 충전기가 있으면
            count += 1          # 충전 횟수 += 1
            charge = now        # 마지막 충전 위치를 지금으로 설정
            now += K            # 현재 위치 += 최대 이동 거리
        else:               # 현재 위치에 충전기가 없으면 뒤로 돌아가기
            now -= 1

        # 마지막 충전 위치까지 후진했다 -> 실패
        if charge == now:
            count = 0
            break

    print(f'#{tc} {count}')
