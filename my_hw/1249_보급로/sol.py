import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    # 후보군 사라질 때까지
    while queue:
        # 방문
        nowX, nowY = queue.popleft()
        for i in range(4):
            nx, ny = nowX + dx[i], nowY + dy[i]
            # 행렬 안벗어나야 함
            # 이전에 방문했던 루트보다 누적합 작으면 바꿔치기해야 함
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > (visited[nowX][nowY] + road[nx][ny]):
                    visited[nx][ny] = visited[nowX][nowY] + road[nx][ny]
                    queue.append((nx, ny))

    return visited[N-1][N-1]

C = int(input())
for tc in range(1, C+1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]

    visited = [[float('inf')] * N for i in range(N)]
    visited[0][0] = 0
    print(f'#{tc} {bfs(0, 0)}')


