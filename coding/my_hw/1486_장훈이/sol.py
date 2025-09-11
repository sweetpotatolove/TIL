import sys
sys.stdin = open('input.txt')

def dfs(idx, now_top):

    global min_top

    # 가지치기
    # 이미 최소 탑보다 현재 탑 크기가 커지면 끝
    if min_top < now_top:
        return

    
    # 모든 직원을 처리했으면
    if idx == N:
        # 탑 크기보다 직원 높이 커지면 stop
        if now_top >= B:
            min_top = min(now_top, min_top)
        return
    
    # 다음 직원들 더하기    
    dfs(idx + 1, now_top + people[idx])
    
    # 현재 직원 안더하고 넘어가기
    dfs(idx + 1, now_top)
    


T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    people = list(map(int, input().strip().split()))
    min_top = 10000 * N
    dfs(0, 0)
    print(f'#{test_case} {min_top - B}')