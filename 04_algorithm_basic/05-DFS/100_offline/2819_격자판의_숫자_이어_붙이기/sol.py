import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#  x, y: 좌표
#  depth: 현재까지 진행한 패턴의 길이
#  code: 현재까지의 경로를 나타내는 문자열
def search(x, y, depth, pattern):
    # depth가 7 ==  7자리 숫자 완성 이를 pattern(set)에 추가
    if depth == 7:
        pattern_set.add(pattern)
    else:
        for k in range(4):      # 4방향 전수 조사
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= ny < 4 and 0 <= nx < 4: # 범위를 벗어나지 않는다면
                # 다음 위치로 이동, 현재까지 패턴을 인자로 넘겨 재귀 호출
                search(nx, ny, depth + 1, pattern + data[nx][ny])

T = int(input())
for tc in range(1, T + 1):
    # 문제 조건은 4x4 배열만 존재
    data = [list(map(str, input().split())) for _ in range(4)]

    # 중복은 없어야 하므로 Set 초기화
    pattern_set = set()

    # 4×4 크기의 격자판
    # 모든 배열 위치에서 시작하여 가능한 모든 경로를 탐색
    for x in range(4):
        for y in range(4):
            search(x, y, 0, '')  # 시작 길이와 초기 패턴은 빈 문자열

    print(f'#{tc} {len(pattern_set)}')