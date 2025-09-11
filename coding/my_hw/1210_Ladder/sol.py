import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    data = []
    for _ in range(100):
        data.append(list(map(int, input().strip().split())))
    
    for start_col in range(100):
        if data[0][start_col] == 0: # 시작지점이 1이 아니면 고려XX
            continue

        temp = [row[:] for row in data]     
        # 내가 갔던 경로면 0으로 바꿀건데
        # 원본 오염 시키니까 시작 지점 바뀌었을 때 문제 생김
        # 복사해서 사용하자

        row = 0
        col = start_col
        while row < 100:

            if temp[row][col] == 2:
                print(f'#{test_case} {start_col}')
                break

            temp[row][col] = 0  # 방문 표시

            moved = False
            for j in [-1, 1]:  # 좌, 우 살펴보기
                new_col = col + j
                if 0 <= new_col < 100 and temp[row][new_col] in (1, 2):
                    while 0 <= new_col < 100 and temp[row][new_col] in (1, 2):
                        col = new_col
                        if temp[row][col] == 2:
                            print(f'#{test_case} {start_col}')
                            break
                        temp[row][col] = 0  # 방문 표시
                        new_col += j
                    moved = True
                    break

            if not moved:
                row += 1    # 좌우 이동 못했으면 아래로 내려가기

'''
for test_case in range(1, 11):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if data[99][i] == 2:
            row, col = 99, i
            break

    while row > 0:
        # 왼쪽으로 계속 이동
        if col > 0 and data[row][col - 1] == 1:
            while col > 0 and data[row][col - 1] == 1:
                col -= 1
        # 오른쪽으로 계속 이동
        elif col < 99 and data[row][col + 1] == 1:
            while col < 99 and data[row][col + 1] == 1:
                col += 1
        # 위로 한 칸
        row -= 1

    print(f'#{test_case} {col}')
'''