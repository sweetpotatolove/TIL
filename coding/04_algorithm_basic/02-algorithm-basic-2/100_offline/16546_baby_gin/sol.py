import sys

sys.stdin = open('input.txt')


def baby_gin():
    card1 = [0 for _ in range(10)]
    card2 = [0 for _ in range(10)]

    for idx in range(12):
        n = cards[idx]
        if idx % 2 == 0:  # 짝수 -> player1
            card1[n] += 1  # idx 하나 증가시키고
            if card1[n] == 3:  # triplet이면 -> player1 승리
                return 1
            if check_run(card1) == 1:  # run이면 -> player1 승리
                return 1
        else:  # 홀수 -> player2
            card2[n] += 1
            if card2[n] == 3:  # triplet이면 -> player2 승리
                return 2
            if check_run(card2) == 1:  # run이면 -> player2 승리
                return 2
    # return 안만났다면 12개의 카드를 도는 동안 승부 x -> 무승부
    return 0


def check_run(card):
    # 0 ~ 9까지의 숫자 카드 중에서
    for i in range(8):  # 최대 i + 2 -> 9 (마지막 인덱스 9)
        if (
            card[i] >= 1 and card[i + 1] >= 1 and card[i + 2] >= 1
        ):  # 연속된 수가 1이상 체크되어있다면 run
            return 1


T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))  # 12장의 카드 정보
    winner = baby_gin()
    print(f'#{tc} {winner}')