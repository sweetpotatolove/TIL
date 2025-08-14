from django.urls import path
from . import views


urlpatterns = [
    # N번 작가의 상세 정보
        # 사용자가 PK에 대한 정보를 URL에 담아서 보낼 예정
        # 그 때 경로는 variable routing
    path('<int:author_pk>/', views.author_deatil),  
]
