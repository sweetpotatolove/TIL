'''
3x3 크기의 2차원 리스트를 생성하여 초기 좌석 배치를 표현하시오. 좌석은 'O'로 표시합니다.
    3 x 3 
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
                    ]
'''
seats = [
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
    ['O', 'O', 'O'],
]
# 2차원 리스트를 구성하기 위해 모든 내용을 한번 다 풀어서 써보자.
# step 1. 'O'를 3개 가지고 있는 리스트 만들기
# 시퀀스 연산자로 'O'를 3번 반복해서 가지고 있는 리스트 만들기
seats = ['O'] * 3
print(seats)    # ['O', 'O', 'O']
# step 2. 이 seats를 3개 가지고 있는 리스트 만들기.
# seats_list = [seats] * 3    # 반복 하는 것이기 때문에...
# print(seats_list)
# seats_list[0][0] = 'X'
# 얕은 복사 이슈 발생.
# print(seats_list)   # [['X', 'O', 'O'], ['X', 'O', 'O'], ['X', 'O', 'O']]

# 반복문을 통해서 한땀 한땀 넣어보자.
# seats_list = []
# for i in range(3): # 3번 삽입
#     seats_list.append(seats[:])    # seats 리스트를 3번 삽입한다. 얕은복사를 해서
# seats_list[0][0] = 'X'
# print(seats_list)

# seats_list = [seats[:] for i in range(3)]
# 이건 왜 복사 이슈 안생김?
# 순회하면서 계속 새로운 ['O', 'O', 'O'] 리스트를 만들기 때문에. 다른 값들이다.
seats_list = [['O'] * 3 for i in range(3)]
# seats_list[0][0] = 'X'
print(seats_list)

'''
(0,2), (1,0), (1,2), (2,0), (2,2) 좌석을 예매 처리하시오. 예매된 좌석은 'X'로 표시합니다.
예매된 좌석을 포함하여 현재 좌석 배치를 출력하시오.
'''
reservations = [(0,2), (1,0), (1,2), (2,0), (2,2)]
# 반복문 실행시 iterable 객체의 각 요소를 item에 할당한다.
# 우리는... 저 (0, 2)가 2차원 리스트의 각 col, row의 index로 사용하고 싶다.
for item in reservations:
    '''
        (0, 2)
        (1, 0)
        (1, 2)
        (2, 0)
        (2, 2)
    '''
    print(item) # tuple -> sequence -> index 접근 가능
    print(item[0], item[1]) # 0 2
    seats_list[item[0]][item[1]] = 'X'

# 언패킹 -> 2개 이상의 변수에 나눠서 할당하기
# reservations의 각 요소 -> (0, 2)
# a, b = 0, 2
# a, b = (0, 2)
for row, col in reservations:
    seats_list[row][col] = 'X'
print(seats_list)   # [['O', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

# 이쁘게 출력하기
# 2차원 리스트를 하나하나 순회하면서 출력하기.
for row in seats_list:  # [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
    for item in row:
        # print는 기본인자로 end='\n' 이라는 값을 가진다.
        # \n의 역할은 줄바꿈.
        # end 인자에 할당할 값을 ' ' 공백으로 바꿨다 -> 이제 줄바꿈 대신 공백이 하나 추가.
        print(item, end=' ')    # O O X X O X X O X
    # 근데... 한 row 모두 출력하면 줄 바꿈 하고 싶어.
    # 한 row는 첫번째 반복문 마다 바뀐다.
    print()

# 이건 2차원 리스트로 직접 순회하면서 print의 특성을 알아낸 방식
# 이번엔 소 심플한 방법
print()
for item in seats_list:
    # print(item) # ['O', 'O', 'X'] 
    # 프린트는 출력할 대상을 가변인자 *values 로 받는다.
    # 즉, 여러개 넣어도 잘 출력해준다. -> 공백을 기준으로 모든 요소를 다 출력 해준다.
    # 그럼..
    # 이 리스트 item을 * 언패킹 하면? item이 가진 각 요소를 print에 쪼개서 넣어준다.
    print(*item)