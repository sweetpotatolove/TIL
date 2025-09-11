import sys
sys.stdin = open('input.txt')

from collections import defaultdict


def dfs(start_num):
    visited[start_num] = True

    for v in graph[start_num]:
        if not visited[v]:
            dfs(v)


T = int(input())
for test_case in range(1, T + 1):
    # 마을에 사는 사람 수, 관계 수
    # vertex 수, edge 수
    N, M = map(int, input().split())
    # 서로 알고 있는 관계 입력 받기
    # 인접 리스트 형태로 관리 ( 인접 행렬이던, 어떤 방식이든 상관없음)
    graph = defaultdict(list)
    # graph = {}

    group_cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        # 아래와 같이 하면 에러가 남..
        # 왜냐면 주어지지 않은 정점이 있을 때
        # 해당 정점에 접근하려고 할 때 문제가 생김
        # if a not in graph: graph[a] = []
        # if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    # 각 정점에 대해서 방문 여부를 확인할 리스트 추가
    # 숫자가 1부터 시작하기 때문에, N+1까지 할당
    visited = [False] * (N + 1)
    # 모든 정점에서 DFS 실행
    # 이미 방문한 정점은 스킵될 거고, 결국 DFS가 실행되는 횟수가 곧 마을이 나눠진 수
    for i in range(1, N + 1):  # 모든 정점에 대해서 DFS 실행
        if not visited[i]:  # 이미 방문한 정점은 DFS로 인해 하나의 그룹으로 묶인 상황이므로, BFS 진행 X
            dfs(i)
            group_cnt += 1  # DFS가 진행될 때마다 마을의 무리가 하나씩 생성
    print(f"#{test_case} {group_cnt}")
