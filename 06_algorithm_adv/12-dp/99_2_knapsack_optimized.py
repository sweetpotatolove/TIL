def knapsack_optimized(weights, values, capacity):
    # 1차원 DP 테이블 초기화
    # dp[w]는 현재 용량 w에서의 최대 가치를 저장
    dp = [0] * (capacity + 1)

    # 물건들을 하나씩 순회
    for i in range(len(weights)):
        # 용량 w를 capacity부터 1까지 역순으로 순회
        for w in range(capacity, weights[i] - 1, -1):
            # 현재 물건을 담는 경우와 담지 않는 경우 중 더 큰 가치를 선택
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]


# 예시
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack_optimized(weights, values, capacity)
print(f"최적화된 배낭 문제의 최대 가치: {max_value}")