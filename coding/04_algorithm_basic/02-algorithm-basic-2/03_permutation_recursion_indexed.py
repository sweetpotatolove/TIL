def perm_no_slice(arr, start_idx):
    '''
    Args:
        arr: 순열을 만들 원본 리스트 (여기서는 변경 가능)
        start_idx: 현재 순열을 만들고 있는 시작 인덱스
    '''
    ''' nPn
    # 시작해야 하는 인덱스가 내가 선택해야하는 요소 개수만큼이 되었다
    # 즉, 시작해야 하는 인덱스가 마지막 번호가 되었다
    if start_idx == len(arr):
        print(arr)
        return
    # 재귀호출
    for idx in range(start_idx, len(arr)):
        # start_idx번째와 idx번째의 값을 swap
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        print(f'스왑된 배열 상태: {arr}')
        print(f'이번에 선택한 요소: {arr[start_idx]}')
        print(f'위치가 바뀐 요소: {arr[idx]}')
        perm_no_slice(arr, start_idx + 1)
        # 어질러놓은거 되돌려놔야함(다음 반복문 실행 전까지)
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        print('===재귀 호출 후 돌아온 시점 ===')
        print(f'복원된 배열 상태: {arr}')
    '''
    # nPr이 하고싶다. 즉, 앞에 r개 까지만 보고싶다
    # 시작해야 하는 인덱스가 내가 선택해야하는 요수 만큼이 되었다
    # 즉, 시작해야 하는 인덱스가 마지막 번호가 되었다
    if start_idx == 2:
        print(arr[:2])

    if start_idx == len(arr):
        #print(arr)
        return
    # 재귀호출
    for idx in range(start_idx, len(arr)):
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]
        perm_no_slice(arr, start_idx + 1)
        arr[start_idx], arr[idx] = arr[idx], arr[start_idx]

# 사용 예시
my_list = [1, 2, 3]
perm_no_slice(my_list, 0)