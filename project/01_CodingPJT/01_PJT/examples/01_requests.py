# 외부 라이브러리 requests를 import
import requests
from pprint import pprint

# 오늘 수업에서는 jsonplaceholder라고하는 sample형 json 데이터 제공 API를 사용할 것
# requests는 get요청으로 응답받은 데이터를 담은 객체에게
# json() 이라는 메서드를 만들어 두었다. -> JavaScrtip 형식의 JSON 데이터를
# 파이썬에서 사용할 수 있도록, 파이썬의 data type에 맞게 변환해주는 메서드
    # response.json()
response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
user_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
# print(user_response)
# print(response)
completed_todos = []   # 최종 결과물을 담을 리스트
fields = ['id', 'title']
for item in response:
    # 전체 데이터중, completed가 True인 경우에 대해서만 사용할 것
    # 임시 변수 item에 할당된 데이터 타입은 dict 따라서, completed에 대해서 물어보자면,
    # Key가 completed인 경우, 그 value가 True인 경우만 출력
    # if item['completed'] == True:
    #     print(item)
    if item.get('completed'):  
        # 그중, 내가 필요로 하는 2개의 필드 id, title 만 따로 모은다.
        temp_item = {}
        for key in fields:  # 'id', 'title'
            # temp_item['id'] = item['id'] value
            temp_item[key] = item[key]
            # {'id': 1, 'title: 'lorem ipsu, ...'}
        for user in user_response:
            if user['id'] == item['userId']:
                # ctrl + alt + 위아래 방향키 : 커서 복제
                # ctrl + shift + 좌우 방향키: 단어 단위로 드래그
                user_info = {
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email'],
                }
                temp_item['user'] = user_info
        completed_todos.append(temp_item)
pprint(completed_todos)

