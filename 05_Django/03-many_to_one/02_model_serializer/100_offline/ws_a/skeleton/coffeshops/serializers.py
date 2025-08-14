from rest_framework import serializers
from .models import CoffeShop


# serializers가 가지고 있는 무슨 class를 상속 받을까?
# Model에 대한 정보를 포함하고 있는 Serializer를 만들려고 한다.

# 매장 정보 생성, 수정, 상세 조회용 시리얼 라이저.
class CoffeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeShop
        fields = '__all__'