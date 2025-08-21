import sys
sys.stdin = open('input.txt')

def dijkstra():
    dist = [E * 100] * (V + 1)
    visited = [0] * (V + 1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = E * 100

        # 최소값 찾기
        for i in range(V + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        # print(min_idx)
        visited[min_idx] = 1

        # 갱신할수 있으면 갱신
        # print(dist)
        for i in range(V + 1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]
        # print(dist)
    return dist[V]


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 마지막 정점의 번호, E 간선 수

    adj_arr = [[E * 100] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w  # 유향 그래프니까
    # print(adj_arr)
    print(f'#{tc} {dijkstra()}')