# 완전 이진 트리 기준 순회

# 전위 순회
def preorder_traversal(idx):
    # 어디까지 순회해야 하는지?
    # 순회 대상이 범위를 벗어나지 않았다면
    if idx <= N:    # 완전 이진 트리이므로 내가 조사해야 하는 노드 개수는 N개(뒤에 더 없음)
        # 전위 순회는 부모 노드를 먼저 조사
        print(tree[idx], end=' ')
        # 이제 왼쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2)
        # 이제 오른쪽 서브 트리에 대해서도 동일한 조건
        preorder_traversal(idx * 2 + 1)


# 중위 순회
def inorder_traversal(idx):
    # 중위순회란, 부모 노드 차례가 중간인 순회 방식
    # 즉, 왼쪽 서브 트리에 대한 처리가 우선되어야 함

    # 전위 순회 코드에서 순서만 바꾸면 됨
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2)
        # 중위 순회는 왼쪽 서브트리 순회 후 조사
        print(tree[idx], end=' ')
        # 오른쪽 서브 트리에 대해서도 동일한 조건
        inorder_traversal(idx * 2 + 1)


# 후위 순회
def postorder_traversal(idx):
    if idx <= N:
        # 왼쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2)
        # 오른쪽 서브 트리에 대해서도 동일한 조건
        postorder_traversal(idx * 2 + 1)
        # 후위 순회는 모든 서브트리 순회 후 조사
        print(tree[idx], end=' ')


N = 5
tree = [0, 'A', 'B', 'C', 'D', 'E']


'''
    트리 구조
        'A'
      /   \
   'B'    'C'
  /   \
'D'    'E'
'''
# 위 트리를 '완전 이진 트리'라고 부를 수 있음

print('전위 순회')
preorder_traversal(1)  # 'A' 'B' 'D' 'E' 'C'
# 트리를 결국 배열 형태로 만들 것이고
# 그 인덱스를 각 노드의 값이 삽입된 위치로 볼 것이기 때문에
# 루트 노드에 해당하는 1번 인덱스부터 조회를 시작할 것임

print()
print('중위 순회')
inorder_traversal(1)  # 'D' 'B' 'E' 'A' 'C'
print()
print('후위 순회')
postorder_traversal(1)  # 'D' 'E' 'B' 'C''A'