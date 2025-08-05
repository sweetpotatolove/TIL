import sys
sys.stdin = open('input.txt')

def inorder(node):
    node = int(node)
    if node:
        inorder(data[node][2])
        print(data[node][1], end='')
        inorder(data[node][3])


for tc in range(1, 11):
    result = 0
    N = int(input())
    data = [input().split() for _ in range(N)]
    print(data)
    data.insert(0, None)
    print(data)
    for idx in range(1, N+1):
        while len(data[idx]) < 4:
            data[idx].append('0')
    print(data)
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
