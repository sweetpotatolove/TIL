'''
    해당 코드는 제가 사용하기 위해 만든 코드입니다.
    여러분들은 BASE_URL에 해당하는 부분의 경로가 저와 다릅니다 :)
    사용하고자 하신다면 수정해서 사용해 주세요.
'''

# os
# 현재 작업 위치
import os
import subprocess
# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()
# 특정 폴더 내로 이동 후에 작동하도록 하려면? os 모듈의 어떤 함수?
# 현재 폴더 및 하위 폴더를 반복
# subprocess.run(['문자열 형태로', '실행할 명령어', 변수])
subject = input('과목을 입력해 주세요 : ')
seperators = ['hw', 'ws']  # -> 반복문 사용해서 만들어 지도록 하면되겠다.
set_number = input('세트 번호를 입력해 주세요 : ')
for sep in seperators:
    if sep == 'hw':
        BASE_URL = f'https://lab.ssafy.com/data_track/{subject}_daily_homework/'
        stages = [2, 4]
    else: 
        BASE_URL = f'https://lab.ssafy.com/data_track/{subject}_daily_practice/'
        # 보충 수업에서 쓰는 문제는 a, b, c로 되어 있다.
        stages = [1, 2, 3, 4, 5, 'a', 'b', 'c']
    for stage in stages:   
        URL = f'{BASE_URL}{subject}_{sep}_{set_number}_{stage}'
        subprocess.run(['git', 'clone', URL])

