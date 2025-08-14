from rest_framework import serializers
from .models import Post


# 나는 생성자를 정의하지 않아도,
# 부모 클래스에 생성자가 정의되어 있다면, 그 내용을 상속받아서
# 내 인스턴스를 생성할때, 적절한 정보를 넘겨 줄 수 있겠다.
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', )    # 필드 정의할때, tuple 아니어도 됨 -> list여도 됨.
        # fields = ('title', 'created_at')

# 클래스를 만드는 이유를 생각하면서 이름을 짓자.
# 과연진짜 생성할때만ㅇ ㅒ를 쓸까? 아니지 않나?
# 데이터 상세조회 -> 모든 필드 보여줘야함.
# 데이터 수정 -> 모든 필드 보여줘야함 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'