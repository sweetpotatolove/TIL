# bfs 방식으로 풀기.
import sys
sys.stdin = open('input.txt')

def search(x, y):
    # 습관적으로 코드 적기
    # visited = [[0] * 100 for _ in range(100)]
    # queue로 조사 한다.
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            '''
                # 습관적으로 코드적기
                # 1. 범위를 벗어나지 않고
                # 2. 0(길)인 경우만 이동
                # if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and data[nx][ny] == 0:
                
                # 위 코드는 이번 문제에서는 필요없다.
                # 이건 확실히 코드 실행 시간에 영향을 미친다.
                # q에 삽입될 대상 후보군의 양 만큼 if 연산을 해야 하기 때문이다.
                
                # and data[nx][ny] == 0:
                # 길인 경우만 이동가능 X
                    -> 벽인 경우는 이동 불가능    
            '''
            if data[nx][ny] != 1:
                if data[nx][ny] == 3:
                    return 1    # 도착 성공했음을 반환.

                # 이번 조사는 출발지 1개, 도착지 1개.
                # 즉, 누구든 도착만 했으면 된거임.
                data[nx][ny] = 1    # 왔던길 전부 벽으로 만들어버림
                # if tc == 1:
                #     for d in data:
                #         print(d)
                # print()
                queue.append((nx, ny))
    # 모든 경우에 대해서 모두 조사를 했음에도,
    # 즉, while이 끝났음에도 아직 함수가 안끝나고 있네?
    # 위에서 while안에서 return 을 만적이 없어서 여기까지 왔다는거네?
    return 0        # 아, 모든 경우에도 도착점 못갔구나.



# _ 를 사용하는 경우가 있는데,
# for문으로 10번 반복 할건데, 그때 정의한 임시변수를
# 이 for문 안에서 사용하지 않을때, 이렇게 작성
    # -> 메모리나, 시간이나 그런거에 더 빨라지거나 그런거 없다.
    # `_` 다른곳에서 실수로라도 쓸 일 없겠죠?
for _ in range(10):
    tc = int(input())
    # 100 * 100 으로 고정.
    # 1: 벽, 0: 길, 2: 출발점, 3: 도착점.
    data = [list(map(int, input())) for _ in range(100)]
    result = 0      # 도착지에 도착 할 수 있는지 정보
    # BFS로 그래프를 탐색할 건데, 시작 정점이 어디인지 모르는 상황.
    # -> BFS를 정의할 때, 시작 정점의 좌푯값을 넘겨 받을 수 있도록 만들어주자.
    # 시작 정점이 어딘지 찾아 나가야 한다.
    for x in range(100):
        for y in range(100):
            if data[x][y] == 2:     # 출발지
                # 약속, 조사 도중, 도착지에 도달하면 True 반환해주기
                result = search(x, y)    # 해당 위치에서 출발
                # break는 본인이 속해있는 for문에 대해서만 정지.
                break           # 출발지가 하나 밖에 없으니 한번 조사했으면 끝.
        if result:  # 만약, 목적지에 도착했다면, result를 1로 바꿀 것.
            break   # 그렇게 어떤 경우든 result가 1이 되면 break
    print(result)