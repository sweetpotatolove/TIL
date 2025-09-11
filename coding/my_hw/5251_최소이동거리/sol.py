import sys
sys.stdin = open('sample_input.txt')

import math, heapq
T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    edges = {}
    for _ in range(E):
        edge, k, v = map(int, input().split())
        edges[edge][k] = v
    print(edges)

    distances = {v: math.inf for v in range(N+1)}
    distances[0] = 0    # 시작 정점 0

    heap = []
    heapq.heappush(heap, [0, 0])

    visited = set()
    #
    # while heap:
    #     dist, current = heapq.heappop(heap)
    #     if current in visited or distances[current] < dist:
    #         continue
    #     visited.add(current)
    #
    #     for next, weight in edges[current].items():
    #         next_distance = dist + weight
    #         if next_distance < distances[next]:
    #             distances[next] = next_distance
    #             heapq.heappush(heap, [next_distance, next])
    #
    # print(distances)
