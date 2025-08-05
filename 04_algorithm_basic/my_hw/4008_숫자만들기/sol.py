import sys
sys.stdin = open('input.txt')

def dfs(now, result, o_list, num):
    if now >= len(num):
        return result_list.append(result)
    if o_list[0] > 0:
        o_list[0] -= 1
        dfs(now+1,result + num[now], o_list, num )
        o_list[0] += 1
    if o_list[1] > 0:
        o_list[1] -= 1
        dfs(now+1,result - num[now], o_list, num )
        o_list[1] += 1
    if o_list[2] > 0:
        o_list[2] -= 1
        dfs(now+1,result * num[now], o_list, num )
        o_list[2] += 1
    if o_list[3] > 0:
        o_list[3] -= 1
        if result < 0:
            dfs(now+1, -(-result//num[now]), o_list, num)
        else:
            dfs(now+1,result // num[now], o_list, num )
        o_list[3] += 1


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    o_list = list(map(int, input().split()))
    numbers = list(map(int,  input().split()))
    
    result_list = []
    dfs(1, numbers[0], o_list, numbers)
    print(f'#{test_case} {max(result_list) - min(result_list)}')

