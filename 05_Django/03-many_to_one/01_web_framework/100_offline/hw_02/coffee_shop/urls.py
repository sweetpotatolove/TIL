"""
URL configuration for coffee_shop project.

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
# 이곳에서 직접 app의 views를 import 해서 경로 작성
    # -> 프로젝트가 확장될 가능성이 없다면 여기다가 해도 상관 없음.
# 단, 높은 확률로 대부분 app이 2개 이상 필요할 예정이므로, 각자 관리 할 수 있도록 나눠주자.

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/menus/ 라는 경로로 요청이 들어오게 되면,
    # menus/ 뒤에 어떤 글자가 오는지에 따라 서로 다른 처리를 해야 할 건데
    # 그 부분에 대해서는 menus app의 urls.py에 작성된 내용을 따른다.
        # django의 기본 설정은 모든 url은 pjt의 urls.py에서 설정하는게 기본!
        # 따라서, app의 구성 목록에 굳이 안쓸 urls.py를 추가해 주지는 않는다.
    # 그러나, 상황에 따라서는 필요할 수 있다! -> 파일을 만들면 된다.
        # 그럼 urls.py의 `urls` 라는 이름은 어떠한 역할이 있는가? XXXXX
        # 어떤 역할이 있는 이름은 아니지만, url을 관리할 파일명을
        # url 말고 다른 이름으로 뭘로 할건데? 전 모르겠거든요?
    path('menus/', include('menus.urls')),
]
