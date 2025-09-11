import sys
sys.stdin = open('input.txt')

def combination(arr, r):
    result = []

    if r == 1:  # 선택할 요소가 1개만 남은 경우
        # 남아 있는 arr의 모든 각 값들을 배열로 만들어서 반환
        return [[i] for i in arr]
    for idx in range(len(arr)):
        elem = arr[idx]
        for rest in combination(arr[idx + 1:], r - 1):
            result.append([elem] + rest)
    return result

T = int(input())        # 10
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    # tc 수
    # 최종 결괏값 # 최솟값을 구하기 위한 초기값?
    # min_height = 'inf'   # 충분히 큰 값
    # 직원당 최대 키 10000 * 최대 직원수 20
    min_height = 10000 * N
    # 1명부터 N명까지 만들수 있는 모든 키의 조합
    for r in range(1, N+1):
        # 조합을 통해 얻어낸 리스트를 순회해서
        for comb in combination(data, r):
            # 조합에 들어온 모든 점원들의 키를 합한 경우
            total = sum(comb)

            # 최종 조건: 선반보다는 키의 합이 커야한다.
            if total >= B:
                # 근데, 그 중에서 제일 작아야한다.
                min_height = min(min_height, total)
    # 출력 결과
    print(f'#{tc} {min_height - B}')