from django.db import models
from django.conf import settings


# articles/models.py
class Article(models.Model):
    # user = models.ForeignKey(
    #     'accounts.User', on_delete=models.CASCADE
    # )
    # 그러면 그냥 문자열로 적으면 되지 왜 귀찮구로...?
    # django가 기본적으로 User에 대한 Auth 모델을 지원
    # User 모델이란 내용은, 매우 복잡한 관계를 가지고 있으므로
    # 우리는 현재 `활성화` 된 유저 모델에 대한정보를
    # 장고 개발자들 끼리는 AUTH_USER_MODEL에 적기로 `약속`
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
