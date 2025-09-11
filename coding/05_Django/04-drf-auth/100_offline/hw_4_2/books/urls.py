from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list),
    path('borrow/<str:isbn>/', views.book_borrow),
]
