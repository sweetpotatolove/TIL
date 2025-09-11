import sys
sys.stdin = open('input.txt')


def solve():
    dist = [[float('inf')] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                dist[i][j] = 1
        dist[i][i] = 0

    # 플로이드-워셜 알고리즘
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_network_index = float('inf')

    # 각 정점의 네트워크 지수 계산
    for i in range(N):
        network_index = 0
        for j in range(N):
            network_index += dist[i][j]
        min_network_index = min(min_network_index, network_index)
    
    return min_network_index


T = int(input())
for tc in range(1, T + 1):
    input_line = list(map(int, input().split()))
    N = input_line[0]
    graph = []
    for i in range(N):
        graph.append(input_line[1 + i*N : 1 + (i+1)*N])

    result = solve()
    print(f"#{tc} {result}")