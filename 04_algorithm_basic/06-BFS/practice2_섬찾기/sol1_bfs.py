import sys
sys.stdin = open('input.txt')

from collections import deque

#         상      하       좌      우       좌상     좌하    우상     우하
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

def find_island(island, x, y):
    # deque를 사용하여 BFS 구현
    queue = deque([(x, y)])
    island[x][y] = 0  # 시작점 방문 처리

    # BFS 탐색
    while queue:
        cx, cy = queue.popleft()  # 현재 위치

        for dx, dy in dxy:  # 8방향 탐색
            nx, ny = cx + dx, cy + dy

            # 범위를 벗어난 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이미 방문했거나 바다인 경우
            if island[nx][ny] == 0:
                continue
                
            # 연결된 땅 발견
            queue.append((nx, ny))
            island[nx][ny] = 0  # 방문 처리

# 입력 처리
n, m = map(int, input().split())  # 지도의 크기
arr = [list(map(int, input())) for _ in range(n)]  # 지도 입력
island_cnt = 0  # 섬의 개수

# 모든 위치를 확인하여 BFS 실행
for i in range(n):
    for j in range(m):
        # 땅인 경우에만 BFS 탐색 시작
        if arr[i][j] == 1:
            find_island(arr, i, j)  # BFS로 연결된 땅 모두 탐색
            island_cnt += 1  # 하나의 섬 발견

print(island_cnt)  # 결과 출력

