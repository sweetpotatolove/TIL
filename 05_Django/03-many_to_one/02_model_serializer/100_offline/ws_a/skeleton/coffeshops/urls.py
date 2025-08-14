from django.urls import path
from . import views


urlpatterns = [
    # 왜 endpoint가 한개인데, 2개의 요청에 대한 처리가 가능하냐
    # 식별자. 즉 사용자의 요청에 대한 URL + method. 행위에 따라서 다르게 구성
    # GET or POST <- 서로 완전히 다른 요청이므로, 로직상으로 구분하면 그만.
    # GET이 되었든, POST가 되었든 어쨋든 shop_info와 관련된 어떤 로직
    # 그러기 위해서 필요로 하는 추가적인 경로의 내용이 필요로 하진 않는다.
        # 경로도 명시적으로 적고 싶어서... create 요청은 create를 경로에 넣고싶어요.
        # POST method가 이미 create인데 경로 또 create를 넣는다?
        # POST 'shop_info/create/' <- 이 방법은
        # `역전앞` 과 같다.
            # 그러면, view함수에는 왜 create 넣었는데...?
            # 이건 용도가 다르다. client가 요청을 보낼 경로를 적는것과
            # 그 경로에서 실행될 함수가 무슨 역할을 할 것인지는 다르다.
    path('', views.shop_list_or_create),
    # 상세 조회, 수정, 삭제를 위한 경로 -> PK
    path('<int:shop_pk>/', views.shop_detail),
]