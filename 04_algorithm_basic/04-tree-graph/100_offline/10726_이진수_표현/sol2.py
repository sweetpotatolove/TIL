import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # print(type(bin(M)))
    # print(bin(M)[2:])
    # print(bin(M)[2:][-N:])
    if all(list(map(int, bin(M)[2:][-N:]))):
        print('ON')
    else:
        print('OFF')