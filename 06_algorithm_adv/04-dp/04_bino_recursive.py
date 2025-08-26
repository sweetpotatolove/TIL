def bino(n, k):
    if k == 0 or k == n:
        return 1    
    return bino(n-1, k-1) + bino(n-1, k)

n = 5
k = 2
print(bino(n, k))  # 출력: 10
