def hanoi(n, source, auxiliary, target):
    """
    n개의 원반을 source 기둥에서 target 기둥으로 옮깁니다.

    Args:
        n (int): 이동할 원반의 개수
        source (str): 시작 기둥 (예: 'A')
        auxiliary (str): 보조 기둥 (예: 'B')
        target (str): 목표 기둥 (예: 'C')
    """
    # 일단, 옮겨야 할 원판의 수가 1개보단 많아야 일을 함
    if n > 0:
        # 1단계: 가장 큰 원반을 옮기기 위한 준비
        # n-1개의 원반들을 모두 옮겨야 한다 -> 보조 기둥으로
        hanoi(n-1, source, target, auxiliary)

        # 2단계: 목표였던 가장 큰 원반을 옮긴다
        print(f'원반 {n}을 {source}에서 {target}으로 이동하였음')

        # 3단계: 마무리 작업
        # 가장 큰 원반을 옮기는 데 성공했으니
        # 우리는 이제 보조 기둥(각각의 원반 기준으로 보조기둥)에서
        # 다시 target 기둥으로 옮겨야 한다.
        hanoi(n-1, auxiliary, source, target)
# --- 실행 예시 ---
# 3개의 원반을 'A' 기둥에서 'C' 기둥으로 옮기기 ('B' 기둥을 보조로 사용)
number_of_disks = 3
hanoi(number_of_disks, 'A', 'B', 'C')