import sys
sys.stdin = open('input.txt')

'''
    깊이 우선 탐색 시 소요 시간을 줄여보기 위해 조건을 하나 더 추가해봤지만...
    여전히 시간초과 발생.
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search():
    stack = [(0, 0, 0)]
    visited[0][0] = 0  # 현재 위치에 대한 시간 갱신
    while stack:
        # 좌표, 누적 된 시간
        x, y, acc_time = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # 1. 범위를 벗어나지 않고
            # 2. 다음 방문 위치가 지금까지 걸린 시간 + 다음 위치까지 걸리는 시간보다 적은동안
                # 2-1. 이전에 한 번 방문 한적이 있을 수 있음.
                # 2-2. 이번 경우의 수에 더 빨리 도착 했을 수도 있음.
                # 2-3. 똑같은 좌표에 더 오랜 시간 걸려서 도착한다면 유망성 없음.
            # 3. 이전에 누군가가 깊이 우선 탐색으로 최종 목적지에 도착한 적이 있다면,
                # 3-1. 그때까지 누적된 값이 내 현재 누적값보다 커야지만 조사할 가치가 있음.
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > acc_time + data[nx][ny] and visited[N-1][N-1] > acc_time:
                new_acc_time = acc_time + data[nx][ny]
                stack.append((nx, ny, new_acc_time))    # 다음 좌표 및 갱신된 누적시간으로 후보군 삽입
                visited[nx][ny] = new_acc_time          # 다음 위치 누적 시간 갱신

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    result = 0
    # 충분히 오래 걸릴 시간 -> 최대 복구시간 을 모든 칸에 대해서 적용
    maximum_time = 100 * 100 * 9
    # 방문 여부 확인용 값.
    visited = [[maximum_time] * N for _ in range(N)]
    search()
    print(f'#{tc} {visited[N-1][N-1]}')