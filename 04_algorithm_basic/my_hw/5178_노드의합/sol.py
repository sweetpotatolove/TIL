import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T+1):
    n, m, l = map(int, input().strip().split())
    tree = [0] * (n+1)
    for _ in range(m):
        location, num = map(int, input().split())
        tree[location] += num
    
    for i in range(n, 0, -1):
        if tree[i] > 0:
            tree[i // 2] += tree[i]
    
    print(f'#{test_case} {tree[l]}')
    