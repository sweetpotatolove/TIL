import sys
sys.stdin = open('input.txt')

from itertools import combinations

def find(field, size, target):
    for subset in combinations(field, size):
        if sum(subset) == target:
            for s in sorted(subset):
                print(s)
            return
    return None

nanjaeng = set()
for _ in range(9):
    nanjaeng.add(int(input()))

find(nanjaeng, 7, 100)
