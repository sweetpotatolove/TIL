"""
URL configuration for libraries_system project.

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
    # 앞쪽 문자열 -> 내가 원하는대로 맘대로 바꾸면된다.
    path('api/', include('books.urls')),
    # accounts와 관련된 이 경로들도 내 마음대로 바꾸면된다.
    # 라이브러리 입장에서의 나름의 배려
        # accounts라는 app이름이 대체로 관례적이고, django를 쓴다면 보통 auth관련 app은
        # accounts라고 이름짓습니다. -> django가 몇가지 기능들을 미리 준비헀는데
            # 그때의 link연결 포인트를 accounts라고 만들어놨어요
    # accounts는 니가 진짜 써서 만드는 그 app을 위해서 남겨둘게.
    # 하지만 우리는 지금 accounts에서 별도로 작업할게 없다.
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/singup/', include('dj_rest_auth.registration.urls'))
]
