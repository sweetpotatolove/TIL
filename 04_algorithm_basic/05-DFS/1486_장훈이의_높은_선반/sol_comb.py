import sys
sys.stdin = open('input.txt')

def combination(arr, r):
    result = []
    if r == 1: # 선택할 요소가 1개만 남은 경우
               # 남아있는 arr의 모든 각 값들을 배열로 만들어서 반환
        return [[i] for i in arr]
    for idx in range(len(arr)):
        elem = arr[idx]
        for rest in combination(arr[idx+1:], r-1):
            result.append([elem] + rest)
    return result

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))

    # 최종 결과값
    # 최솟값을 구하기 위한 초기값은? 충분히 큰 값이어야 함
    min_height = 10000 * N   # 제약사항: N <= 20, h <= 10000

    # 1명부터 N명까지 만들 수 있는 모든 키의 '조합'
    for r in range(1, N+1):
        for comb in combination(data, r):    # 조합을 통해 얻어낸 리스트를 순회
            # 조합에 들어온 모든 점원들의 키를 합친 경우
            total = sum(comb)

            # 최종 조건: 선반보다는 키의 합이 커야 함
            if total >= B:
                # 그 중 가장 작아야 함
                min_height = min(min_height, total)

    # 출력 결과
    print(f'#{tc} {min_height - B}')