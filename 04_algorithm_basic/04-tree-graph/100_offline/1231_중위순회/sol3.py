import sys
sys.stdin = open('input.txt')

class TreeNode:
    # 넘겨받은 데이터를 unpacking 단, left와 right가 없는 경우 None으로 처리
    def __init__(self, parent, value, left=None, right=None):
        self.parent = parent        # 부모 정보
        self.value = value          # 내 값
        # 아래는 각각 left, right 정보가 있다면 해당 정보를 토대로 새로운 노드 생성하여 할당
        # 단, left 정보가 실제 data의 index와 일치하지 않으므로 각각 -1
        self.left = TreeNode(*data[left-1]) if left else None
        self.right = TreeNode(*data[right-1]) if right else None


def inorder(node):
    # 노드 정보가 None이 아닐때만 조사
    if node:
        inorder(node.left)     # 왼쪽
        print(node.value, end='')
        inorder(node.right)     # 오른쪽

for tc in range(1, 11):
    N = int(input())
    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    # data 기반 트리 구성 (data의 값을 unpacking 하여 전달)
    # data의 0번째 요소가 항상 root 노드
    root = TreeNode(*data[0])
    print(f'#{tc}', end=' ')
    inorder(root)
    print()