import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1):
    # N: 노드의 개수
    # CC(i): i노드로 도달하는 모든 노드들의 최단 경로의 합
        # 즉 CC(2): 4의 의미는
        # 1~5번 노드들 에서 2번 노드로 도달하는 최단경로들의 합이 4라는 뜻.

    # 간선 정보
        # 단, 자기 자신으로 돌아가는 간선 없음.
    # 노드의 개수 N, 이후 한 줄로 N개의 값이 N번 반복
    N, *input_line = list(map(int, input().split()))
    max_value = float('inf')
    # 인접 행렬 초기화
    adj_matrix = []
    for row in range(N):
        adj_matrix.append(input_line[row*3:row*3+N])
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if not adj_matrix[i][j]:
                adj_matrix[i][j] = max_value

    print(f"#{tc} {input_line}")