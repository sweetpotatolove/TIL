def combinations(arr, r, current_comb, start_idx):
    # 종료 조건
    if len(current_comb) == r:  # 내가 만든 조합의 길이가 r개가 되었다
        print(current_comb)
        return
    # 아직 더 모아야 한다
    for idx in range(start_idx, len(arr)):
        # 그 idx 번째를 선택
        current_comb.append(arr[idx])
        # 다음 요소 선택하러 조합 재귀 떠남
        combinations(arr, r, current_comb, idx+1)
        # 그렇게 선택한 개수가 r개가 되어 조합을 출력하고 나면,
        # 돌아와서는 마지막으로 선택한 요소를 취소하고, 다른 요소를 선택할 수 있게 해야 함
        current_comb.pop()


# 사용 예시
my_list = [1, 2, 3, 4]
r = 3 # 3개의 요소를 선택하는 조합

# 함수를 호출할 때는 초기 상태를 전달
# 빈 리스트 []는 현재 선택된 요소가 없음을 의미
# 0은 arr의 첫 번째 인덱스부터 탐색을 시작함을 의미
combinations(my_list, r, [], 0)