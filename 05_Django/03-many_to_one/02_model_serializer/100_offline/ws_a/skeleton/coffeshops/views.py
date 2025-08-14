from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CoffeShopSerializer
from .models import CoffeShop

# Create your views here.
# 요구사항. GET 요청과 POST 요청에 대해서 처리하는 view 작성하기
    # 그래서 그 모든 코드 한번에 와다다닥 쓰고 서버키기 절대 금지.
    # 우리는 로직상 확인하기 쉬운 것들 기능 먼저 1개 구현하고, 테스트하기.
@api_view(['GET', 'POST'])
def shop_list_or_create(request):
    '''
        1. 사용자가 POST 요청을 보냈다. -> 조건 분기하기
        2. 사용자가 POST를 위해서 데이터를 보냈다. -> 데이터 받기
        3. 그 데이터를 serializer에 집어넣어서 직렬화 한다.
        3. 그 데이터가 DB에 삽입 되어도 마땅한지 유효성 검사를 한다.
            3-1. 주의. 유효성검사는 Serializer에 정의된 field에 대해서만 한다.
        4. 유효성 검사를 통과했다면, DB에 반영한다.
            4-1. save 메서드를 호출하지 않으면, 그냥 python instance일 뿐이다.
        5. 정상적으로 모든 과정을 마쳤다면 적절한 응답.
    '''
    if request.method == 'POST':
        # 매장 정보 생성할 수 있어야함. -> 직렬화가 없네? 만들어야지
        serializer = CoffeShopSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'GET':
        '''
            1. 게시글 전체 조회 요청이 왔다.
            2. 전체 게시글 정보를 all() 을 사용해서 조회 했다.
            3. 이때, 데이터가 하나도 없다면, 나는 status code를 무엇을 반환해야할까?

            A. 200 OK와 빈 배열 -> 지금 아래의 코드 상으로는 200 OK가 오더라.
                -> 빈 배열은 왜 보내주냐?
                -> 전체 조회를 했다-> 그 결과로 아마 순회를 하지 않을까? 일반적인 상황
                -> 우리는 빈 배열을 반환함으로써, 상대에게 오류가 나지 않도록 배려,
                -> 데이터가 없음을 나타내 주고
                -> 200 -> 아무튼 조회에 대한 요청을 정상적으로 성공했다는 사실을 알림
                    -> 4xx client의 잘못도 아니고,
                    -> 5xx server의 잘못도 아니다!
            B. 404 Page Not Found
                -> 전체 조회에서 404를 반환해야 하는 경우?
                -> 상대방이 조회 했었던 그 전체 목록이 `반드시` 존재 했어야 하는 데이터
                -> 요청 보낸 위치에서 해당 데이터가 존재하지 않을수가 없는데, 없는 경우
                    -> 특정한 조건에 맞춰 filter를 거쳐서 얻는 정보...
                        -> 그 검색 조건을 사용자가 잘못 적은 경우
        '''
        # 조회 요청 왔을때 어떤 데이터 보여줄건지
        # 어떤 필드 보여줄건지 누가 정하냐? -> BackEnd 개발자가 정하겠죠.
        # -> FrontEnd랑 같이 잘 협의 하십쇼!
            # 모든 커피샾 객체들 조회
        shops = CoffeShop.objects.all()
        serializer = CoffeShopSerializer(shops, many=True)
        return Response(serializer.data)
    
@api_view(['DELETE'])
def shop_detail(request, shop_pk):
    '''
        1. 넘겨받은 shop_pk 데이터를 하나 조회한다.
        2. 그 인스턴스에 대해서, PUT, GET, DELETE method에 따라 다른 일을 한다.
    '''
    shop = CoffeShop.objects.get(pk=shop_pk)
    if request.method == 'DELETE':
        shop.delete()
        # 삭제 요청인데 난 뭘 응답해준담...? 성공했다는 사실은 알려야하는디...
        # 매장 정보 삭제 해달래서 삭제했고, 응답해줄 데이터 아무것도 없어서
        # 아무것도 없는 그냥 빈 값 응답해줌! 200 status code는 넘겨줬음!
        # 근데 이따구로 만들어두면 FE가 잔뜩 화냄
            # 그 왜 빈객체라도 보내주던가... 204라도 보내주던가... 오류라고라도 해주던가
            # 아무것도 안줘서 FE 에러났는데, 200 OK 왓으면 요청도 잘 한건데
            # 뭐가 문젠데? 나 디버깅이 안되잖아!!!!!!!!!!!
        # 204_no_content는 DELETE에 대해서, 응답하는 `너에게 줄 데이터 없음`을 의미하기도 하면서
        # 이게 진짜로 content가 없어서 못준다. 라는 의미보다는
        # 처리는 다 했는데, `난 너에게 줄 데이터가 없다.`
        return Response(status=status.HTTP_204_NO_CONTENT)
