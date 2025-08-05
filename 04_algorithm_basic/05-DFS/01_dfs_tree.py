# 인접 리스트 사용 이유
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I']
}

# 인접 행렬도 가능. but, 트리 입장에서 인접 리스트가 좀 더 편함

def depth_first_search(node):
    '''
        node: 현재 방문 노드
    '''
    # 내 자식들 순회 전에 내 노드 출력
    print(node)
    # node가 가진 모든 자식들에 대해서 순회하여
    # 동일한 깊이 우선 탐색

    # for next in adj_list[node]: # 대괄호 접근법으로 하면 에러
                                  # 왜? 노드가 없을 때 처리가 안됨
    if node not in adj_list:
        return

    for next in adj_list[node]:
        depth_first_search(next)

depth_first_search('A')