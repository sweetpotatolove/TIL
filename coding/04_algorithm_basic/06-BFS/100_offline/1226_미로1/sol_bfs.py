import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def escape(x, y):
    start_point = [(x, y)]
    while start_point:
        # stack 말고 queue로 하려면?
        # stack과 queue의 차이는? LIFO냐, FIFO이냐 밖에 없으니까?
            # 그래서 stack을 쓰냐 queue를 쓰냐에 따라서 DFS냐, BFS냐 이기 때문에.
        x, y = start_point.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if data[nx][ny] != 1:
                if data[nx][ny] == 3:
                    return 1
                data[x][y] = 1
                start_point.append((nx, ny))
    return 0

for _ in range(10):
    test_case = int(input())
    data = []
    for _ in range(16):
        data.append(list(map(int, input())))
    result = False
    for x in range(16):
        for y in range(16):
            if data[x][y] == 2:
                result = escape(x, y)
                break
        if result:
            break
    print(f'#{test_case} {result}')







