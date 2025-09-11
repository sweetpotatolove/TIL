import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def mix_number(row, col, num):

    if len(num) == 7:
        numbers.add(num)
        return
    
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            mix_number(nx, ny, num + matrix[nx][ny])

T = int(input())
for test_case in range(1, T+1):
    matrix = [list(map(str, input().strip().split())) for _ in range(4)]
    numbers = set()

    for x in range(4):
        for y in range(4):
            mix_number(x, y, matrix[x][y])
    
    print(f'#{test_case} {len(numbers)}')
    