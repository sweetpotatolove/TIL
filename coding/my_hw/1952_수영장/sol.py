import sys
sys.stdin = open('input.txt')
T = int(input())
for test_case in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    day_one_month = [0, 0]
    year = cost[3]  # 1년 단위
    for i in plan:
        if cost[0] * i <= cost[1]:  # 1일 단위가 1달 금액보다 작으면
            day_one_month.append(cost[0] * i)
        else:
            day_one_month.append(cost[1])
    day_one_month += [0, 0]

    # 3달
    three_month = [0] * (12 + 4) # 앞에 2칸 뒤에 2칸
    for month in range(2, 14): # 0 ~ 11 -> 1 ~ 12월
        three_month[month] = min(day_one_month[month] +
                                 day_one_month[month+1] +
                                 day_one_month[month+2], cost[2])
    #print(day_one_month)
    #print(three_month)

    # total: 각 월까지의 누적 최소 요금
    '''
    total = [0] * len(day_one_month)
    for month in range(2, 14):  # 1월(index 2)~12월(index 13)
        # 이번 달을 1달 단위로 결제하는 경우
        # total은 누적값이니까
        # 직전 total + 이번달 값
        one_or_month = total[month-1] + day_one_month[month]

        # 이번 달부터 3달 단위로 결제하는 경우
        # ex. 5월이라 가정했을 경우
            # 3,4,5월 3개월치랑 2월까지 누적값
        three_month_pass = total[month-3] + three_month[month-2]  # 시작 월 맞춰줌
        # 최소값 선택
        total[month] = min(one_or_month, three_month_pass)

    answer = min(total[13], year)
    print(f'#{test_case} {answer}')
    '''
    total = [0] * len(day_one_month)
    for month in range(2, 14):  # 1월(index 2) ~ 12월(index 13)
        # 이번 달을 개별(1일/1달 최소)로 결제
        one_or_month = total[month - 1] + day_one_month[month]

        # 이번 달에 '끝나는' 3달권 선택 (month >= 4일 때만 가능)
        if month >= 4:
            three_month_pass = total[month - 3] + three_month[month - 2]
        else:
            three_month_pass = float('inf')

        total[month] = min(one_or_month, three_month_pass)

    answer = min(total[13], year)
    print(f'#{test_case} {answer}')
