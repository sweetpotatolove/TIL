from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import CoffeeShop
from .serializers import CoffeeShopSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def list_create_coffee_shops(request):
    if request.method == 'GET':
        coffee_shops = get_list_or_404(CoffeeShop)
        serializer = CoffeeShopSerializer(coffee_shops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CoffeeShopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
