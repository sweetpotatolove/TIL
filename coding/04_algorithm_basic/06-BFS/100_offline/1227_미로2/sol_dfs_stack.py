# bfs 방식으로 풀기.
import sys

sys.stdin = open('input.txt')


def search(x, y):
    # queue -> stack으로 바꿈. 외 변동사항 없음.
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if data[nx][ny] != 1:
                if data[nx][ny] == 3:
                    return 1  # 도착 성공했음을 반환.

                data[nx][ny] = 1  # 왔던길 전부 벽으로 만들어버림
                stack.append((nx, ny))

    return 0  # 아, 모든 경우에도 도착점 못갔구나.


for _ in range(10):
    tc = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    result = 0
    for x in range(100):
        for y in range(100):
            if data[x][y] == 2:
                result = search(x, y)
                break
        if result:
            break
    print(result)