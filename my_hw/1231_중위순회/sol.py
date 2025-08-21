import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    n = int(input())
    tree = [None] * (n+1)
    for i in range(1, n+1):
        tree[i] = list(input().strip().split())[1]
    # print(tree)
    def in_order(tree, index=1):
        if index >= len(tree) or tree[index] is None:
            return
        
        # 왼쪽 방문
        in_order(tree, 2 * index)

        # 현재 노드
        print(tree[index], end='')

        # 오른쪽 방문
        in_order(tree, 2 * index + 1)
    
    print(f'#{test_case}', end=' ')
    in_order(tree)
    print()
    
