# 현재 위치에 퀸을 놓아도 되는지 판별하는 함수
def is_vaild_pos(board, row, col):
    # 현재 열에 다른 퀸이 있는지 검사
    for idx in range(row):
        if board[idx][col] == 1:  # 내 인덱스 행에 있는 .. 설명..
            return False

    # 현재 위치의 왼쪽 대각선 위로 퀸이 있는지 검사
    '''
    row = col = 2
    row, col = [2, 1, 0], [2, 1, 0]
    row, col = zip(range(row, -1, -1), range(col, -1, -1))
    (2, 2), (1, 1), (0, 0)
    '''
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 현재 위치의 오른쪽 대각선 위
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    # 모든 검증이 끝났는데 return False가 아니다?
    # 그럼 이 위치에 퀸을 놓을 수 있따!
    return True


def n_queens(row, board):
    # row가 내 모든 행에 대해서 조사를 했다면
    if row == n:
        # 어떠한 일을 하고 종료
        solutions.append([r[:] for r in board])
        return

    # 아직 모든 행에 대해 조사하지 않았다면
    # 모든 열에 대해서 현재 행에 퀸을 놓아 볼 것이다
    for col in range(n):
        # 현재 위치에 퀸을 놓아도 되는지 판별
        if is_vaild_pos(board, row, col):    # True or False
            board[row][col] = 1     # 이번 row, col 위치에 말을 놓음
            n_queens(row + 1, board)    # 다음 조사 보내기
                                        # 근데 row+1 위치에 모든 경로가 다 막혔다면
                                        # 여기로 백트래킹 함
            board[row][col] = 0         # 그럼 원상복귀





n = 4
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트

# n-queens라는 함수를 호출했을 때, 언제까지 조사할 것인가?
# 퀸 4개를 모두 놓았고, 그게 solution이라면, ... 어떠한 일을 할 것이다
    # 그러기 위해서, 퀸을 현재 조사 위치에 놓을 수 있을지도 판별

n_queens(0, board)

for solution in solutions:
    print(solution)
