def bino(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]   
    # n+1, k+1 크기의 이차원 리스트가 필요함
    # n도 변하고, k도 변함
    # 한 행은 전체 k의 개수, 그 행이 n개 있는 것
    '''
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]

    '''
    for i in range(n+1):
        # k는 0부터 n까지 갈 수 있음 (x+y)²일 때 k가 2를 넘지XX
        for j in range(min(i, k) + 1):  
            if j == 0 or i == j:
                # j=0이면 k=0이므로 공집합 => 경우의 수: 1
                # n == k일 때도 항상 1
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp[n][k]

n = 5 
k = 2
print(bino(n, k))  # 출력: 10
