import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N: 노드의 개수, M: 리프 노드의 개수, L: 출력 할 노드번호
    N, M, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    # 0번 노드 사용하지 않음 + N 개의 노드 만큼 저장할 트리
    # 완전 이진트리이므로 순서대로 삽입하면 된다.
    tree = [0] * (N + 2)        # 단, 리프가 아닌 노드가 자식 정보가 없을 수 있으므로 충분히 크게 만든다.
    # 정보 순회하며 tree에 리프노드 정보 삽입
    for idx, value in data:
        tree[idx] = value

    # 전체 노드의 개수 N == 마지막 노드의 index 번호
    # 따라서 N을 조사 대상의 index로 사용할 예정
    # 조사 대상 index가 L보다 큰 동안
    while N >= L:
        parent = N // 2 # 부모 인덱스
        # 부모의 값은    왼쪽 자식       +  오른쪽 자식
        tree[parent] = tree[parent * 2] + tree[parent * 2 + 1]
        # 조사 대상을 2칸씩 건너뛰면서 조사 (어차피 부모 노드의 양쪽 자식 값을 더해서 계산할 것이므로)
        N -= 2
    # print(tree, L, tree[L])
    print(f'#{tc} {tree[L]}')
