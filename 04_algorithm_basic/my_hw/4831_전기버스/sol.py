import sys
sys.stdin = open('input.txt')
# open 사용해서 input 파일 연다

T = int(input())
for test_case in range(1, T+1):
    k, n, m = map(int, input().strip().split())      # k: 최대이동 n: 정류장개수 m: 충전소개수
    m_num = list(map(int, input().strip().split()))  # m_num: 충전소 위치
    count = 0   # 충전 횟수
    now = 0     # 현재 위치

    while now + k < n:
        check = []
        for move in range(now+1, now+k+1):
            if move in m_num:
                check.append(move)  # 만약 최대 이동거리 이내에 충전소가 여러개 있다면
                                    # 충전소 위치 리스트업

        if len(check) == 0:         # 만약 최대 이동거리 내에 충전소가 없다면 리스트가 비어있을 것
            count = 0               # 리스트가 비어있으면 앞에 충전했던 횟수 초기화하고
            break                   # 넘어감
        else:
            now = check[-1]     # 가장 마지막 충전소 위치로(최소 충전 횟수 구해야하니까)
            count += 1

    print(f'#{test_case} {count}')





