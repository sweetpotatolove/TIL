import sys

sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        now = queue.popleft()
        nowX = now[0]
        nowY = now[1]

        # 4방향 탐색
        for k in range(4):
            nx, ny = nowX + dx[k], nowY + dy[k]

            # 조건에 맞으면 후보군에 넣기
            if 0 <= nx < 16 and 0 <= ny < 16 and road[nx][ny] != 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

                if road[nx][ny] == 3:  # 도착지점
                    return 1
    return 0


for t in range(10):
    test_case = int(input())
    road = [list(map(int, input())) for i in range(16)]

    visited = [[False] * 16 for _ in range(16)]
    # x = 0
    # y = 0
    # for i in range(16):
    #     for j in range(16):
    #         if road[i][j] == 2:
    #             x = i
    #             y = j

    print(f'#{t + 1} {bfs(1, 1)}')
