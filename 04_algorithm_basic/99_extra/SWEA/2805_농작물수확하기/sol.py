import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    global result
    q = deque([(x, y, 0)])
    while q:
        x, y, cnt = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 아직 반지름 내에 있고, 방문한적 없다면
            if cnt < mid and data[nx][ny] != -1:
                result += data[nx][ny]  # 값 추가하고
                data[nx][ny] = -1       # 방문표시
                q.append((nx, ny, cnt + 1))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 입력값이 공백 없이 주어지므로, 문자열 자체를 순회하여 정수로 변환
    data = [list(map(int, input())) for _ in range(N)]
    mid = N//2                # 정중앙 값 저장
    result = data[mid][mid]   # 정중앙 수확
    data[mid][mid] = -1       # 방문 표시
    search(mid, mid)
    # for d in data:
    #     print(d)
    print(f'#{tc} {result}')
