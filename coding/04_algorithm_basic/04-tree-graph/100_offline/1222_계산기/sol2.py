import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    data = input()
    # print(data)
    print(eval(data))