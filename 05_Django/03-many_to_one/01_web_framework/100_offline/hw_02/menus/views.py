from django.shortcuts import render
from django.http import JsonResponse
# 아래 문장은 django의 어떤 기능과 전혀 상관없다.
# 그냥 파이썬 문법이다. -> settings에 rest_framework를 등록 했냐 안했냐와 아무 상관없다.
from rest_framework.decorators import api_view


# Create your views here.
# 행위에 대한 처리.
# 여기는 GET만 받을 수 있습니다.
# 어... rest_framework 분명 강사는 settings에 등록 안했는데 왜 됨?
# -> 로직상, django rest framework가 가진 어떤 기능을 동작하도록 해야함.
# 그걸 누가 하느냐? django가 django rest framework에서 가져와서 해야함
# 그럼 당연히 django는 자기가 쓸 수 있는 app 목록에 rest_framework가 있어야함.
@api_view(['GET']) 
def menu_list(request):     
    # 이거는 그냥 외우십쇼, view 함수는 첫번째 매개변수 request임.
    # 아래의 리스트를 JSON 형식으로 반환.
    menus = [
            {"name": "Espresso", "price": 3000},
            {"name": "Americano", "price": 3500},
            {"name": "Latte", "price": 4000}
        ]
    return JsonResponse(menus, safe=False)

