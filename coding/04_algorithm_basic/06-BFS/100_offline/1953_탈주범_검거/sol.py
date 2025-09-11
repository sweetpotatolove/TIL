import sys

sys.stdin = open('input.txt')

'''
    A형은 시간초과가 문제일 거라 생각하시는 당신!
    deque를 쓰지 않고 그냥 list로 queue를 대체하여도 문제는 풀린다.
    정말 시간 초과가 걸림돌일까?
    시간초과는 생각보다 지엽적인 문제이다.
    문제를 해결하기 위한 올바른 접근법이었을지 다시 체크.
'''

# 모든 터널 정보
tunnel = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상하좌우
    2: [(-1, 0), (1, 0)],  # 상하
    3: [(0, -1), (0, 1)],  # 좌우
    4: [(-1, 0), (0, 1)],  # 상우
    5: [(1, 0), (0, 1)],  # 하우
    6: [(1, 0), (0, -1)],  # 하좌
    7: [(-1, 0), (0, -1)],  # 상좌
}


# cnt: 현재까지 누적된 시간
def search(x, y, cnt):
    global result  # 이동 가능 총 수
    queue = [(x, y, cnt)]  # 첫 출발점
    visited[x][y] = 1  # 방문 표시
    while queue:
        x, y, cnt = queue.pop(0)
        if cnt == L:  # 이동하는데 소요한 시간이 L과 같으면 조사 종료
            return
        result += 1  # 현재 위치 총 수에 추가
        # 내 위치의 터널 정보를 이용해 다음 조사 가능 지역 조회
        for dx, dy in tunnel[data[x][y]]:
            '''
            # 내 위치가 2 였다면
            tunnel[2] => [(-1, 0), (1, 0)]
            dx, dy = -1, 0  첫 번째 순회
            dx, dy = 1, 0   두 번째 순회
            '''
            nx = x + dx  # 다음 위치 좌표 계산
            ny = y + dy
            # 다음 위치가 이동 가능하고, 0이 아니면서, 방문한 적 없다면
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] and not visited[nx][ny]:
                # 다음 위치의 터널 정보를 통해 이동 가능한지 판별
                for cx, cy in tunnel[data[nx][ny]]:
                    '''
                    다음 이동 위치가 6이라면
                    tunnel[6] => [(1, 0), (0, -1)]
                    cx, cy = 1, 0  첫 번째 순회
                    cx, cy = 0, -1   두 번째 순회

                    이동해왔던 이전 터널 정보 dx, dy (-1, 0) (위로 이동)과
                    다음 위치의 터널 정보 cx, cy (1, 0) (아래에서 입장 가능) 의 합을 판별
                    각 좌표의 합이 각각 0이라면 (서로 역순이라면)
                    이동 가능
                    '''
                    if cx + dx == 0 and cy + dy == 0:
                        # 다음 이동 위치 방문 표시 후,
                        # 다음 조사 대상에 cnt 1 증가 하고 이동
                        visited[nx][ny] = 1
                        queue.append((nx, ny, cnt + 1))
                        break  # 한번이라도 0인 경우가 나왔다면 이동 가능하므로 조사 종료


T = int(input())
for tc in range(1, T + 1):
    # N:세로 크기, M:가로 크기, R:맨홀 세로 위치, C:가로 위치, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0          # 탈주범이 있을 수 있는 위치의 개수
    visited = [[0] * M for _ in range(N)]   # 해당 위치 방문 여부 체크용 -> 이미 방문 한 적 있는 곳 다시 조사할 필요 없음
    search(R, C, 0)     # 맨홀 좌표에서 조사 시작.
    print(f'#{tc} {result}')