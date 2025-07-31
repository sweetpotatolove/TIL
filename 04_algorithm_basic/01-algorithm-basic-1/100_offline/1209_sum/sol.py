# sys
import sys
# open을 사용해서 input 파일을 연다
sys.stdin = open('input.txt')

# 이 문제는 10개의 TC를 가진다.
for _ in range(10):
    tc = input()    # 테스트케이스 번호 입력
    # 입력 받은 문자열을 공백 기준으로 쪼개서 정수로 바꾼다음 리스트에 담는걸 100번반복
    data = [list(map(int, input().split())) for _ in range(100)]
    print(data)
    # 각 행마다 가진 값들을 더한다.
    # 각 열마다 가진 값들을 더한다.
    # 대각선의 값들을 더한다.
    # 그 모든 값들 중 제일 큰 값을 구한다. -> max 금지

    # 100 x 100을 2차원 리스트로 받아야한다.
    # 즉, 한번 입력받은 한줄에 100개의 숫자가 공백을 기준으로 문자열로 오게됨
        # 이걸 100번 반복해야함.

    # data = []   # 2차원 배열을 만들기 위한 리스트
    # for _ in range(100):
    #     tmp_list = input().split()  # 공백 기준으로 쪼개서 리스트로 만듬
    #     # 공백 기준으로 쪼개진 문자열 (ex '13', '24') 를 정수로 바꿔야함
    #     map_data = map(int, tmp_list)
    #     # 리스트로 만들어야함
    #     map_to_list_data = list(map_data)
    #     # data.append(tmp_list)       # 그 리스트를 data에 추가
    #     data.append(map_to_list_data)
    # print(data)
