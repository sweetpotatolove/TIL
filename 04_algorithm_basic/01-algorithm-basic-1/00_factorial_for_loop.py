# 팩도리얼을 반복문으로 구현
# 3! = 1 * 2 * 3
# 구하고자 하는 값 N
N = 5

# 최종 결과 값
answer = 1      # 초기값을 1로 초기화(곱셈 할거라서)

# 이제 1부터 N까지 answer에 곱해 나갈 수 있도록 순회
for num in range(1, N+1):   # range는 1부터 N-1까지 순회
    # answer = answer * num
    answer *= num
print(answer)   # 출력 120
# 코드 실행은 ctrl + shift + F10
