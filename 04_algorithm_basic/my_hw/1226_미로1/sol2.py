import sys
sys.stdin = open('input.txt')
    # 상  하  좌  우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col):

    global ok
    
    # 가지치기
    if ok:      # 도착지에 도달할 수 있는 미로라면 다른 길 더 볼 필요 없음
        return

    if matrix[row][col] == 3:
        ok = True   # 한번이라도 3에 도달했다면 ok는 True가 될 것임
        return

    # 4방향 탐색
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if visited[nx][ny] == 1:    # 방문한적 있거나 벽이면 못감
            continue
        
        # 방문할 수 있다면
        visited[nx][ny] = 1
        dfs(nx, ny)

        # 다시 돌려놓기
        visited[nx][ny] = 0    

for _ in range(10):
    test_case = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    visited = [row[:] for row in matrix]
    ok = False
    dfs(1,1)

    if ok:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')

    