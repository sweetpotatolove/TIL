def fibo(n):
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0:
        # memo[n] = memo[n-1] + memo[n-2]
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [0] * (101)  # 0부터 100까지 들어갈 배열 생성

# f(100)을 얻기 위해서는 f(99), f(98)을 얻을 수 있어야 하듯
# 기저 조건을 미리 넣어줘야 함(초기값 넣기)
memo[0] = 0
memo[1] = 1

cnt = 0
result = fibo(100)
print(result)
print(cnt)