import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    # DP 테이블 초기화 (13개월까지 고려, 0번 인덱스는 사용하지 않음)
    dp = [0] * 13

    for month in range(1, 13):
        # 1일 이용권으로만 사용할 경우의 비용
        daily_cost = prices[0] * plans[month - 1]

        # 1달 이용권 사용 비용
        monthly_cost = prices[1]

        if month <= 2:
            # 1, 2월의 경우 1일 또는 1달 이용권 중 저렴한 것 선택
            dp[month] = dp[month - 1] + min(daily_cost, monthly_cost)
        else:
            # 3달 이용권 고려
            quart_cost = prices[2]

            # 이번 달에 1일 또는 1달 이용권 사용
            cost_without_quart = dp[month - 1] + min(daily_cost, monthly_cost)

            # 3달 전부터 3달 이용권 사용
            cost_with_quarterly = dp[month - 3] + quart_cost

            # 두 경우 중 저렴한 것 선택
            dp[month] = min(cost_without_quart, cost_with_quarterly)

    # 1년 이용권과 비교하여 최종 결과 반환
    result = min(dp[12], prices[3])
    print(f"#{tc} {result}")
