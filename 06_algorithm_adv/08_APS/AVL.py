class Node:
    """AVL 트리의 노드를 나타내는 클래스"""
    def __init__(self, key):
        self.key = key      # 노드의 키 (값)
        self.left = None    # 왼쪽 자식 노드
        self.right = None   # 오른쪽 자식 노드
        self.height = 1     # 노드의 높이 (리프 노드는 1)

class AVLTree:
    """AVL 트리의 연산을 관리하는 클래스"""

    def get_height(self, node):
        """노드의 높이를 반환하는 함수"""
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """노드의 균형 인수(Balance Factor)를 계산하는 함수"""
        if not node:
            return 0
        # 균형 인수 = (왼쪽 서브트리 높이) - (오른쪽 서브트리 높이)
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, z):
        """오른쪽으로 회전 (LL Case)"""
        
        y = z.left
        T3 = y.right

        # 회전 수행
        y.right = z
        z.left = T3

        # 높이 갱신 (높이가 변한 노드부터 갱신)
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # 새로운 루트 노드 반환
        return y

    def rotate_left(self, y):
        """왼쪽으로 회전 (RR Case)"""
        
        z = y.right
        T2 = z.left

        # 회전 수행
        z.left = y
        y.right = T2

        # 높이 갱신
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        # 새로운 루트 노드 반환
        return z

    def insert(self, root, key):
        """노드를 삽입하고 트리의 균형을 맞추는 함수"""
        # 1. 일반적인 BST 삽입 수행
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. 조상 노드의 높이 갱신
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. 균형 인수 계산 및 불균형 확인
        balance = self.get_balance(root)

        # 4. 불균형 상태라면 회전 수행
        # LL Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # RR Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    
    def get_min_value_node(self, node):
        """주어진 서브트리에서 가장 작은 키 값을 가진 노드를 찾는 함수"""
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def delete(self, root, key):
        """노드를 삭제하고 트리의 균형을 맞추는 함수"""
        # 1. 일반적인 BST 삭제 수행
        if not root:
            return root
        
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else: # 삭제할 노드를 찾은 경우
            # 자식이 하나이거나 없는 경우
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            # 자식이 둘인 경우
            # 오른쪽 서브트리에서 가장 작은 노드(in-order successor)를 찾음
            temp = self.get_min_value_node(root.right)
            root.key = temp.key # 후계자의 키로 현재 노드를 덮어씀
            root.right = self.delete(root.right, temp.key) # 후계자 노드를 삭제

        # 트리가 비어있으면 바로 반환
        if root is None:
            return root

        # 2. 높이 갱신
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. 균형 인수 계산
        balance = self.get_balance(root)

        # 4. 불균형 상태라면 회전 수행
        # LL Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        # RR Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        # LR Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        """전위 순회로 트리를 출력하는 함수 (테스트용)"""
        if not root:
            return
        
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


my_tree = AVLTree()
root = None

keys_to_insert = [10, 5, 15, 20, 30, 40, 18, 17]
for key in keys_to_insert:
    root = my_tree.insert(root, key)
    print(f"\n[{key}] 삽입 후 (전위 순회): ", end="")
    my_tree.pre_order(root)

print("\n\n" + "="*30)
print("최종 삽입 결과 (전위 순회): ", end="")
my_tree.pre_order(root)
print("\n" + "="*30)


key_to_delete = 30
root = my_tree.delete(root, key_to_delete)
print(f"\n[{key_to_delete}] 삭제 후 (전위 순회): ", end="")
my_tree.pre_order(root)
print()
