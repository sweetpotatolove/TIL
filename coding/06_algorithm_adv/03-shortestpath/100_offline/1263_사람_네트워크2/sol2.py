import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start_node, N, graph):
    distances = [-1] * N
    distances[start_node] = 0
    q = deque([start_node])
    
    while q:
        u = q.popleft()
        for v in range(N):
            if graph[u][v] == 1 and distances[v] == -1:
                distances[v] = distances[u] + 1
                q.append(v)
    
    return sum(distances)

def solve():
    N = input_line[0]
    graph = []
    for i in range(N):
        graph.append(input_line[1 + i*N : 1 + (i+1)*N])

    min_network_index = float('inf')

    for i in range(N):
        network_index = bfs(i, N, graph)
        min_network_index = min(min_network_index, network_index)
    
    return min_network_index

T = int(input())
for tc in range(1, T + 1):
    input_line = list(map(int, input().split()))
    result = solve()
    print(f"#{tc} {result}")