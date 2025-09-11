import sys

sys.stdin = open('input.txt')

# 모든 터널 정보
tunnel = [
        None,           # 0번 터널 없음
        [[-1, 0], [1, 0], [0, -1], [0, 1]],  # 상하좌우
        [[-1, 0], [1, 0]],  # 상하
        [[0, -1], [0, 1]],  # 좌우
        [[-1, 0], [0, 1]],  # 상우
        [[1, 0], [0, 1]],  # 하우
        [[1, 0], [0, -1]],  # 하좌
        [[-1, 0], [0, -1]]]  # 상좌

def search(x, y, cnt):
    global result
    queue = [[x, y, cnt]]
    visited[x][y] = 1
    while queue:
        x, y, cnt = queue.pop(0)
        if cnt == L:  # 이동하는데 소요한 시간이 L과 같으면 조사 종료
            return
        result += 1  # 현재 위치 총 수에 추가
        for dx, dy in tunnel[data[x][y]]:
            nx = x + dx  # 다음 위치 좌표 계산
            ny = y + dy

            # 1. 영역을 벗어나지 않고
            # 2. 방문한 적 없고
            # 3. 연결된 파이프가 있으면
            '''
                이동 방향의 역 방향으로 접근이 가능하다면 연결된 파이프
                ex) 
                    상좌로 이동 가능한 파이프 정보는 
                    [[-1, 0], [0, -1]]]  # 상좌
                    이곳을 도착점이라 보았을때, 나는 내려가거나 오른쪽으로 이동할때, 이 파이프가 있어야 이동가능
                    그렇다면...
                    하 혹은 우 로 이동하는 좌표 정보는?
                    [[1, 0], [0, 1]],  # 하우
                    
                    내가 이동할 방향 하 -> (1, 0) 의 각각의 역수는 (-1, 0) 
            '''
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] != 0 and not visited[nx][ny] and [-dx, -dy] in tunnel[data[nx][ny]]:
                queue.append([nx, ny, cnt + 1])
                visited[nx][ny] = 1

T = int(input())

for tc in range(1, T + 1):
    # N:세로 크기, M:가로 크기, R:맨홀 세로 위치, C:가로 위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 탈주범이 있을 수 있는 위치의 개수
    visited = [[0] * M for _ in range(N)]  # 해당 위치 방문 여부 체크용 -> 이미 방문 한 적 있는 곳 다시 조사할 필요 없음
    search(R, C, 0)
    print(f'#{tc} {result}')