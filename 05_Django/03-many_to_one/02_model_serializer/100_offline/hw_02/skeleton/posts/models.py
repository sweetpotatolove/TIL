from django.db import models

# Create your models here.
'''
Post 모델 : SNS의 게시글을 저장하기 위해 정의된 데이터베이스 모델로, 다음과 같은 필드로 구성된다.
title: 게시글의 제목을 저장하는 필드입니다. 최대 100자의 문자열을 저장할 수 있다.
content: 게시글의 내용을 저장하는 필드입니다. 긴 텍스트를 저장할 수 있다.
created_at: 게시글이 생성된 시간을 저장하는 필드다. 자동으로 현재 시간이 설정되며, 수정할 수 없다.
updated_at: 게시글이 마지막으로 수정된 시간을 저장하는 필드다. 자동으로 현재 시간이 설정되며, 게시글이 수정될 때마다 갱신된다.
'''
# Q. 모델을 수정해서 DB에 반영시키면 되는데 굳이 Migrations을 거치는 이유가 있을까요? 
# Q. migrations폴더에 생기는 저 파일 번호가 0001 부터 시작되는데 9999 넘어가면 어케됨?
    # A. 10000_이렇게 만들어짐.
'''
    이 프로젝트 시작시. 2019년 DB를 생성했다.
    2020년 프로젝트 개선으로 인해서 DB를 변경하였습니다.
    DB의 테이블의 구조가 달라졌다.
    2019년도에 사용했었던 데이터와 2020년도에 사용하는 데이터가 모두 있는 상황.
    DB가 변경되었다는 사실을 설계도에 기록해두지 않았다면,
    단순 데이터만 보아서는 2019년도에 사용했던 데이터는 현재 프로젝트에서 사용할 수 없는.
    특정 컬럼이 완전히 비어있는 data가 되겠다.
        -> DB의 변경 연혁을 기록해 두는 용도가 되겠다.
'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add => 자동_지금_추가
    created_at = models.TimeField(auto_now_add=True)
    # auto_now => 자동_지금
    updated_at = models.TimeField(auto_now=True)
