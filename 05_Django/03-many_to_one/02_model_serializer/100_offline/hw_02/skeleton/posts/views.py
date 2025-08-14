from django.shortcuts import render
# 난 분명 venv에 설치했어 rest_frameworm 근데 왜 자동 완성 안돼?
# bash 가상환경 활성화도 했어!  -> bash는 bash입니다. (VSC가 아니라는 뜻)
# 자동완성은 VSC가 해주는 것. -> 인터프리터 설정 화면 우측 하단.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, PostListSerializer
from .models import Post    # 현재 위치라는 것을 명시하기 위해서. 현재위치 `.` 을 앞에 붙인다.

# Create your views here.
# 모든 post 정보를 조회 -> GET
# post 생성 요청 -> POST
@api_view(['GET', 'POST'])
def post_list(request):
    # 사용자의 요청 method가 GET이라면 조회에 대한 적절한 응답을 해줄거야.
    if request.method == 'GET':
        # Post 정보를 얻고 싶어요. -> python으로 SQL 쓰는법 몰라요.
        # model에 Post 클래스를 정의 해 놨고 -> 이걸 DB에서 쓰고 있어요.
        # 우리는 python 문법으로 class 사용하는 그 사용법 그대로 쓰면되요.

        #       Model.manager.querySet API
        posts = Post.objects.all()  # 직렬화

        serializer = PostListSerializer(posts, many=True)
        # 직렬화가 뭔데 -> 어디서든 문제없이 사용할 수 있는 데이터타입으로 변환하는 과정.
        # 이건 RESTful 한 API를 만들 수 있게 해주는 REST_FRAMEWORK가 가지고 있다.
        # serialzer를 정의 할건데....

        # 저렇게 직렬화된 데이터를 반환 해야하는데...
        # JsonReponse라는걸 썼었는데 왜 rest_framework가 주는 Response를 써야 하는걸까?
        # serializer 객체는 어떻게 만들어졌는가? 아시나요? 전 몰라요. rest_framework가 알아서 만들어줌.
        return Response(serializer.data)
    elif request.method == 'POST':  # 그런데 사용자가 POST요청을 보냈다면
        # 게시글 생성을 위한 적절한 응답을 해줄거야.
        # 우리가 정의해둔 PostSerializer는 어떤 데이터들에 대해서 직렬화 해주냐
            # id, title만 해주기로 해놨다.
            # 이러면 안된다.
        # 게시글을 생성하려면 사용자가 보낸 데이터를 삽입해서 DB에 저장할거야.
        # 사용자가 요청보낸 데이터는? request.data에 들어잇어.
        serializer = PostSerializer(data=request.data)
        # 그렇게 사용자가 넘긴 데이터를 아무튼 DB에다가 우겨넣으면되나? 안된다
        # 올바른 데이터를 넣었는지 확인해야한다. is_valid()
        # 만약, 유효성 검사를 통과하지 못했을때, 적절한 예외상황을 발생시키도록
        # raise_exception=True <- 이런 인자를 같이 넘겨주면, 알아서 처리해줌.
        # print('여기서 오류가 났을까?')
        if serializer.is_valid(raise_exception=True):
            # print('유효성 검사는 통과 했을까?')
            serializer.save()
            # print('저장까지 하고, 반환과정에서 오류가 났을까?')
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_pk):
    # 특정 post 하나만 받아오기
    post = Post.objects.get(pk=post_pk)
    if request.method == 'PUT':
        # __init__(self, instance=None, data=empty, **kwargs)
        # serializer = PostSerializer(instance=post, data=request.data)
        # serializer = PostSerializer(post, data=request.data)
        serializer = PostSerializer(post, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
