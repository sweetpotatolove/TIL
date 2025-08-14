from rest_framework import serializers
from .models import CoffeeShop

class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeShop
        fields = '__all__'
