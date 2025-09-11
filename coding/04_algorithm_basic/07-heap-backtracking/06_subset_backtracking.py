def find_subset(start, current_subset, current_sum):
    global cnt  # 함수 실행 횟수 기록
    cnt += 1

    # 가지치기 하나 더 추가
    if current_sum > target_sum:
        return # 더이상 조사할 의미 없음

    # 현재 부분집합의 합이 target_sum과 일치하면 result에 추가
    if current_sum == target_sum:
        # 원본 그대로 넣으면 복제본이 들어가서 곤란하므로
        # 새로운 리스트 만들어서 집어넣기
        # result.append(current_subset[:]) XX
        result.append(list(current_subset))
        return

    # 'start부터' 전체 수를 다 순회
    # 0부터 순회하면 다음 조사하러 갔을 때 이전 조사에서 선택 여부 골랐는데
    # 다시 중복해서 선택하게 되버림(중복조합, 중복순열)
   for idx in range(start, len(nums)):
        num = nums[idx]
        # 현재 선택한 수를 집합에 넣고, 값도 추가해서 다음 작업
        current_subset.append(num)
        find_subset(idx + 1, current_subset, current_sum + num)
        current_subset.pop()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []
cnt = 0

# 필요한 인자들은?
# 1. 재귀를 중단시킬 파라미터 (총합이 10이 되면 종료) -> 기준점
# 2. 누적해서 가야할 파라미터 -> 만들어지는 부분집합
# + 그 선택할 집합의 index 파라미터
find_subset(start=0, current_subset=[], current_sum=0)
