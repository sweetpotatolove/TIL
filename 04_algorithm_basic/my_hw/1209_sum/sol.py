import sys
sys.stdin = open('input.txt')
# open 사용해서 input 파일 연다

# 이 문제는 10개의 TC를 가진다
for _ in range(10):
    tc = input() # 테스트케이스 번호 입력
    # 100 X 100을 2차원 리스트로 받아야 함
    # 즉, 한번 입력 받은 한 줄에 100개의 숫자가 공백을 기준으로 문자열로 오게 됨
        # 이걸 100번 반복
    data = []   # 2차원 배열 만들기 위한 리스트
    for _ in range(100):
        data.append(list(map(int, input().split()))) # 공백 기준으로 쪼개서 리스트로 만들자

    # data = [list(map(int, input().split())) for _ in range(100)]




    cross_sum = [0]*2
    row = []
    column = [0]*100
    for i in range(100):
        row_sum = 0
        for j in range(100):
            if i == j:
                cross_sum[0] += data[i][j]
            if (i + j) == 99:
                cross_sum[1] += data[i][j]
            row_sum += data[i][j]
            column[j] += data[i][j]
        row.append(row_sum)

    row_max = row[0]
    column_max = column[0]
    cross_max = cross_sum[0]
    if cross_sum[0] < cross_sum[1]:
        cross_max = cross_sum[1]

    for r in row:
        if row_max < r:
            row_max = r
    for c in column:
        if column_max < c:
            column_max = c

    total = [row_max, column_max, cross_max]
    total_max = total[0]

    for t in total:
        if total_max < t:
            total_max = t

    print(f'#{tc} {total_max}')
