import sys
sys.stdin = open('input.txt')

class TreeNode:
    def __init__(self, index, value, left=None, right=None):
        self.index = index
        self.value = value
        self.left = TreeNode(*data[left-1]) if left else None
        self.right = TreeNode(*data[right - 1]) if right else None

def postorder(node):
    global expression
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=' ')
        expression.append(node.value)

def calc(expression):
    stack = []
    for char in expression:
        if type(char) == int: stack.append(char)
        else:
            y = stack.pop()
            x = stack.pop()
            if char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
            elif char == '*':
                stack.append(x * y)
            elif char == '/':
                stack.append(x // y)
    return stack[0]

for tc in range(1, 11):
    N = int(input())
    data = [list(map(lambda x: int(x) if x.isnumeric() else x, input().split())) for _ in range(N)]
    print(data)
    root = TreeNode(*data[0])
    print(root)
    print(root.index)
    print(root.value)
    print(root.left.left)
    print(root.right.right)
    expression = []
    postorder(root)
    print(f'#{tc} {calc(expression)}')