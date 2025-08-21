import sys
sys.stdin = open('input.txt')
T = int(input())

for test_case in range(1, T+1):
    r = int(input())
    list_color = []
    for _ in range(r):
        list_color.append(list(map(int, input().strip().split())))
    
    color = [[0]*10 for x in range(10)]
    for c in list_color:
        for x in range(c[0], c[2]+1):
            for y in range(c[1], c[3]+1):
                if c[-1] == 1: # 빨강
                    color[x][y] += 1
                if c[-1] == 2: # 파랑
                    color[x][y] += 100
    
    # print(color)
    count = 0
    for i in range(10):
        for j in range(10):
            if color[i][j] == 0:
                continue
            if (color[i][j]//100) > 0 and (color[i][j]%10) > 0:
                count += 1
    
    print(f'{test_case} {count}')

