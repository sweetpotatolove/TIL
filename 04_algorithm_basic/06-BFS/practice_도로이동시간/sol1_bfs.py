import sys
sys.stdin = open('input.txt')
from collections import deque

#    상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_road_move_time(row, col):
    # 너비 우선 탐색 -> queue
    # deque의 첫 번째 인자는 iterable 객체이고,
    # 내가 지금 queue에 넣고 싶은 후보군은 (0,0)
    # queue = deque((0,0)) -> queue = deque[0,0] 이렇게 됨
    # queue = deque([(0,0)]) -> 이렇게 해야 올바르게 (0,0)
    # 헷갈리니까 아래와 같이 하자
    queue = deque()
    queue.append((0,0)) # 시작 정점 후보군에 삽입
    distance[0][0] = 0  # 시작 위치까지 이동거리는 0

    # BFS 탐색
    while queue:    # 후보군이 있는 동안
        row, col = queue.popleft()
        # 이 위치에서 4방향에 대한 탐색
        # for k in [(-1,0), (1,0), ..] 가능
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            # 이제 그 다음 탐색지 data[nx][ny]번째가 이동 가능한지 판별
            # 그럴려면 리스트 범위를 벗어나지 않아야 함
            # 그리고, 이전에 방문한 적 없어야 함
            # 그리고, 그 위치가 '길' 이어야 함
            if 0 <= nx < N and 0 <= ny < M and distance[nx][ny] == -1 and data[nx][ny]:
                # 위 조건을 모두 만족하면 후보군에 들 수 있음
                queue.append((nx, ny))
                # 다음 위치까지 도달하는 비용은, 내 위치 비용 + 1
                distance[nx][ny] = distance[row][col] + 1
                # 도착지점에 도착하면, BFS 특성상 가장 빠르게 도착한 길이니
                # 그때까지의 비용을 할당하고 종료
                if nx == N-1 and ny == N-1: # 도착지
                    return
    # 모든 후보군을 다 탐색했지만, return 되어서 함수가 종료된 적이 없다면??
    # 코드가 이곳까지 도달했다면? 도착할 수 없다는 의미
    return -1


# 데이터 입력
# row: N, col: M
N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]
    # map에 넣는 요소는 iterable한 요소
    # 문자열도 iterable
    # 문자열 자체를 받아서 차례대로 순회하여 int로 변경

# 방문 표시를 할거야 -> 우리의 최종 목적이 무엇이냐?
# 해당 위치까지 도달하는 데 걸린 비용이 얼마인지 기록하는 것!
distance = [[-1] * M for _ in range(N)]
    # 내가 n, m 위치에 도달했을 때
    # distance에 기록되어 있는 누적값(최종 결과값)
    # ??

# 시작지점(0,0)은 distance를 0으로 초기화해주면 좋겠다
# (0,0) -> (0,1)로 이동했을 때 발생하는 1 이라는 비용을 어떻게 알까
# (0,0) -> (0,2)로 이동했을 때 발생하는 2 라는 비용을 어떻게 알까
# (0,1)로 갈 때 발생했던 비용 + 1

get_road_move_time(0, 0)
print(distance[N-1][M-1])

