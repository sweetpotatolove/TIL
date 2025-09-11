import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start_index):
    visited = set()
    queue = deque()
    queue.append([start_index])
    visited.add(start_index)
    last_level = []  # 같은 레벨의 최대값 구해야함

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node)  # 같은 레벨 노드들 기록

            # 모든 노드 조사
            for next_index in range(1, 101):
                # 방문하지 않았고, 1이면 드가자
                if next_index not in visited and adj_matrix[node][next_index]:
                    queue.append(next_index)
                    visited.add(next_index)
        last_level.append(level)

    return max(last_level[-1])

for test_case in range(1, 11):
    length, start = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_matrix = [[0] * 101 for _ in range(101)]    # 0번 인덱스 안쓸거임
    for i in range(length//2):
        from_index, to_index = edges[i * 2], edges[i * 2 + 1]
        adj_matrix[from_index][to_index] = 1
        # adj_matrix[to_index][from_index] = 1 양방향 아님!!!

    print(f'#{test_case} {bfs(start)}')


