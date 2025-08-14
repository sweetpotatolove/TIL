from django.urls import path
from . import views 


urlpatterns = [
    # posts/ 경로로 GET 요청이 왔다 -> 조회 요청이겠구나.
    # posts/ 경로로 POST 요청이 왔다 -> 생성 요청이겠구나.
    # 내가 정하는거다.
    path('', views.post_list),
    # 수정 기능 -> 누구를 수정할 거니
    # variable rouing에 적은 변수명과
    # view 함수의 매개변수명이 다르면 동작할까?
    # 내가 경로를 작성할때 있어서, URL의 올바른 표현을 위해
    # variable routing에 사용된 변수의 위치는 실제 post_detail view함수의
    # 매개변수 위치와 다를 수 있다.
    # path('<int:pk_1>/<int:post_pk>/', views.post_detail),    
    path('<int:post_pk>/', views.post_detail),    
    # path('<int:post_pk>/', views.post_edit),    
    # path('<int:post_pk>/', views.post_delete),    
    # path('<int:post_pk>/<str:query>/', views.post_search),    
]