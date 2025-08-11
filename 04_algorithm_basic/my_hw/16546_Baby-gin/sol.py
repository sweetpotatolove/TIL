import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    cards = input().strip()

    check = [0] * 10
    for i in cards:
        check[int(i)] += 1
    
    count = 0
    for j in range(len(check)):
        while check[j] >= 3:
            count += 1
            check[j] -= 3
        
        if j <= 7:
            while check[j] >= 1 and check[j+1] >= 1 and check[j+2] >= 1:
                check[j] -= 1
                check[j+1] -= 1
                check[j+2] -= 1
                count += 1
    
    result = 'false'
    if count == 2:
        result = 'true'
    
    print(f'#{test_case} {result}')

