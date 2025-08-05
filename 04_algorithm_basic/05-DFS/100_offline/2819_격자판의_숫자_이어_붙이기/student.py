import sys
sys.stdin = open('input.txt')


# dfs 함수 정의
def dfs(x, y, current_num):  # x: row / y: column / current_num: 현재까지 저장된 숫자들
    # global result, direction
    # 현재까지 저장된 숫자의 길이가 7인 경우
    if len(current_num) == 7:
        result.add(current_num)  # set에 추가하고
        return  # 반환

    # 동서남북 탐색
    for (dx, dy) in direction:
        nx, ny = x + dx, y + dy

        # 인덱스 에러 방지 (격자판 내에 존재하는지 확인)
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, current_num + str(grid[nx][ny]))


T = int(input())
for t in range(1, T + 1):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향
    grid = [list(map(int, input().strip().split())) for _ in range(4)]  # 4*4의 격자판 입력 받기
    # 만들 수 있는 서로 다른 일곱 자리 수를 구해야하므로
    result = set()  # 저장된 숫자들을 담을 'set' 선언

    # 4 * 4 격자판의 모든 점에서 확인 (완전탐색)
    for i in range(4):
        for j in range(4):
            dfs(i, j, str(grid[i][j]))

    print(f"#{t} {len(result)}")