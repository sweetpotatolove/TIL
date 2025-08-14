from django.db import models
# from authors.models import Author

# Create your models here.
class Book(models.Model):
    # 저자랑 1:N 관계 만들기?
    # 저자의 PK값을 FK로 정의할 필드를 만든다.
    # ForeignKey(to=Model Name)
    # FK를 저장하는 필드는 DB에서 column이 만들어질때, author_id 라는 이름으로 생성됨.
    author = models.ForeignKey('authors.author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)