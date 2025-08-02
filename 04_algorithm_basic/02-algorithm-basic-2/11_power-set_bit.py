arr = [1, 2, 3]
n = len(arr)
subset = []

# 모든 경우의 수에 대해서 조회
# for idx in range(2**n): 또는
for idx in range(1 << n):   # 1을 n번 shift한 정수 8을 기준으로 순회
    tmp_subset = []     # 이번 경우의 수의 부분집합
    for j in range(n):  # j번째 요소가 이번 경우의 수에 사용되었는지 판별
        '''
        idx = 0  => 000
        j = 0    => 001  &연산 -> 0

        idx = 3  => 011
        j = 0    => 001  &연산 -> True
        j = 1    => 010  &연산 -> True
        '''
        # 1을 j번 shift 연산한 것과 idx를 &연산
        if idx & (1 << j):
            tmp_subset.append(arr[j])
            # true라면 j번째 요소가 이번 경우의 수에 사용되었다는 것이므로
            # tmp_subset에 넣음
    
    # 필요하다면 추가 조건 달 수 있음
    # 부분집합의 합이 3인 부분집합만 넣기
    if sum(tmp_subset) == 3:
        subset.append(tmp_subset)
print(subset)


