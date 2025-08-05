def DFS(now):
    '''
    now: 현재 방문한 정점 정보
    '''
    # 방문 대상 후보군들을 stack에 삽입해서 관리
    stack = []
    visited.add(now)    # 현재 지점 방문
    stack.append(now)

    # 순회: 언제까지? stack이 빌 때까지
    while stack:
        # 이번 방문 대상을 알아내야 함
        target = stack.pop()
        print(target)   # LIFO 방문

        # 이번 방문 대상의 인접 리스트 순회
        for next in graph[target]:
            # 그 대상(target: A 일 때, next = B, C) 을 방문한 적 없다면
            if next not in visited:
                visited.add(next) # 방문처리는 위에서 프린트 하는데 왜 visited 처리를 여기서 하나?
                                  # 한번 방문한 곳 다시 방문하지 않으려고 visited 씀
                                  # 내 후보군들 스택에 다 넣고난 '후'에
                                  #
                # 방문 표시를 싯ㄹ제방문한 시점에 한다면
                #
                stack.append(next)


# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C']
}

start_vertex = 'A'
visited = set()     # 방문한 정점을 저장할 집합
                    # 왜 집합?
                    # 정점이 가진 정보 자체가 방문 여부를 확인하는 집합에 포함되어 있는지 확인
DFS(start_vertex)