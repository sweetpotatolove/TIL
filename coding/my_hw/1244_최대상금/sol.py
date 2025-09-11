import sys

sys.stdin = open("input.txt")


def dfs(num_list, count):
    global max_num
    # count가 change가능 횟수에 도달하면 종료
    if count == int(change):
        max_num = max(max_num, int(''.join(num_list)))
        return
    # 내가 저장해야하는 것?
    state = ''.join(num_list)
    if (state, count) not in visited:
        visited.add((state, count))

        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                dfs(num_list, count + 1)
                num_list[i], num_list[j] = num_list[j], num_list[i]


T = int(input())
for test_case in range(1, T + 1):
    numbers, change = input().split()
    num_list = []
    for i in numbers:
        num_list.append(i)
    visited = set()
    max_num = 0
    dfs(num_list, 0)

    print(f'#{test_case} {max_num}')
