def knapsack(weights, values, capacity):
    n = len(weights)  # 물건의 개수
    # DP 테이블 초기화: (n+1) x (capacity+1) 크기의 2차원 리스트를 0으로 초기화
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # DP 테이블 채우기
    for i in range(1, n + 1):  # 1부터 n까지
        for w in range(1, capacity + 1):  # 1부터 capacity까지
            if weights[i - 1] > w:  # 현재 물건을 담을 수 없는 경우
                K[i][w] = K[i - 1][w]  # 이전 물건까지의 최대 가치를 그대로 가져옴
            else:  # 현재 물건을 담을 수 있는 경우
                # 현재 물건을 담는 경우와 담지 않는 경우 중 최대 가치를 선택
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])

    return K[n][capacity]  # 최대 담을 수 있는 가치 반환


weights = [10, 20, 30]  # 각 물건의 무게
values = [60, 100, 120]  # 각 물건의 가치
capacity = 50  # 배낭의 용량

max_value = knapsack(weights, values, capacity)
print(f"배낭에 담을 수 있는 물건들의 최대 가치: {max_value}")
