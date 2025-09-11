from rest_framework import serializers
from .models import Article

'''
Serializer를 통해 직렬화할 때 사용할 필드를 지정할 때 사용 가능한 속성
1. fields: 직렬화할 필드를 지정
    - '__all__': 모든 필드를 직렬화
2. exclude: 직렬화에서 제외할 필드를 지정
3. read_only_fields: 읽기 전용 필드를 지정 - 1:N 관계에서 학습 예정

- 참고: 튜플 또는 리스트로 여러 개의 필드를 지정할 수 있음

'''

class ArticleListSerializer(serializers.ModelSerializer):
    # 직렬화를 한다.
    class Meta:
        # 모델에 대한 정보를 토대로
        model = Article
        # fields = '__all__'
        fields = ('id', 'title',)

# 위에는 오로지 전체 목록만을 위한 시리얼라이저 였다면
# 이번에는 범용적으로 게시글에 대한 전반적인 처리가 가능한 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('created_at', 'updated_at',)