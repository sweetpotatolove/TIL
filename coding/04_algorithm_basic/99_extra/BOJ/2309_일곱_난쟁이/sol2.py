import sys
sys.stdin = open('input.txt')


def search(n, cnt, result):
    if cnt > 100:
        return

    if n == 7 and cnt == 100:
        print(result, sum(result))
        return result
    else:
        for k in range(9):
            if visited[k] == 0:
                visited[k] = 1
                search(n + 1, cnt + data[k], result + [data[k]])
                visited[k] = 0


data = [int(input()) for i in range(9)]
visited = [0] * 9
search(0, 0, [])