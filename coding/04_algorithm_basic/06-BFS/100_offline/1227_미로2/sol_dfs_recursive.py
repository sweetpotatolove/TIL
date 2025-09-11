# sol_dfs_recursive
# bfs 방식으로 풀기.
import sys
sys.stdin = open('input.txt')

'''
    이거 뭐임?
    파이썬은 재귀함수를 기본적으로 1000번 스택에 쌓이면 멈추게 함.
    RecursionError: maximum recursion depth exceeded in comparison
    최대 재귀 가능 횟수 바꿀 수 있음.
'''
# sys.setrecursionlimit(100000)
def search(x, y):
    global result, cnt
    cnt += 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy# SWEA 1226 미로 1 문제 풀이

def bfs(start, end):
    """
    BFS(너비 우선 탐색)를 사용하여 시작점에서 끝점까지의 경로가 존재하는지 확인

    Args:
        start: 시작점 좌표 (x, y)
        end: 도착점 좌표 (x, y)

    Returns:
        bool: 경로가 존재하면 True, 없으면 False
    """
    queue = [start]  # BFS를 위한 큐, 시작점으로 초기화
    visited = set()  # 방문한 노드를 저장하는 집합

    while queue:  # 큐가 비어있지 않은 동안 반복
        current = queue.pop(0)  # 큐의 첫 번째 요소를 꺼내어 현재 위치로 설정

        if current == end:  # 현재 위치가 목표점이면
            return True  # 경로를 찾았으므로 True 반환

        if current not in visited:  # 현재 위치를 아직 방문하지 않았다면
            visited.add(current)  # 현재 위치를 방문 처리

            # 현재 위치의 모든 이웃 노드를 확인
            for neighbor in get_neighbors(current):
                if neighbor not in visited:  # 이웃 노드가 방문되지 않았다면
                    queue.append(neighbor)  # 큐에 추가하여 나중에 탐색

    return False  # 모든 탐색이 끝났는데 목표점에 도달하지 못했으면 False

def get_neighbors(pos):
    """
    주어진 위치의 상하좌우 이웃 위치들 중 이동 가능한 위치들을 반환

    Args:
        pos: 현재 위치 (x, y)

    Returns:
        list: 이동 가능한 이웃 위치들의 리스트
    """
    x, y = pos  # 현재 위치 좌표 분리
    neighbors = []  # 이웃 위치들을 저장할 리스트

    # 상하좌우 네 방향으로 이동할 수 있는 방향 벡터
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상, 하, 좌, 우
        nx, ny = x + dx, y + dy  # 새로운 위치 계산

        # 새로운 위치가 미로 범위 내에 있고, 벽('1')이 아닌 경우
        if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != '1':
            neighbors.append((nx, ny))  # 이동 가능한 위치로 추가

    return neighbors

# 미로 데이터 입력 (16x16 크기의 미로)
maze = [list(input().strip()) for _ in range(16)]

# 시작점과 끝점 설정 (문제에서 주어진 좌표)
start = (1, 1)    # 시작점 좌표
end = (14, 14)    # 도착점 좌표

# BFS 탐색 실행하여 경로 존재 여부 확인
if bfs(start, end):
    print(1)  # 도달 가능하면 1 출력
else:
    print(0)  # 도달 불가능하면 0 출력 (이 부분이 누락되어 있었음)
        # if x == 7:
        #     print(f'지금{x}, 방향: {dx} ')
        #     print(f'지금{y}, 방향: {dy} ')
        #     print(data[nx][ny])
        #     print('='*30)
        # 모든 모서리 1로 둘러쌓여 있어서, 범위 벗어날 일 없다.
        # 1. 다음 위치가 벽이 아니면
        if data[nx][ny] != 1:
            # print() # 이러저러해서이렇게 되었다.
            if data[nx][ny] == 3:   # 도착지면
                result = 1          # 전역변수 변경
                return 1
                # return 1            # 도착했다는 정보 반환
            data[nx][ny] = 1
            # 도착을 했든 못했든 반환받은 0과 1 그냥 버리네?
            search(nx, ny)
            # if check: return 1
            '''
                그렇다고 반환 받은 값을 그대로 return 하게 만들면?
                도착 못해서 0 반환 받은것도 그대로 return 하곘네...? 
                return search(nx, ny)
                재귀 함수 호출 받은 결과로 return 하는 상황은
                돌아온 시점에서 바로 종료 해야 하는 특별한 상황
                혹은, 재귀 함수 호출 결과 값으로 연산하여서 재 호출해야하는상황
                    -> fibonacci or factorial 
            '''
    # 여기서 0을 반환하는게 맞아?
    # return 0

for _ in range(1):
    tc = int(input())
    cnt = 0
    data = [list(map(int, input())) for _ in range(100)]
    result = 0
    for x in range(16):
        for y in range(16):
            if data[x][y] == 2:  # 출발지
                search(x, y)  # 해당 위치에서 출발
                break
        if result:
            break
    print(cnt)
    print(result)