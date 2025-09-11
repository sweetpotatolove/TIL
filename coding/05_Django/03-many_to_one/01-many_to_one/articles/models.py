from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Article class를 참조 하는데, 내가 참조 중인 게시글이 삭제되면, 나도 삭제
    '''
        project의 urls.py에서, 내가 지금 요청 들어온것에 대한 처리를
        다른 위치에 있는 다른 모듈 혹은 어떠한 함수에 대해 처리를 위임하려고 할때
        그 대상을 직접적으로 호출하여 작성하는 것이 아니라,
        문자열 형태로 (현재 활성화 되지 않았어도) 지금 코드가 실행되는데 문제없도록
        실행 대상의 명확한 위치를 기록
        include("articles.urls") -> app_name.module_name
    '''
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
