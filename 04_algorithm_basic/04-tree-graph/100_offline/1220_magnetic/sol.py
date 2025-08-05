import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    # 1은 N극 2는 S극
    data = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for x in range(100):
        stack = 0
        for y in range(100):
            if data[y][x] == 1:
                stack = 1
            elif data[y][x] == 2 and stack:
                stack = 0
                result += 1
    print(result)
