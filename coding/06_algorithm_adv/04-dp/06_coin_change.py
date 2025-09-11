def coin_change(coins, amount):
    # 이전에는 이곳의 값을 0으로 초기 화
    # 충분히 큰 값
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[amount]

coins = [1, 4, 6]  # 사용 가능한 동전의 종류
amount = 8  # 만들어야 할 금액

print(coin_change(coins, amount))
