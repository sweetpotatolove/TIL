# menus앱에 요청이 들어올 각 경로들을 이곳에서 관리
from django.urls import path
from . import views

'''
    def func():
        print('func')
    
    def other(some_func):
        some_func()
        return None

    othre(func)
'''
urlpatterns = [
    # http://127.0.0.1:8000/menus/ 라는 곳으로 요청이 들어오면
    # views 모듈에 있는 menu_list 함수를 호출한다.
    path('', views.menu_list),
]
