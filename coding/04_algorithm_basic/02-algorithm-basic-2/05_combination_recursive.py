def comb(arr, n):
   # 최종 결과값
   result = []
   if n == 1: # 선택할 요소의 수가 1인 경우
      # n이 1이라면 더 이상 조합할 요소가 필요 없어짐
      # 각 요소 자체가 하나의 조합이 됨
      return [[i] for i in arr] #[[1], [2], [3], [4]] 이런식으로 반환

   # 배열의 모든 요소를 일단 순회
   for idx in range(len(arr)):
      # 요소 하나를 선택
      select_item = arr[idx]
      # 현재 선택한 그 요소 이후의 나머지 요소들
      # 즉, n-1개의 요소들로 조합을 재귀로 다시 구성
      for rest in comb(arr[idx+1:], n-1):
         # 순회 가능한 어떤 요소에서 반복을 할 것이다
         # 그럼 저 함수의 호출 결과 값을 알아야함
         # 그걸 알기 위해 반복문?
         result.append([select_item] + rest) #rest = [[4]]
      return result


print(comb([1, 2, 3, 4], 3))  # [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] 출력
