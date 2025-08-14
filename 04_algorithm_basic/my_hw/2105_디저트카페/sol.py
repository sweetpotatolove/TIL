import sys
sys.stdin = open('input.txt')
T = int(input())

dxy = [(1,1), (1,-1), (-1,-1), (-1,1)]

def dfs(row, col, cnt, now):
    global r, c, max_count

    if row == r and col == c:
        max_count = max(max_count, cnt)
        return

    if now < len(dxy):  # 직진
        nx, ny = row + dxy[now][0], col + dxy[now][1]
        if 0 <= nx < N and 0 <= ny < N:
            if now == cafe[nx][ny] == visited[0]:

            if cafe[nx][ny] not in visited:
                visited.append(cafe[nx][ny])
                dfs(nx, ny, cnt + 1, now)
                visited.remove(cafe[nx][ny])

    if now < len(dxy) - 1:  # 드리프트
        nx, ny = row + dxy[now + 1][0], col + dxy[now + 1][1]
        if 0 <= nx < N and 0 <= ny < N:

            if cafe[nx][ny] not in visited:
                visited.append(cafe[nx][ny])
                dfs(nx, ny, cnt + 1, now + 1)
                visited.remove(cafe[nx][ny])

    # 제자리로 돌아가지 못하고
    # 아니면 방문했던 곳이거나
    # 범위에 벗어났다면
    # 그래서 여기까지 왔다면
    return

for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    max_count = 0
    for i in range(0, N-2): # row가 젤 밑줄 못감
        for j in range(1, N-1): # col은 첫줄, 마지막줄 못감
            r, c = i, j
            visited = [cafe[i][j]]
            dfs(i + 1, j + 1, 1, 0)
    print(max_count)