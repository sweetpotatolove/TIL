import sys
sys.stdin = open('input.txt')

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # 정렬된 값들
    def __init__(self, sorted_values):
        # 주어진 정렬된 값들으로 BST를 만들어서 반환된 node를 루트로 잡을 것.
        self.root = self._build_balanced_bst(sorted_values)

    def _build_balanced_bst(self, values):
        if not values:
            return None
        # 정렬된 값들을 가지고, bst 구성할때 핵심은 중앙값
        mid = len(values) // 2  # 그 중앙에 위치판 값으로 node 생성
        node = TreeNode(values[mid])
        # 나의 왼쪽은? 내 값보다 작은 애들로만 이루어진 내용
        node.left = self._build_balanced_bst(values[:mid])
        node.right = self._build_balanced_bst(values[mid+1:])
        return node


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bst = BinarySearchTree(range(1, N+1))

    # 만약 정렬이 안되어 있다.
    # a = [1, 8, 23, 9, 34, 82, 6, 98, 2]
    # python은 a.sort() 하면 됩니다.
    # b = sorted(a) 하면 됩니다.

