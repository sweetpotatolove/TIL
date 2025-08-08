import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = 0
    for i in range(N):
        if i <= N//2:
            result += sum(arr[i][N//2-i:N//2+i+1])
        else:
            result += sum(arr[i][N // 2 + i - N + 1:N // 2 - (i - N)])
    print(f'#{tc} {result}')
