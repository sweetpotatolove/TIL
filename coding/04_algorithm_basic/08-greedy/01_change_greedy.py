'''
    거스름돈 문제 그리디로 해결
    가장 큰 거스름돈을 먼저 거슬러주고,
    남은 금액을 다음 단위로 해결
'''
def get_minimum_coins(coins, change):
    # 어떤 동전이: 몇개 사용되었는가?
    result = {}

    # 가장 큰 코인부터 coins에서 빼나갈 것이다 -> 오름차순
    coins.sort(reverse=True)

    # 코인 종류별로 change에서 제거
    for coin in coins:
        count = 0               # 몇 번 뺐는지 알아야 하므로 count 세자
        while change >= coin:   # 뺄 수 있으면
            change -= coin
            count += 1
            result[coin] = count
    return result

coins = [1, 5, 10, 50, 100, 500]  # 동전 종류
change = 882  # 잔돈

# 아래의 경우라면 어떨까?
'''
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈
# 400원짜리가 끼면 그리디로 해결되지 않음
# 빠른 것보다 정확도가 중요!!
# 백트래킹 방식으로 진행해보자
'''
result = get_minimum_coins(coins, change)
for coin, count in result.items():
    print(f"{coin}원: {count}개")
