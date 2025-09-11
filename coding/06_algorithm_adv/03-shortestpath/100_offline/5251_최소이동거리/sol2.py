import sys
sys.stdin = open('input.txt')


import heapq

def dijkstra():
    # 거리 최대치로 초기화
    distances = [float('inf')] * (N + 1)
    # 방문 정보 초기화
    visited = set()
    heap = []
    # 누적 거리, 시작 정점
    heapq.heappush(heap, (0, 0))
    distances[0] = 0    # 시작 정점 0으로 초기화

    while heap:
        weight, current = heapq.heappop(heap)
        # 이미 방문한 적 있다면 조사 취소
        if current in visited: continue
        # 현재 정점 방문 처리
        visited.add(0)
        # 현재 정점의 인접 정점들에 대해
        for next, next_weight in graph[current].items():
            acc = weight + next_weight  # 누적값 계산후
            if acc < distances[next]:   # 갱신 가능시
                distances[next] = acc
                # 다음 후보군에 삽입
                heapq.heappush(heap, (acc, next))
    return distances
T = int(input())

for tc in range(1, T + 1):
    # N: 마지막 정점의 번호, E 간선 수
    # 주의 N이 마지막 정점의 `번호`임
    N, E = map(int, input().split())
    # start, end, weight
    data = [list(map(int, input().split())) for _ in range(E)]
    # 0번 노드부터 N + 1 노드까지의 인접 노드 정보를 인접 리스트로 표기
    graph = {v: {} for v in range(N + 1)}
    for s, e, w in data:    # 인접 정보 갱신
        graph[s][e] = w
    result = dijkstra()
    print(f'#{tc} {result[N]}')



