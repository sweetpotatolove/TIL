def fibonacci_for_loop(n):
    # 기본 룰은 동일하게 적용해야 함
    # n이 0이면 0을 반환함
    if n == 0:
        return 0
    # n이 1이면 1을 반환함
    elif n == 1:
        return 1
    # n이 2 이상인 경우
    else:
        # 내 이전의 두 항의 값이 무엇인지 알 수 있어야 함
        # 이 else문에 올 수 있는 가장 적은 수 2를 기준으로 생각해보자
        first, second = 0, 1    # f(i-1), f(i-2)의 역할을 해 줄 것
        # 2부터 n까지도 위의 규칙과 동일한 규칙이 실행되어야 함
        # 2부터 n까지 모두 순회할건데,
            # 피보나치 규칙 상, 사실 그렇게 순회해서 얻어내는
            # 2, 3, 4, ..., n까지 있는 수는 필요 없음
        # 그러므로, 임시변수는 _로 처리
        for _ in range(2, n+1):
            # 다음 피보나치 수는 이전 두 항의 합을 사용함
            next_fib = first + second
            # 기존의 first는 쓸모 없어지고,
            # 기존의 second가 first가 되어야 함
            # 또한, 다음 피보나치 수가 second가 되어야 함
            first = second
            second = next_fib
            # first, second = second, next_fib 파이썬은 이렇게 작성 가능
        # 만약 위의 순회에서, 더 이상 다음 연산을 할 작업이 없다면
        # next_fib == second이다.
        return second
# 사용 예시
print(fibonacci_for_loop(10)) # 55