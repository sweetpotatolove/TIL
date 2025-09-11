from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 인증과 관련된 테이블을 설정할 때,
    # 장고가 기본으로 제공해주는 필드들 (username, password, email 등)을
    # 수정 없이 그대로 사용한다고 하더라도,
    # 장고는 User 모델을 custom해서 등록하기를 `강력히 권장`한다.
        # 이때, 단순히 accounts 앱에 User 모델을 만들기만 한다고해서,
        # 기존의 django가 제공해주는 그 인증, 권한, auth 모델과의
        # 복잡한 연관 관계가 모두 한번에 수정되는 것은 아님!
    # 우리는 django에게, 이 class가 기존의 auth class를 대체할 것임을 설정한다.
    # 설정? 어디서? -> settings.py
    pass
