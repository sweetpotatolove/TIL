from django.urls import path
from . import views


urlpatterns = [
    # 1:N
    path("<int:teacher_pk>/", views.create_course), # 강사 pk를 받아서 새로운 강좌를 생성하는 페이지로 이동
    # M:N
    path("<int:teacher_pk>/assistant/<int:course_pk>/", views.assistant),  # 강사 pk와 강좌 pk를 받아서 강좌의 부강사를 지정하는 페이지로 이동
 
]