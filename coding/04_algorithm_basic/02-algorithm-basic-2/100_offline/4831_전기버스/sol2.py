import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 정류장 정보
    station = list(map(int, input().split()))

    count = 0       # 충전 횟수
    prev = 0        # 이전 위치
    now = K         # 현재 위치
    candidate = []  # 충전 가능 후보군
    idx = 0         # 충전소 위치 정보
    while True:
        # 충전소 배열 station의 범위를 벗어나지 않고
        # 충전소 위치가 이전 위치보다는 크고
        # 현재 위치 보다는 작거나 같을때
        if idx < M and station[idx] > prev and station[idx] <= now:
            candidate.append(station[idx])  # 해당 충전소 정보를 후보군에 추가
            idx += 1        # 다음 충전소 조사
            continue        # 모든 후보군 조사를 위해 아래 코드 무시
        elif not candidate: # 충전 가능 후보군이 없다면
            count = 0       # 실패
            break
        now = candidate[-1] # 현재 위치를 후보군 마지막 충전소로 이동
        candidate.clear()   # 모든 후보군 제거
        count += 1          # 충전 횟수 1 증가
        prev = now          # 이전 위치를 현재로 변경 후,
        now += K            # 최대 이동 가능 거리 만큼 이동
        if now >= N:        # 종점을 지나쳤다면 종료
            break
    print(f'#{tc} {count}')
