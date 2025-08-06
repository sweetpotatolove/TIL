from collections import deque
def BFS(start_vertax):
    # 해당 정점 방문 여부 표시할 배열 필요함
    # visited = [0] * len(nodes)
    # 또는
    visited = set()

    # 후보군 저장
    # deque는 첫번째 인자로  iterable 객체를 받음
    queue = deque([start_vertax]) # 그냥 넣지말고 리스트로 만들어서 넣자

    # 조사 시작할 때 시작정점 넣어주기
    visited.add(start_vertax)

    # 최종 결괏값
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 내 인접 리스트에서 인접 정점 찾아서 순회
        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한 적 없다면
            if neighbor not in visited:
                visited.add(neighbor)   # 방문 예정 표시
                queue.append(neighbor)  # 다음 후보군에 추가
    return result

def BFS2(start_index):
    visited = set()
    queue = deque([start_index])
    visited.add(start_index)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 모든 노드들에 대해 인덱스 조사
        for next_index in range(len(nodes)):
            # ??
            if next_index not in visited and adj_matrix[node][next_index]:
                visited.add(next_index)
                queue.append(next_index)
    return result
# --------------------------------------------

# 정점 정보
#         0    1    2    3    4    5    6
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 간선 정보
edges = [
    '0 1',  # A - B 무방향 그래프
    '0 2',  # A - C 무방향 그래프
    '1 3',  # B - D
    '1 4',  # B - E
    '2 4',  # C - E
    '3 5',  # D - F
    '4 5',  # E - F
    '5 6'   # F - G
]

# -------------------------------------------------
# 간선 정보를 보기 쉬운 인접 리스트 형태로 만들어보자
adj_list = {        # dict comprehension
    node: [] for node in nodes
   # key: value
}

# 간선 정보와 정점의 index 정보로 adj_list 채워주기
for edge in edges:
    u, v = edge.split()     # 시작 정점, 도착 정점
    # print(f'{u}: {nodes[int(u)]}, {v}: {nodes[int(v)]})

    adj_list[nodes[int(u)]].append(nodes[int(v)])
    # 현재 간선 정보는 '무방향' 그래프
    # -> 양쪽 다 갈 수 있다는 뜻
    # 반대방향도 넣어주자
    adj_list[nodes[int(v)]].append(nodes[int(u)])
# 인접 리스트 완성
# print(adj_list)

print(BFS('A'))
# --------------------------------------------------

# 인접 행렬 -> [[], [], [], ...]
adj_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
            # 모든 정점에 못간다고 가정해두고
            # 갈 수 있는 정점을 1로 변경하자(아니면 나중에 0 다 채워야함)

for edge in edges:
    u, v = edge.split()
    u_index, v_index = int(u), int(v)
    adj_matrix[u_index][v_index] = 1
    adj_matrix[v_index][u_index] = 1    # 무방향이므로 반대쪽도 해주기

print(BFS2(0))