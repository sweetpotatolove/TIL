def bellman_ford(graph, start):
    n = len(graph)  # 정점의 수 
    # 모든 노드에 도달하는데 걸리는 거리 무한대로 초기화
    distances = {v: float('inf') for v in graph}
    print(distances)
    # 시작 정점 거리 0 초기화
    distances[start] = 0
    # 마지막 정점을 제외한 횟수만큼 순회
    for _ in range(n - 1):
        updated = False # 이번 회차에 갱신여부 확인용
        # 각 정점별 인접 정점 순회
        for u in graph:
            for v, weight in graph[u].items():
                # 시작 정점 u에 도달하는 거리 + 다음 정점 가중치
                # 해당 정보가 도착 정점까지 걸리는 최소거리보다 작아야
                # 단, 시작정점 u가 무한대면 안된다.  -> 아직 도달 불능
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight    # 갱신
                    updated = True
        # 이번 회차에 전체 노드에 대한 조사를 했음에도 갱신이 없다?
        if updated == False:
            break
    # 음수 사이클 검사
    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                # 어? 조사 이미 끝났는데 왜 또 갱신 해야 하는 상황나옴?
                print('음수 사이클이 있습니다.')
                return False
    return distances

# 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': 3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# 음수 사이클 예시 그래프
graph = {
    'a': {'b': 4, 'c': 2},
    'b': {'c': -3, 'd': 2, 'e': 3},
    'c': {'b': 1, 'd': 4, 'e': 5},
    'd': {'e': -3},
    'e': {'f': 2},
    'f': {}
}

# 시작 정점 설정
start_vertex = 'a'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
