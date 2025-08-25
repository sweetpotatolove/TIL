def fibo(N):
    if N <= 1:      # 0이거나 1이면 return
        return N
    
    # 함수 내에서 저장할 공간을 생성
    dp = [0] * (N+1)
    dp[1] = 1   # 0번째는 0이니 1번째만 1로 초기화

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

result = fibo(100)
print(result)