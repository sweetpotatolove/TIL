import sys
sys.stdin = open('input.txt')


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())

for tc in range(1, T+1):
    # N: 학생 번호 (1~N), M: 신청서 수
    N, M = map(int, input().split())
    # 신청 정보 [from, to, from, to]
    data = list(map(int, input().split()))

    '''
        간선수가 2일 때, 간선 정보가 선형 데이터로 넘겨 받게 되면
        range(M) ->  0 에 대해서 2개 1에 대해서 2개
                   0 1 2 3
        1 - 2   -> 1 2 3 4
        3 - 4
    '''
    '''
    # 트리 형태를 만들어서 -> 집합으로 처리 할 것.
        # 두 노드의 대표자가 동일한지 확인하고
        # 이미 대표자가 동일하면... 그냥 무시
        # 두 노드의 집합의 대표자가 다르다면, 하나의 집합으로 합치기. (union)
    # 대표자가 누군지 먼저 설정
    # 기본적으로 단독으로 조를 구성 할 수 있다. -> 최악의 경우, 각 노드가 서로 완전히 배타적인 집단들이 N개 만큼 만들어 질 수도 있다.
        # 자기 자신이 대표자인 상태
    # make_set
    '''
    # 0번노드 사용하지 않고, 자신을 루트로 잡는 N+1개의 리스트
    parent = [i for i in range(N+1)]

    for idx in range(0, M*2, 2):    # 2명씩 잘라서
        from_child = data[idx]
        to_child = data[idx+1]
        union(from_child, to_child)

    # 모든 작업을 마쳤으면 경로 압축
    for i in range(1, N+1):
        find_set(i)

    # 최종 생성된 조의 개수
    # 집합의 개수 (0번을 제외하기 위해 -1)
    print(f'#{tc} {len(set(parent)) - 1}')


