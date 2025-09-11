from django.urls import path
from . import views

urlpatterns = [
    # 왜? articles/ 경로에 GET or POST 요청이 왔을때,
    # 행위 method에 따라, 서로 다른 작업을 진행한다.
    # 경로만 보면 articles/
    # 행위와 더해서 보면 GET or POST articles/
    path('', views.article_get_or_create),
    path('<int:article_pk>/', views.article_detail),
]
