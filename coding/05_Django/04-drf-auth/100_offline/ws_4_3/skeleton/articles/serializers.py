from rest_framework import serializers
from .models import Article


# articles/serializers.py


# articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
