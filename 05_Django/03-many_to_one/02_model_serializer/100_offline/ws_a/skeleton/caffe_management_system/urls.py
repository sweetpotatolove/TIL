"""
URL configuration for caffe_management_system project.

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
'''
# pjt의 ursl.py에 경로를 직접 설정하는 경우는 언제인가?
    # 이 프로젝트가 충분히 작아서, 굳이 경로를 파일별로 나누지 않아도 될때
    # 그럼 과제할때 안나눠도 되는거아님? -> 그르킨함...
# 우리가 파일을 나눠야 하는 분기점 -> 결국 개발자가 결정.
    # 우리는 template을 다루는 django를 경험 해본 적이 없다.
    # template도 django가 직접 다룰때는 왜 url 을 나눠 놓는 편이편하냐?
        # accounts 앱의 어떤 페이지 (login 페이지) 에서, 
        # articles의 전체 페이지로 돌아가야 하는 링크를 만들어야함.
            # 그 경로를 a tag에 적어야함. 어디로 보내야하는지? 경로를? 직접?
            # 하드코딩 하지 않는다. -> src="articles/list/"
            # src="{% url 'articles:list' %}"
            # src="{% url 'app_name:url_name' %}"
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop_info/', include('coffeshops.urls')),
]
