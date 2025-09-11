from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User 모델에 별다른 필드 정의 할 것도 아닌데.. 왜 이런 짓을 하고 있느냐??
# django가 기본적으로 제공하는 auth.User 모델이 있기는 한데...
    # 영원히 auth.User에서 변경사항 하나 없이 쓰더라도
    # django는 Custom User Model 을 만드는걸 `강력히 권장`
class User(AbstractUser):
    pass