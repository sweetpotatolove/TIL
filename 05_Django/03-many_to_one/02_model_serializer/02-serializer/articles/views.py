from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_get_or_create(request):
    if request.method == 'GET':
        # 전체 게시글 조회
        articles = Article.objects.all()
        # 전체 게시글 조회라서, id, title만 보여주고싶음.
        # serializer라는걸 정의!
        serializer = ArticleListSerializer(articles, many=True)
        # 직렬화를 마친 객체의 data만 사용자에게 반환.
        # 그리고, 이 직렬화는 django가 아닌 DRF로 인해 만들어진 것!
        # 즉, 반환도 django 기본 기능이 아니라 DRF의 반환방식을 쓸것
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # 사용자가 보낸 데이터로 article을 생성하고,
            # 앗, 지금 우리가 만든 시리얼라이저는... content에 대한
            # 필드가 없다...
        # 그 정보가 유효한지 검증하고,
        if serializer.is_valid():
            # 정상적이면 저장하고
            serializer.save()
            # 반환한다. 
            return Response(serializer.data)
        

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET': # article 객체를 직렬화하여 반환
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # instance: 업데이트할 article 객체
        # data: 업데이트할 데이터
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        # :partial = True로 설정하면 일부 필드만 업데이트 가능 // request Method Patch 일 때
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):  # serializer를 통해 입력 데이터의 유효성 검사
            serializer.save(raise_exception=True)
            return Response(serializer.data)
