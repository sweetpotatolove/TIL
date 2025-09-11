import sys
sys.stdin = open('input.txt')
import heapq

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    o_list = [list(map(int, input().split())) for i in range(N)]
    max_heap = []
    largest = []
    for oper in o_list:
        if oper[0] == 1:
            heapq.heappush(max_heap, -oper[1])
        else:
            if max_heap:
                largest.append(-heapq.heappop(max_heap))
            else:
                largest.append(-1)

    print(f'#{test_case}', end=' ')
    for p in largest:
        print(p, end=' ')
    print()

