import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    data = input()

    result, stick = 0, 0
    for idx in range(len(data)):
        # 여는 괄호는 막대기 or 레이저 포인터
        if data[idx] == '(':
            # 닫는 괄호가 나올 때 까지 여는 괄호 카운트
            stick += 1
        # 닫는 괄호가 나오면
        else:
            # 직전이 여는괄호 였다면, 레이저 발사
            if data[idx - 1] == '(':
                # 직전 괄호는 막대기가 아니라, 레이저였으므로 stack -1
                stick -= 1
                result += stick  # 잘린 막대기 수 만큼 총량 증가

            # 직전이 닫는 괄호였다면, 레이저가 아님. 막대기 종료
            else:
                # 막대기 총 개수 감소,
                stick -= 1
                # 짜투리 개수 만큼 1 증가.
                result += 1

    # 최종 결과 값 == 레이저 쏜 횟수 + 쇠막대기 갯수
    print(f'#{tc} {result}')