import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def building(row, col):

    global max_building
    
    b_len = 1
    
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        while 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0:
                break
            b_len += 1
            nx += dx[i]
            ny += dy[i]
        
        if max_building < b_len:
            max_building = b_len
        b_len = 1
    
        
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    max_building = 0
    
    for x in range(N):
        for y in range(M):
            if matrix[x][y] == 1:
                building(x, y)

    print(f'#{test_case} {max_building}')