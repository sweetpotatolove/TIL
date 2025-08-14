"""
URL configuration for sns_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 이거 왜 굳이 2개로 나눠서 만드느냐? -> posts 앱은 urls.py 있지도않을걸 직접 만들어서 관리하냐?
    # 프로젝트가 커졌을때를 생각하자.
    # 프로젝트가 커져서 endpoint가 많아지게 되면... 이 path 함수가 엄청많아질건데
    # 디버깅 어떻게 하냐... app별로 기능별로, 경로별로 나눠서 관리하기 위해서 따로 만든다.
    path('posts/', include('posts.urls')),
]
