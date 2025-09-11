import sys

sys.stdin = open('input.txt')

# 터널 인덱스에 따른 갈 수 있는 방향 리스트
tunnel = {
    0:[],
    1:[(-1, 0), (1, 0), (0, -1), (0, 1)],
    2:[(-1, 0), (1, 0)], # 상하
    3:[(0, -1), (0, 1)], # 좌우
    4:[(-1, 0), (0, 1)], # 상우
    5:[(1, 0), (0, 1)],  # 하우
    6:[(1, 0), (0, -1)], # 하좌
    7:[(-1, 0), (0, -1)],# 상좌
}

# 지금 칸에서 갈 방향과 이어져있는, 다음칸에서 갈 수 있는 방향
connect = {
    (-1, 0):(1, 0),
    (1, 0):(-1, 0),
    (0, -1):(0, 1),
    (0, 1):(0, -1),
}

def bfs(nn, mm, rr, cc, LL):
    global underground, tunnel

    visited = [[0]*mm for _ in range(nn)]
    q=[(rr, cc, LL-1)] # 행, 렬, time left
    visited[rr][cc] = 1
    location = 1
    while q:
        ci, cj, t_left = q.pop(0) # 큐에서 꺼내가며
        t_i = underground[ci][cj] # 현재 위치의 파이프 인덱스
        if t_left>0: # 이 위치에서 갈 수 있는 시간이 남아있으면
            for di, dj in tunnel[t_i]: # 파이프 인덱스에 따른 갈 수 있는 방향을 돌아보며
                ni, nj = ci+di, cj+dj
                # 다음칸이 범위내에 있고, 파이프가 있는 위치고,
                if (0<=ni<nn) and (0<=nj<mm) and (visited[ni][nj]==0) and (underground[ni][nj]!=0):
                    # 이동하는 칸의 파이프가 지금 칸의 파이프와 연결돼있다면
                    if connect[(di, dj)] in tunnel[underground[ni][nj]]:
                        q.append((ni, nj, t_left-1)) # 큐에 추가
                        visited[ni][nj] = 1 # 가본곳으로 표시
                        location += 1 # 탈주범이 있을 수 있는 위치 갯수 +=1

    return location

T = int(input())

for tc in range(1, T+1):
    n, m, r, c, L = map(int, input().split()) # 가로, 세로, 행, 열, 시간
    underground = []
    for _ in range(n):
        underground.append(list(map(int, input().split())))
    out = bfs(n, m, r, c, L)
    print(f'#{tc} {out}')