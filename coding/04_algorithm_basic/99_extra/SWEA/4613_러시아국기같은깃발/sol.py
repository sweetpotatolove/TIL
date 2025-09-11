import sys
sys.stdin = open('input.txt')



def search(K, cnt, v):
    global result
    if cnt > result:    # 가지치기
        return
    if K == N-1:        # 마지막 전줄 까지 조사했다면
        if all(visited):    # 모든 색을 썼다면,
            if cnt < result:    # 교환
                result = cnt
    else:
        # 다음 색으로 넘어가버렸다면 이전 색을 칠하지 않음
        # 흰색을 칠하는 중이라면, 흰색을 계속 조사하지만
        # 한번이라도 파란색으로 조사를 넘어갔다면 흰색으로 돌아가지 않음
        for i in range(v, 3):
            visited[i] += 1     # 현재 색 칠한 횟수 증가
            # 현재 사용하려는 색을 누적값에 더하고, 칠하는 중인 색을 다음 조사 위치로 전송
            search(K+1, cnt + M - WBR[K][i], i)
            visited[i] -= 1     # 이번 색을 칠하지 않고 다음색으로 넘어가는 조사사


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    WBR =[[0, 0, 0] for _ in range(N)]

    # 각 줄별, 흰파빨 색 수 저장
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                WBR[i][0] += 1
            elif arr[i][j] == 'B':
                WBR[i][1] += 1
            else:
                WBR[i][2] += 1
    result = N*M            # 최댓값
    visited = [1, 0, 1]     # 첫줄과 마지막줄은 무조건, 흰색, 빨간색
    # 첫 줄과 마지막줄에 바꿔 넣어야 하는 값 계산
    default = (M - WBR[0][0]) + (M - WBR[N-1][2])
    # 조사 행, 누적 값, 색 종류
    search(1, default, 0)
    print(f'#{tc} {result}')