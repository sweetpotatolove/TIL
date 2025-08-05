import sys
sys.stdin = open('input.txt')

class TreeNode:
    def __init__(self, index, value=0):
        self.index = index
        self.value = value
        self.left = None
        self.right = None
        # self.parent = None

class BinaryTree:
    def __init__(self, N):
        self.N = N
        # 1번 노드를 기본으로 하는 이진트리 구성    {1: <object Node>, 2: <object Node> ... }
        self.nodes = {i: TreeNode(i) for i in range(1, N + 1)}

        # 완전 이진트리 구조 설정 (부모-자식 연결)
        for i in range(1, N // 2 + 1):  # 부모 노드 탐색
            if 2 * i <= N:
                self.nodes[i].left = self.nodes[2 * i]
            if 2 * i + 1 <= N:
                self.nodes[i].right = self.nodes[2 * i + 1]

    def add_leaf(self, index, value):
        if index in self.nodes:
            self.nodes[index].value = value

    def build_tree(self, node):
        # 양쪽 모두 자식이 없는 리프노드
        if not node or (node.left is None and node.right is None):
            return node.value  # 자기 값을 반환

        # 초기에 초기화 했던 값들 0 or 본래의 왼쪽 자식의 값
        left_val = self.build_tree(node.left) if node.left else 0
        right_val = self.build_tree(node.right) if node.right else 0
        # 내 값은 나의 왼쪽과 오른쪽 자식들의 값.
        node.value = left_val + right_val
        return node.value

    # index가 주어지면 nodes 정보에서 해당 노드의 값을 반환
    def get_value(self, index):
        return self.nodes[index].value if index in self.nodes else 0

# 입력 및 실행
T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # 전체 노드의 크기 만큼 트리 구성
    tree = BinaryTree(N)

    for _ in range(M):
        idx, value = map(int, input().split())
        tree.add_leaf(idx, value)

    tree.build_tree(tree.nodes[1])  # 루트 노드(1)부터 전체 트리 계산
    print(f'#{tc} {tree.get_value(L)}')
