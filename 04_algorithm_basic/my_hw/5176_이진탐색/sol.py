import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    
    count = [1]     # 리스트는 함수 내에서 변경 가능하므로 사용
                    # 또는 전역 변수 사용할 수 있을듯?

    def order(i):
        if i > n:
            return
        order(i*2)      # 왼
        tree[i] = count[0] # 현 노드에 숫자 저장
        count[0] += 1  
        order(i*2 +1)   # 오

    order(1)
    print(f'#{test_case} {tree[1]} {tree[n//2]}')

