import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(input().strip())
    
    code = {'0001101' : 0,
            '0011001' : 1,
            '0010011' : 2,
            '0111101' : 3,
            '0100011' : 4,
            '0110001' : 5,
            '0101111' : 6,
            '0111011' : 7,
            '0110111' : 8,
            '0001011' : 9}
    
    total = []
    for row in matrix:
        if '1' not in row:   # 1이 없으면 넘어감
            continue

        for col in range(M-1, 0, -1):     # 뒤에서 1찾기
            if row[col] == '1':
                end = col
                break
        
        for number in range(end-55, end + 1, 7):
            total.append(code[f'{row[number:number+7]}'])
    
        break
    
    total_sum = 0
    for i in range(0, 8):
        if i % 2 == 0:
            total_sum += (total[i] * 3)
        else:
            total_sum += total[i]
    
    if total_sum % 10 == 0:
        print(f'#{test_case} {sum(total)}')
    else:
        print(f'#{test_case} {0}')
    
    
