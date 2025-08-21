import sys
sys.stdin = open('input.txt')

def dfs(row, now_percent):

    global max_percent, visited

    # 확률은 곱할수록 작아짐
    if now_percent <= max_percent:
        return

    if row == N:
        if max_percent < now_percent:
            max_percent = now_percent
        return
    
    for col in range(N):
        if visited[col] == False:
        # 해당 일을 선택한적 없었을 때 방문표시하고 다음 사람으로 넘어감
            visited[col] = True 
            dfs(row + 1, now_percent * P[row][col])
            visited[col] = False
        
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [[element / 100 for element in row] for row in P]

    visited = [False] * N
    max_percent = 0
    dfs(0, 1)

    print(f'#{test_case} {max_percent * 100:.6f}')
