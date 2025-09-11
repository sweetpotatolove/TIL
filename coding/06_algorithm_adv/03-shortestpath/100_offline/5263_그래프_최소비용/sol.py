import sys
sys.stdin = open('input.txt')

def flowyd_washall():
    global result
    for k_node in range(N):
        for start in range(N):
            for end in range(N):
                # 경유지가 무한대가 아니면,
                # 직진과 경유지중, 짧은 거기로 가중치 갱신
                if data[start][k_node] != max_value and data[k_node][end] != max_value:
                    data[start][end] = min(data[start][end], data[start][k_node] + data[k_node][end])

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수 N
    N = int(input())
    # 모든 노드에 대한 인접 행렬 정보
    # 단, 처음 주어지는 정보는 도달 불능지역이 0으로 되어있음.
    # 도달 불능 지역은 0이 아닌 충분히 큰 값으러 전처리 하여야 함.
    # 음수 가중치로 인해, 도중에 0이 되는 경우도 있기 때문
    data = [list(map(int, input().split())) for _ in range(N)]
    max_value = float('inf')

    for i in range(N):
        for j in range(N):
            if i == j: continue # 자기 자신은 0 유지
            if data[i][j] == 0:
                data[i][j] = max_value

    result = -max_value  # 음수 가중치가 있으므로 음수 무한대
    flowyd_washall()

    # 모든 조사 종료 후, result 갱신
    for i in range(N):
        for j in range(N):
            result = max(result, data[i][j])

    print(f'#{tc} {result}')

