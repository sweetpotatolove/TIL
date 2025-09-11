import sys
sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())  # 회전 횟수
    magnet = [deque(map(int, input().split())) for _ in range(4)]  # 4개의 자석 상태
    rotate = deque([list(map(int, input().split())) for _ in range(K)])  # 회전 명령들

    for i in range(4):
        magnet[i] = deque(magnet[i])  # 각 자석을 deque 형태로 변환
    rotate = deque(rotate)  # 회전 명령도 deque로 변환

    while rotate:
        start, RL = rotate.popleft()  # 회전 시작 자석 번호, 회전 방향
        s = start - 1                 # 인덱스(0~3) 맞추기
        note = [0] * 4                 # 각 자석별 회전 방향 기록
        note[s] = RL                   # 시작 자석 회전 방향 기록

        # 오른쪽 방향으로 전파
        for i in range(s, 3):
            if magnet[i][2] != magnet[i + 1][6]:  # 맞닿은 극이 다르면
                note[i + 1] = -note[i]            # 반대 방향으로 회전
            else:
                break                             # 같으면 전파 중단

        # 왼쪽 방향으로 전파
        for i in range(s, 0, -1):
            if magnet[i][6] != magnet[i - 1][2]:
                note[i - 1] = -note[i]
            else:
                break

        # 기록된 회전 방향대로 실제 회전 수행
        for i in range(4):
            magnet[i].rotate(note[i])

    # 최종 점수 계산 (각 자석의 12시 위치 자극에 따라 가중치 합)
    res = magnet[0][0] + (magnet[1][0] * 2) + (magnet[2][0] * 4) + (magnet[3][0] * 8)
    print(f"#{test_case} {res}")