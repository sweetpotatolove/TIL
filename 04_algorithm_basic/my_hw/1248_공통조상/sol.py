import sys
sys.stdin = open('input.txt')

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def build_tree(edges):
    global nodes
    nodes = {1: TreeNode(1)}

    for i in range(0, len(edges), 2):
        p, c = edges[i], edges[i+1]

        if p not in nodes:
            nodes[p] = TreeNode(p)
        if c not in nodes:
            nodes[c] = TreeNode(c)
        
        parent = nodes[p]
        child = nodes[c]

        if parent.left is None:
            parent.left = child
        else:
            parent.right = child
        
        child.parent = parent
    
    return nodes[1]

def count_subtree(node):
    if node is None:
        return 0
    left_cnt = count_subtree(node.left)
    right_cnt = count_subtree(node.right)
    return 1 + left_cnt + right_cnt     # 부모 + 왼쪽 + 오른쪽

T = int(input())
for test_case in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    edges = list(map(int, input().strip().split()))

    root = build_tree(edges)
    
    parents1 = []
    node = nodes[num1]
    parents1.append(node.data)
    while node.parent:
        node = node.parent
        parents1.append(node.data)
    
    parents2 = [num2]
    node = nodes[num2]
    parents2.append(node.data)
    while node.parent:  # 부모 있을 때까지
        node = node.parent
        parents2.append(node.data)

    result = []
    for j in parents1:
        if j in parents2:
            result.append(j)
    
    print(f'#{test_case} {result[0]} {count_subtree(nodes[result[0]])}')
    
