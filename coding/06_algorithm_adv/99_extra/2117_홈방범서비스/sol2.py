import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N: 도시의 크기, M: 각 집마다 내는 지원금
    N, M = map(int, input().split())
    # 1: 집 위치
    data = [list(map(int, input().split())) for _ in range(N)]
    # 최종 출력은 집의 개수
    result = 0
    house = []
    for x in range(N):
        for y in range(N):
            if data[x][y]:  # 집이 있다면
                house.append((x, y))    # 집 좌표 추가
    
    # 모든 좌표에 대한 완전 탐색
    for x in range(N):
        for y in range(N):
            '''
            # 해당 좌표와 모든 집들과의 거리를 계산
            # 제일 멀리 있는 집에 도달 할 수 있는 거리를
            # 최대 반지름 r로 잡아서 계산
                # 유클리드 거리 계산법에서 내 좌표는 거리 0으로 보기 떄문에
                # 문제와 조건이 다르므로 거리 계산 후 + 1
            '''
            distances = []
            for hx, hy in house:
                distances.append(abs(x - hx) + abs(y - hy) + 1)
            # 계산된 거리중 가장 멀리 있는 집
            K = max(distances)
            for k in range(K, 0, -1):
                cost = (k*k) + (k-1)*(k-1)
                count = 0       # 범위 k에 속하는 집들
                '''
                    범위 k안에 있는 모든 집들이 몇갠지 센다.
                    세어서, 범위 k일떄 최소 유지 비용과 집들이 내주는 지원금 계산
                '''
                for dist in distances:
                    if dist <= k:   # 범위 k보다 현재 좌표에서 집까지 걸리는 거리가 더 작으면
                        count += 1  # 그 집은 범위 k 서비스 영역 안에 속한다
                # 모든 집들에 대한 조사가 끝나면?
                if (count * M) - cost >= 0:     # 이번 범위에 속한 집들이 충분히 돈을 내면?
                    result = max(result, count) # 결과 반영
                    break

    print(f'#{tc} {result}')