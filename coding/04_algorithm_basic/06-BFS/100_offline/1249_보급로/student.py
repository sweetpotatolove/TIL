import sys

sys.stdin = open('input (1).txt', 'r')

from collections import deque

#    상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_minimum_time(N):
    queue = deque()

    # x,y,time
    queue.append((0, 0, 0))

    # 이전과 같은 방식으로 하면 시간복잡도가 말도 안됨. 따라서 cost_time이라는 맵을 만들어서 해당하는 곳에 가장 작은 cost를 항상 최신화 해줄 거임.
    # 따라서 무한대로 크게 만들어 놓기
    cost_time = [[float('inf')] * N for _ in range(N)]
    cost_time[0][0] = 0

    while queue:
        row, col, time = queue.popleft()

        # 위치를 4방향으로 조사
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]

            # 다음에 조사할 곳이 범위 밖이면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 지금까지 누적된 time과 해당 칸의 cost까지 더했을 때 그 곳에 저장되어 있던 최솟값인 cost_time이랑 비교
            # 지금 진행 중인게 더 크면 이건 더이상 조사할 가치가 없는 루트임.
            if time + arr[nx][ny] >= cost_time[nx][ny]:
                continue

            # 이건 어차피 제일 빠른 걸 조사하는게 아니기 떄문에 필요 없는 조건
            # if nx == N-1 and ny == N-1:
            #     cost_time[nx][ny]

            # 위 조건이 아니면 cost_time에 값을 넣어주기
            cost_time[nx][ny] = time + arr[nx][ny]
            # queue에 넣어주기
            queue.append((nx, ny, time + arr[nx][ny]))

    return cost_time[N - 1][N - 1]


T = int(input())

for tc in range(1, T + 1):
    # 입력을 내가 원하는 데이터 타입으로 받기 완료
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # N에 대한 그걸 줘.
    result = find_minimum_time(N)

    print(f'#{tc} {result}')
