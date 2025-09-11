import sys
sys.stdin = open("input.txt")

# 중위 순회 함수
def inorder_traversal(idx):
    # 순회 대상이 범위를 벗어나지 않았다면
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리 순회 후에 조사한다.
        print(tree[idx], end='') # 붙여서 출력하기 위해 end=''
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)

for t in range(1, 11): # 테스트 케이스 10개
    N = int(input())
    tree = [None] * (N+1) # 트리 미리 생성

    # N값에 따른 자식 개수 별 정점 개수
    child0_cnt = (N//2) + (N%2)
    child1_cnt = ((N%2) + 1) % 2
    child2_cnt = N - child0_cnt - child1_cnt

    # 자식 개수가 2개인 정점
    for _ in range(child2_cnt):
        # node_val이 문자열 이므로 우선 전부 문자열로 받고
        node_num, node_val, child1_num, child2_num = input().split()
        # 숫자만 int형으로 변환
        node_num, child1_num, child2_num = map(int, [node_num, child1_num, child2_num])
        # tree에 value 기입
        tree[node_num] = node_val

    # 자식 개수가 1개인 정점
    for _ in range(child1_cnt):
        node_num, node_val, child1_num = input().split()
        node_num, child1_num = map(int, [node_num, child1_num]) # 문자열이 아닌 변수 int 적용
        tree[node_num] = node_val

    # 자식 개수가 0개인 정점
    for _ in range(child0_cnt):
        node_num, node_val = input().split()
        node_num = int(node_num) # 문자열이 아닌 변수에 int 적용
        tree[node_num] = node_val

    print(f"#{t}", end=' ')
    inorder_traversal(1)
    print() # 다음 테스트 케이스 가기 전에 줄바꿈