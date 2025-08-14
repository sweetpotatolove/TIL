from rest_framework import serializers
from .models import Author

'''
    우리는 DB가 중요하니, 예시는 계속 ModelSerializer 쓸거임
    왜냐? model에 이미 author에 대한 정보 다 적어놨음
        그게 id, name, .... 다양한 필드들...
    그래서, 직렬화도 그 Model class Author에 있는 정보 그대로 쓸거임!

    그건 그거고, Serializer의 원 역할이 뭔데?
    어떤 data를 fomatting 하는게 원 역할임
'''

# class SomeSerializer(serializers.Serializer):
#     # 얘는 모델에 대한 정보를 참고할 수 없음!
#     # 그럼 뭘 포맷팅 한다는거임?
#     # 그 포맷팅할 대상 데이터가 어떤 형태일건지 여기서 정의 하셈
#     title = serializers.CharField()
#     content = serializers.CharField()
#     opening_time = serializers.TimeField()

#     # 위에서 정의한 저 필드들을 그래서 어떻게? 최종적으로? Client한테 넘길건데?
#     class Meta:
#         fields = '__all__'
#         read_only_fields = ('opening_time')

class AuthorSerializer(serializers.ModelSerializer):
    # Meta class내에 있는 변수랑 밖에 있는 변수 어떤 차이가 있나요?
    # Author 모델을 토대로, 필드를 정의하라고했으니,
    # annotate로 추가한 필드는 Serializer가 처리할 수 없음!
    # book_count 필드 정의하기
        # 정의하는 방법 2가지
        # 하나는 내가 직접 source 찾아서 떄려박기
    # book_count = serializers.IntegerField(source='book_set.count', read_only=True)
    book_count = serializers.SerializerMethodField()
    # SerializerMethodField로 할당할 값을 정의할 메서드는
    # 그 get_필드명
    def get_book_count(self, obj):
        '''
            obj: 이 시리얼라이저를 호출한 객체 (아마 author 일듯)
        '''
        return obj.book_count
    
    class Meta:
        model = Author
        fields = '__all__'
