import sys
sys.stdin = open('input.txt')

#    상  하  좌  우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def search_core(idx, core_count, wire):

    global max_core, min_len, cores

    # 모든 코어를 돌았다면 종료
    if idx == len(cores):
        # 코어 개수가 우선적으로 많고, 개수가 같다면 전선 길이가 짧을 때 기록
        if core_count > max_core or (core_count == max_core and wire <= min_len):
            max_core, min_len = core_count, wire 
        return

    row, col = cores[idx]
    
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]

        path = []
        ok = True

        while 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] != 0:    # 이미 전선이 있거나 core가 있으면
                ok = False
                break
            path.append((nx, ny))
            nx += dx[i]
            ny += dy[i]
        if not ok or not path:          # 길막 당했거나
            continue            # 바로 벽만나서 길이 0이면
        
        
        # 전선 배치
        for x, y in path:
            visited[x][y] = 2
        
        search_core(idx+1, core_count + 1, wire + len(path))    # 와이어 깔았던 칸 길이

        # 되돌리기
        for x, y in path:
            visited[x][y] = 0
    
    # 이 코어는 연결X 다음 코어 보기
    search_core(idx + 1, core_count, wire)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]

    cores = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1 and (i != 0 and i != N-1 and j != 0 and j != N-1):
                cores.append((i, j))

    max_core = 0
    min_len = float('inf')
    visited = [x[:] for x in matrix]
    search_core(0, 0, 0)
    
    print(f'#{test_case} {min_len}')

    