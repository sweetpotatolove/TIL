import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(T):
    # N: 총 노드 수, M: 리프 노드 수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 노드 값을 저장할 리스트
    tree = [0] * (N + 1)

    # 리프 노드의 값을 입력 받아 트리에 저장
    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    # 트리의 마지막 노드부터 역순으로 부모 노드에 값을 더해줌
    for i in range(N, 0, -1):

        # 부모 노드가 존재할 때만 처리
        if i // 2 > 0:
            tree[i // 2] += tree[i]  # 부모 노드에 현재 노드 값을 더함

    # L번 노드의 값을 출력
    print(f'#{test_case + 1} {tree[L]}')