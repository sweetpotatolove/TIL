import sys
sys.stdin = open('input.txt')
T = int(input())

dxy = [(1,1), (1,-1), (-1,-1), (-1,1)]

def dfs(row, col, cnt, now):
    global r, c, max_count

    if row == r and col == c and cnt >= 4:
        max_count = max(max_count, cnt)
        return

    if now < len(dxy):  # 직진
        nx, ny = row + dxy[now][0], col + dxy[now][1]
        if 0 <= nx < N and 0 <= ny < N:
            if cafe[nx][ny] not in visited:
                visited.append(cafe[nx][ny])
                dfs(nx, ny, cnt + 1, now)
                visited.remove(cafe[nx][ny])
            elif nx == r and ny == c and cnt >= 4: # 최소 4개 이상 디저트 먹은 경우
                                                # 출발 점으로 가려고 한다면 보내줌
                dfs(nx, ny, cnt, now)

    if now < len(dxy) - 1:  # 방향 전환
        nx, ny = row + dxy[now + 1][0], col + dxy[now + 1][1]
        if 0 <= nx < N and 0 <= ny < N:
            if cafe[nx][ny] not in visited:
                visited.append(cafe[nx][ny])
                dfs(nx, ny, cnt + 1, now + 1)
                visited.remove(cafe[nx][ny])
            elif nx == r and ny == c and cnt >= 4:
                dfs(nx, ny, cnt, now + 1)

for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    max_count = -1  # 결과가 없을 경우 -1 출력
    for i in range(0, N-2): 
        for j in range(1, N-1): 
            r, c = i, j
            # 첫 번째 이동을 수동으로 처리하고 DFS 시작
            nx, ny = i + 1, j + 1 
            # 시작점과 첫 방문 디저트가 다를 경우에만 탐색
            if cafe[i][j] != cafe[nx][ny]:
                visited = [cafe[i][j], cafe[nx][ny]]
                # 디저트 2개(시작점, 첫 방문)를 먹은 상태로 DFS 시작
                dfs(nx, ny, 2, 0)
    print(f"#{test_case} {max_count}")
