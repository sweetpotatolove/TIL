import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    n, a, b = map(int, input().split())

    dp = [[0 for _ in range(b+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i, b) + 1):
            if j == i or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    print(f'#{test_case} {dp[n][b]}')