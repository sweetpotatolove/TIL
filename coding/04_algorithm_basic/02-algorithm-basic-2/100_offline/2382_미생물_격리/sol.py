import sys
sys.stdin = open('input.txt')

x = [0, -1, 1, 0, 0]  # 상 하 좌 우
y = [0, 0, 0, -1, 1]  # 문제에서 상 하 좌 우의 값이 1,2,3,4 이므로 앞에 0을 넣어서 맞춰줌

T = int(input())  # 테스트 케이스 수
for tc in range(1, 1 + T):
    n, m, k = map(int, input().split())  # n*n, m 몇 번 움직이는지, k 움직일 갯수

    board = [list(map(int, input().split())) for _ in range(k)]
    # x, y, 미생물, 방향
    for q in range(m):
        cnt = -1
        # board에서 값을 꺼낼 때마다 +1 해줄 것이고
        # 시작점은 0이기 때문에 초기 cnt 값은 -1로 지정
        # cnt는 숫자가 합쳐질 경우, 이 전 값의 위치를 파악하기 위해 필요

        visited = [[0] * n for _ in range(n)]
        # 한 번에 모든 값들이 움직이는 것이 아니라
        # 순서대로 움직이기 때문에 초기화 시켜주지 않으면
        # 오류 발생 가능

        for w in board:
            cnt += 1
            if w[2] > 0:  # 미생물이 0이면 움직일 필요 없음
                nx = w[0] + x[w[3]]
                ny = w[1] + y[w[3]]
                # 범위를 넘어서는 값을 줄리 없기 때문에
                # 범위에 대한 조건은 고민하지 않아도 됨

                if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                    # 미생물 군집이 약물에 도착한 경우
                    w[2] = w[2] // 2  # 절반을 줄이고

                    if w[3] == 1 or w[3] == 3:  # 방향 바꾸기
                        w[3] += 1
                    else:
                        w[3] -= 1

                else:  # 그 외의 경우
                    if visited[nx][ny] == 0:  # 이 전에 해당 위치로 온 값이 없으면
                        visited[nx][ny] = [w[2], w[2], cnt]
                        # 해당 위치에 값을 넣어 주기
                        # 총 미생물, 현재 최대 값, cnt 값

                    else:  # 이미 visited 위치에 온 값이 있으면(군집을 더해야하는 경우)
                        if visited[nx][ny][1] > w[2]:
                            # 기존 최대 값이 현재의 값보다 큰 경우
                            visited[nx][ny][0] += w[2]
                            # 총 미생물에 현재의 값 더하기
                            board[visited[nx][ny][2]][2] = visited[nx][ny][0]
                            # board에 있는 최대값을 변화시키기
                            # 다음번 for문을 돌 때에는 합쳐지 값으로 돌아야하기 때문
                            w[2] = 0
                            # 현재 도착한 값을 0으로 만들어서 더 이상 고려하지 않게 만들기

                        else:  # 현재의 값이 기존의 최대 값보다 큰 경우
                            visited[nx][ny][0] += w[2]
                            # 총 미생물에 현재의 값 더하기
                            visited[nx][ny][1] = w[2]
                            # 기존 최대 값을 현재의 값으로 대체하기
                            board[visited[nx][ny][2]][2] = 0
                            # board에 있었던 기존 값을 0으로 만들어서 더 이상 고려하지 않게 만들기
                            visited[nx][ny][2] = cnt
                            # cnt를 현재 값으로 바꾸기
                            w[2] = visited[nx][ny][0]
                            # board에 있는 현재의 값을 총 미생물의 합으로 바꾸기

                w[0] = nx
                w[1] = ny
            # x,y 좌표 변경
    num_sum = 0
    for e in board:
        num_sum += e[2]  # 남아있는 미생물들 더하기

    print(f'#{tc} {num_sum}')
