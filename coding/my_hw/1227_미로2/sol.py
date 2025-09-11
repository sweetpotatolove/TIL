import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(row, col):

    queue = deque()
    queue.append((row, col))

    # 큐에 후보군 없을 때까지 루프
    while queue:
        # 방문
        nowX, nowY = queue.popleft()

        for i in range(4):
            nx, ny = nowX + dx[i], nowY + dy[i]
            # 이동했을 때 행렬 내에 있고, 1이 아니어야 하고, 방문하지 않아야 함
            if 0 <= nx < 100 and 0 <= ny < 100 and road[nx][ny] != 1 and visited[nx][ny] == False:
                queue.append((nx, ny))
                visited[nx][ny] = True
                # 만약 3을 만났다면 return 1
                if road[nx][ny] == 3:
                    return 1

    # 길 못찾았으면 return 0
    return 0

for _ in range(1, 11):
    tc = int(input())
    road = [list(map(int, input())) for _ in range(100)]

    visited = [[False] * 100 for _ in range(100)]

    x = 0
    y = 0
    for i in range(100):
        for j in range(100):
            if road[i][j] == 2:
                x, y = i, j

    visited[x][y] = True
    print(f'#{tc} {bfs(x,y)}')