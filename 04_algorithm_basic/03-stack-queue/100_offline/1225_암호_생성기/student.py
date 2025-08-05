import sys
sys.stdin = open("input.txt", "r")


for _ in range(1, 11):
    # 1.입력
    tc = int(input())
    data_list = list(map(int, input().split()))

    # 2.동작 알고리즘
    cycle = 0
    while True:
        data = data_list.pop(0) - (cycle % 5 + 1)
        if data <= 0: data = 0
        data_list.append(data)
        cycle += 1

        # 만약 0보다 작으면 암호 도출
        if data == 0:
            break

    # 3.출력
    print(f"#{tc}", *data_list)