import sys
sys.stdin = open('input.txt')

def make_set(n):
    # 0번 노드 사용하지 않으므로 N+1
    return [i for i in range(N+1)]

def find_set(x):
    # x가 대표자가 아닌경우
    if parent[x] != x:
        # 경로 압축을 적용시키며, 부모 노드 탐색
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    # 대표자를 먼저 찾은 후
    root_x = find_set(x)
    root_y = find_set(y)

    # 대표자가 다른경우, 한쪽으로 대표자 통일
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for tc in range(1, T+1):
    # N: 마지막 원소 번호 (1~N) M: 연산 개수
    N, M = map(int, input().split())
    # 0: 합집합 연산
    # 1: 집합 포함여부 확인 연산
    data = [list(map(int, input().split())) for _ in range(M)]

    # 최종 출력값: 모든 1연산의 결과를 한 줄의 문자열로 표현
    # a, b가 속해있으면 1, 아니면 0
    parent = make_set(N)
    result = ''
    for item in data:
        # 연산자, 집합 a, b
        oper, x, y = item
        if oper == 0:
            union(x, y)
        else:
            root_x = find_set(x)
            root_y = find_set(y)
            # 같은 집합이면 1, 아니면 0
            if root_x == root_y:
                result += '1'
            else:
                result += '0'
    print(f'#{tc} {result}')