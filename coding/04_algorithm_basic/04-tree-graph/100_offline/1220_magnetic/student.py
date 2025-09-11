import sys

sys.stdin = open('input (1).txt')

for t in range(10):
    side = int(input()) # 정사각형 테이블의 한 변의 길이(100)
    data = [list(map(int,input().split())) for _ in range(100)] # 정사각형(100X100) 테이블 데이터
    ans = 0 # 교착 상태 개수

    for i in range(100): # 인덱스 0부터 99까지 순회하는 i
        stack = [] # N극(1)이 나오면 넣어 놓을 stack
        for row in data: # 정사각형 테이블의 행 하나하나 순회
            if row[i] == 1:
                stack.append(row[i])

            elif (row[i] == 2) and stack: # S극(2)이 나오고, stack이 비어있지 않은(N극이 들어있는) 상태라면
                ans += 1 # 교착 상태 개수 +1
                stack = [] # stack 초기화

    print(f"#{t+1} {ans}")