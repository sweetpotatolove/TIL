import sys
sys.stdin = open('input.txt')

def find_set(x):
    '''
    재귀호출 최대 횟수 초과로 while로 대체
    '''
    # x가 그룹의 루트가 아니라면,
    while x != parents[x]:
        x = parents[x]  # x를 부모 노드로 업데이트하여 루트를 찾음
    return x  # x가 그룹의 대표자(루트)인 경우 반환


# 두 그룹을 합치는 함수
def union(x, y):
    # y 그룹의 루트를 x 그룹의 루트로 설정하여 두 그룹을 합침
    parents[find_set(y)] = find_set(x)


TC = int(input())

for tc in range(1, TC + 1):
    # N: 노드(주민수)의 개수, M: 간선(서로 아는 관계의 수)
    N, M = map(int, input().split())

    # make_set
    parents = list(range(N + 1))

    for _ in range(M):
        a, b = map(int, input().split())
        if find_set(a) != find_set(b): # 같은 그룹이 아니라면
            union(a, b)  # 두 그룹을 합침


    cnt = 0  # 마을에 존재하는 무리의 갯수 카운트

    # 1부터 N까지의 노드에 대해서 대표자(루트)가 자기 자신인 경우를 찾아 개수를 센다.
    for i in range(1, N + 1):
        if find_set(i) == i:  # 루트 노드의 개수를 센다.
            cnt += 1

    print(f'#{tc} {cnt}')