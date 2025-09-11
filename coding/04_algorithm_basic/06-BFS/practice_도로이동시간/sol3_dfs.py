import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(row, col, acc):     # 행, 열, 누적값
    global min_count

    # 가지치기
    if acc >= min_count:
        return

    if row == N-1 and col == M-1:   # 도착지이면
        min_count = min(min_count, acc) # 여기까지 도달하는 데 든 비용과 최소값 비교
        return

    # 4방향 탐색
    for k in range(4):
        nx, ny = row + dx[k], col + dy[k]

        # 범위를 벗어나거나, 방문한 적 있거나, 길이 아니면 넘어가자
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny]: continue
        if not road[nx][ny]: continue

        # 갈 수 있으면 방문 표시하고 이동
        visited[nx][ny] = 1
        dfs(nx, ny, acc + 1)    # 조사를 떠났다가 돌아왔으면(백트래킹)
                                # 다음 조사 후보군을 조사해야 함
        # 그러므로, 이전에 nx, ny 조사했던 시점은 없었던 일로 해야함
        # 갔었던 적 없는 깨끗한 길로 만들어줘야 함
        visited[nx][ny] = 0


# 입력 처리
N, M = map(int, input().split())
road = [list(map(int, input())) for _ in range(N)]

# 방문 배열 및 최소 이동 횟수 초기화
visited = [[False] * M for _ in range(N)]
min_count = float('inf')

# 시작점 방문처리 후 탐색 시작
visited[0][0] = True
dfs(0, 0, 0) # x, y, 누적값

print(min_count)  # 결과 출력
