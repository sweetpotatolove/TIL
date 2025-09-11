import sys
sys.stdin = open('input.txt')
'''
    1. 어느 지점에서 영역을 지정할지 정할 기준이 있나?
        1-1. 제일 먼저 찾아야 할게 아마 이거일듯? 
        1-2. 모든 좌표 x,y에서 조사를 시작하도록 하자.
    2. 그 좌표 x,y에서 범위 r 만큼에 도달할 수 있는지는 어떻게 암?
        2-1. 델타 탐색으로 상하좌우를 조사 해야 할 듯?
        2-2. 델타 탐색 형식이지만, 결국 최단경로 구하듯,
            시작 정점 위치에서 너비우선 탐색으로 인접 정점 조사해가며
            누적되는 거리들을 세어보면, 그 거리가 범위 r만에 도달할 수 있는 위치가된다.
        2-3. BFS -> queue (dequeue)
    3. 내 현재위치부터, r이 점점 증가해 나가는 형식으로 코드를 짜
        3-1. r이 1일떄부터 시작해서..
        3-2. 그 위치 기준 너비우선 탐색을 진행할 건데
        3-3. 그 상하좌우가, 도시 범주를 벗어나지 않고, 방문한적 없을때만,
        3-4. 이 조사를, 다음 후보군이 있는 동안!
    4. 근데, r이 무한정 커질수는 없음!
        4-1. 최대로 커질 수 있는 기준점이 있음
            -> 최소 비용 계산식 r*r+(r-1)*(r-1)
            -> 내가 r이 충분히 커져서, 그 범위안에 집들이 있다면, 그 집들의 개수를 세고,
                (집의 개수 * M) - (r*r+(r-1)*(r-1)) >= 0
                양수 일때만, 서비스 영역으로 만들수 있음.
        
'''

from collections import deque

# 델타 탐색용 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS(x, y):
    global result
    # visited를 매 좌표 x, y마다 만들어서 써야한다.
    visited = [[0] * N for _ in range(N)]
    # 시작 좌표를 q에 넣는다.
    q = deque([(x, y)])
    # 현재 위치 방문표시
    visited[x][y] = 1

    # 이번 조사에서 얻을 수 있는 집들을 세자.
    house_count = data[x][y] # 내 현재위치의 정보
    # 이번 조사의 범위
    r = 1
    # 범위가 1일때, 이익 계산
    cost = r * r + (r-1) * (r-1)
    if (house_count * M) - cost >= 0:
        result = max(result, house_count)

    while q:
        # 조사를 시작했다? -> 범위가 1 증가 할 것이다.
        r += 1
        cost = r * r + (r-1) * (r-1)

        # 현재 q에 들어있는 값들의 수 만큼 반복해서 거리 측정
        # 후보군에 들어있었던 좌표들
            # (이전 범위로 찾은 호보군들)
            # 예를들어, 범위를 벗어나지 않았다, 방문한적 없다.
        for _ in range(len(q)):
            x, y = q.popleft()

            # 4방향 탐색
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                # 너비우선탐색 단골 조건
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    # 여기 방문했는데 요기 집이있네? 집 개수 1증가
                    if data[nx][ny]:
                        house_count += 1
                    q.append((nx, ny))  # 다음 후보군에 추가
            # 이번 범위에서 얻어낸 집들의 수를 기준으로...
            # 서비스 영역에 대한 이익 계산
            if (house_count * M) - cost >= 0:
                result = max(result, house_count)


T = int(input())
for tc in range(1, T+1):
    # N: 도시의 크기, M: 각 집마다 내는 지원금
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 최종 출력은 집의 개수
    result = 0

    # 완전탐색
    for x in range(N):
        for y in range(N):
            BFS(x, y)

    print(f'#{tc} {result}')