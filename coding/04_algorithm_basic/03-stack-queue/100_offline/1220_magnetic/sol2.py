import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())    # 정수로 바꿔야 할까?
    # 0 -> 빈칸
    # 1 -> N극 (아래로 이동)
    # 2 -> S극 (위로 이동)
    data = [list(map(int, input().split())) for _ in range(N)]

    # 디버그를 위해서 전체 tc 수도 줄이고,
    # 입력 값도 내가 눈으로 보기 좋게 줄이고
    result = 0
    for y in range(N):
        flag = False
        for x in range(N):
            if data[x][y] == 1:
                flag = True
                # print(flag)
            if flag == True and data[x][y] == 2:
                # 교착 상황이 만들어 졌다.
                # 이전에 마주했던 1에 의해 만들어 질 수 있는
                # 교착 상황은 이제 없다.
                result += 1
                flag = False
    print(f'#{tc} {result}')