import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col, ok, now_val, now_count):
    global max_road_cnt, K

    if max_road_cnt < now_count:
        max_road_cnt = now_count  
    
    visited[row][col] = True

    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        # 범위 안벗어나고, 다음 길이 내가 갈 수 있는 길이면
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if map_info[nx][ny] < now_val:
                dfs(nx, ny, ok, map_info[nx][ny], now_count + 1)

            # 범위 안벗어나는데, 다음 길이 갈 수 없는 길이면
            else:
                # 담칸을 k만큼 깎았는데 나보다 크거나 이미 봉우리 한번 깎았으면
                if map_info[nx][ny] - K >= now_val or not ok:
                    continue    # 여긴 못감

                else:   # 깎을 수 있으면 깎기
                    dfs(nx, ny, False, now_val -1, now_count + 1) 
    visited[row][col] = False


T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().strip().split())) for _ in range(N)]

    max_road_cnt = 0    # 최장길이 넣을거임

    # 봉우리 찾기
    m = []
    for h in map_info:
        m.append(max(h))
    bong = max(m)   # 봉우리 찾음

    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if map_info[row][col] == bong: # 봉우리일때만 함수 출발
                dfs(row, col, True, map_info[row][col], 1)
    
    print(f'#{test_case} {max_road_cnt}')

    