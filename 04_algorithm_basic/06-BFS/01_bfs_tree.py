def BFS(root_node):
    '''

    :param root_node: 너비우선 탐색을 시작할 서브 트리의 루트
    :return: 완성된 경로
    '''
    result = []     # 탐색 경로를 저장할 리스트(바로 print 안하고 append)

    # 이번에 조사할 노드와 앞으로 조사할 노드들(후보군)을 담을 자료구조
    data_structure = [root_node]    # 처음 시작 노드 넣어놓기

    # 탐색이라는 행위는 언제까지 할 것이냐?
    # 모든 노드를 다 탐색해서 더 이상 탐색할 후보군이 없을 때까지!
    while data_structure:   # 후보군이 남아있으면 계속 조사
        # node = data_structure.pop()     # LIFO 해버려서 DFS가 됨
        node = data_structure.pop(0)    # FIFO
        result.append(node)
        # 내 자식 노드들(인접 노드들)을 찾아와서
        for child in graph.get(node, []):   # 디폴트 값 [] 설정
                                            # 찾는 키가 없으면 빈 리스트 반환
            # 다음 조사 후보군 목록에 자식을 추가함
            data_structure.append(child)

    return result


# 그래프 인접 리스트
graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H', 'I'], 
    'E': [],
    'F': [],
    'G': []
}

start_node = 'A'
print(BFS('A'))