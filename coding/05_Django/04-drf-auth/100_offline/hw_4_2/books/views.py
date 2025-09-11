from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookListSerializer
from .models import Book
from .func import func

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)

# POST는 데이터베이스 뭘 수정하니 마니 하더니... 지금은 조회만하는데요?
# POST 요청 왔을때 DB 수정하는 로직을 쓰겠다는건

# 로직 -> DB에 새로운 값을 생성하는 로직
    # Client의 method를 POST로 제한하겠다.
    # 그걸 내가 구현
@api_view(['POST'])
def book_borrow(request, isbn):
    # pk = book_pk
    # get이 pk로만 조회가 되는줄 아는 경우가 있는데 아니다!!!
    # get querySet API에서 중요한건, 조회 결과가 반드시 단 1개의 객체일 수만 있으면된다.
    # print(isbn)
    result = func()
    print(result)
    # SQL작성 -> 사용자 요청에 맞는 Query 작성해서 DB에서 얻어와서 처리....
        # 내 DB에 있는 데이터 외의 참조 데이터 ex) csv -> pandas등으로 처리
        # 그걸 사용자에게 반환. -> JSON  -> Client 측에서 적절히 처리.
    book = get_object_or_404(Book, isbn=isbn)
    if book.borrowed:
        data = {
            'error': 'This book is already borrowed.'
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    book.borrowed = True    # 바꾸기만하면 객체의 정보만 바뀐다
    book.save()             # DB에 반영
    # book = Book.objects.get(isbn=isbn)
    serializer = BookListSerializer(book)
    return Response(serializer.data)