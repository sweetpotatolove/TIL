import sys
sys.stdin = open('sample_input.txt')
T = int(input())

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    ux, uy = find_set(x), find_set(y)
    if ux != uy:
        p[uy] = ux

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    p = [i for i in range(V+1)]
    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))

    edges.sort(key=lambda x: x[2])
    #print(p)
    #print(edges)
    total, cnt = 0, 0
    for edge in edges:
        start, end, w = edge
        if find_set(start) != find_set(end):
            union(start, end)
            total += w
            cnt += 1
            if cnt == V:
                break

    print(f'#{test_case} {total}')