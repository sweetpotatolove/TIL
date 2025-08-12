# Django Model & ORM
## Model
- Model을 통한 DB 관리를 배워보자

    ![DB](모델DB관리.png)
    - article에서 title, content를 어디에 저장할 것인가?

### Django Model
DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공

- 테이블 구조를 설계하는 '청사진(blueprint)'

- models.py에 클래스 정의해주면 됨

    ![class](model클래스)
    - 설명..

- 작성한 모델 클래스는 최종적으로 DB에 아래와 같은 테이블 구조를 만듦

    ![classDB]()

- `django.db.models` 모듈의 `Model` 이라는 부모 클래스를 상속받음
    - Model은 model에 관련된 모든 코드가 이미 작성되어 있는 클래스
    - 개발자는 가장 중요한 **테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것**(상속을 활용한 프레임워크의 기능 제공)




- model class
    1. `클래스 변수명`
        - 테이블의 각 **필드(열) 이름**

    2. `model Field` 클래스
        - 테이블 필드의 **데이터 타입**
        - 설명..

    3. `model Field 클래스의 키워드 인자`(필드 옵션)
        - 테이블 필드의 **제약조건** 관련 설정
        - 설명..

※ 제약 조건

-> 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙

-> ex. 숫자만 저장되도록, 문자가 100자까지만 저장되도록 하는 등


## Migrations
model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법

- Migrations 과정

    ![과정](migrations.png)
    - 객체는 설계도...
    - 클래스로 정의해둔 내용을 토대로 청사진만들 것임(makemigrations)
    - 청사진 내용을 토대로 DB에 테이블 생성(migrate)
    

- Migrations 핵심 명령어 2가지
    1. `python manage.py makemigrations`
        - model class를 기반으로 최종 설계도(migration) 작성

    2. `python manage.py migrate`
        - 최종 설계도를 DB에 전달하여 반영

- migrate 후 DB 내에 생성된 테이블 확인
    - Article 모델 클래스로 만들어진 articles_article 테이블

        ![article 테이블]()

### 추가 Migrations
※ 이미 생성된 테이블에 필드를 추가해야 한다면?

1. 추가 모델 필드 작성
    
    ![추가모델1]()

2. 이미 기존 테이블이 존재하기 때문에 필드를 추가할 때 필드의 기본 값 설정이 필요

    ![추가모델2]()
    - 1번: 현재 대화를 유지하면서 직접 기본 값 입력하는 방법
    - 2번: 현재 대화에서 나간 후 models.py에 기본 값 관련 설정하는 방법

3. 추가하는 필드의 기본 값을 입력해야 하는 상황
    - 날짜 데이터이기 때문에 직접 입력하기 보다 Django가 제안하는 기본 값을 사용하는 것 권장
    - 아무것도 입력하지 않고 enter 누르면 Django가 제안하는 기본 값으로 설정됨

    timezone: 시간 기준을 utc로 할건지, 아시아 서울로 할건디,,

4. migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인

    ![추가모델4]()
    - Django는 설계도를 쌓아가면서 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록 함('git commit'과 유사)
    - 버전 관리..!

5. migrate 후 테이블 필드 변화 확인
    - `python manage.py migrate`

        ![추가모델5]()
    

### 실습
02 폴더

`$ python -m venv venv`

`$ source venv/Scripts/activate` 

`$ pip install django`

`code .gitignore` -> `venv/` , `db.sqlite3`
최상단에 깃이그노어가 있다면 뭐 따로 안만들어도 된다는데 뭔말이

하단에 써야하는 이-유

config -> settings.py -> INSTALLED_APPS에 "article" app 등록되어 있는지 확인

config -> urls -> 주석.. -> articles -> urls가 있구나..

내 프로젝트 입장에서는 articles가 새로운 뭐시기로 받아들여짐. 왜? 설계도가 없기 때문

`python manage.py makemigrations` 설계도 생성

`python manage.py migrate`

Database -> `+` 버튼 -> SQLite -> Path에 02_어디에  Allfies 보게 해서 db.sqlite3 -> +content -> models.py에 아래 내용 작성

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

다시
`python manage.py makemigrations`
-> 1 -> 
```
  articles\migrations\0002_article_created_at_article_updated_at.py
    + Add field created_at to article
    + Add field updated_at to article
```
확인

`python manage.py migrate`

※ model class에 변경사항(1)이 생겼다면, 반드시 새로운 설계도를 생성(2)하고, 이를 DB에 반영(3)해야 함

-> 1. model class 변경 2. makemigrations -> 3. migrate

### Model Field
DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의

- `CharField()`
    - 길이의 제한이 있는 문자열을 넣을 때 사용
    - 필드의 최대 길이를 결정하는 max_length는 필수 인자

- `TextField()`
    - 글자의 수가 많을 때 사용

- `DateTimeField()`
    - 날짜와 시간 넣을 때 사용


## Admin site
### Automatic admin interface
Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공

-> 데이터 확인 및 테스트 등을 진행하는데 매우 유용

1. admin 계정 생성


2. DB에 생성된 admin 계정 확인


3. admin에 모델 클래스 등록


4. admin site 로그인 후 등록된 모델 클래스 확인


5. 데이터 생성, 수정, 삭제 테스트


6. 테이블 확인



## ORM
### Object-Relational-Mapping
객체지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

- ORM 역할
    - 사용하는 언어가 다르기 때문에 소통 불가
    - Django에 내장된 ORM이 중간에서 이를 해석!!

        ![ORM역할]()
    

### QuerySet API
ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구

-> API를 사용하여 SQL이 아닌 Python 코드로 데이터 처리



### QuerySet API 실습
1. Postman 설치
    - API를 구축하고 사용하기 위한 플랫폼
    - API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공
    - 설치 후 로그인 해서 Workspaces - MyWorkspace
    - Postman 화면 구성

        ![postman](postman화면.png)

2. URL과 HTTP requests methods 설계
    ![requests methods 설계]()

음..



### QuerySet API 실습 - Create
데이터 객체를 만드는(생성하는) 3가지 방법

1. 


2. 


3. 


※ `save()` : 객체를 데이터베이스에 저장하는 메서드

### QuerySet API 실습 - Read
- 대표적인 조회 메서드
    - Return new QuerySets
        - `all()`
        - `filter()`
    - Do not return QuerySets
        - `get()`

- `all()`
    - 전체 데이터 조회

- `filter()`
    - 특정 조건 데이터 조회

- `get()`
    - 단일 데이터 조회

        ![]()
    - get() 특징
        - 객체를 찾을 수 없으면 **DoesNotExist** 예외를 발생시킴
        - 둘 이상의 객체를 찾으면 **MultipleOjectsReturned** 예외를 발생시킴
        - 이런 특징으로 인해 **primary key 와 같이 고유성(uniqueness)을 보장하는 조회에서 사용**해야 함

### QuerySet API 실습 - Update


### QuerySet API 실습 - Delete


강사님이 요 실습 내용 말로 한번에 쭉ㄷ 설명함..


## Django Serializer
### Serialization (직렬화)
여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 구성할 수 있는 포맷으로 변환하는 과정

- Serialization 예시
    - 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

-> 즉, Serialization는 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정


### Serializer Class
- Serializer
    - Serialization을 진행하여 Serialized data를 반환해주는 클래스

- ModelSerializer
    - Django 모델과 연결된 Serializer 클래스
    - 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞춰 Serializaion 진행

- ModelSerializer class 사용 예시
    - Article 모델을 토대로 직렬화를 수행하는 ArticleSerializer 정의
    - serializers.py의 위치나 파일명은 자유롭게 가능

- Meta class
    - ModelSerializer의 정보를 작성하는 곳
    - `fields` 및 `exclude` 속성
        - exclude 속성을 사용하여 모델에서 포함하지 않을 필드 지정 가능

        ![]()

## CRUD with ModelSerializer
### GET
- ModelSerializer를 적용한 리스트 조회 로직
    
    ![]()
    ![]()
    ![]()

- ModelSerializer의 인자 및 속성
    
    ![]()
    - many 옵션
        - Serialize 대상이 QuerySet인 경우 입력
    - data 속성
        - Serialized data 객체에서 실제 데이터를 추출

- 과거 view 함수와의 비교
    - 과거
        
        ![]()
    - 현재

        ![]()

- ModelSerializer를 적용한 단일 조회 로직
    1. 단일 게시글 데이터 조회하기
        - 각 게시글의 상세 정보를 제공하는 ArticleSerializer 정의

        ![]()
    
    2. url 및 view 함수 작성

        ![]()
    3. `http://127.0.0.:8000/articles/1/` 응답확인

### POST
- 게시글 데이터 생성하기
    - 데이터 생성이 성공했을 경우 201 Created 응답
    - 데이터 생성이 실패했을 경우 400 Bad request 응답

1. **article_list** view 함수 구조 변경(method에 따른 분기처리)

    ![]()

2. `http://127.0.0.:8000/api/v1/articles/` 응답확인

3. 새로 생성된 게시글 데이터 확인
    - GET `http://127.0.0.:8000/articles/6/`

※ `is_valid()` : 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

- 유효성 검사
    - 수집한 데이터가 정확하고 유효한지 확인하는 과정
    - 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것을 고려해야 함
    - 이런 과정과 기능을 직접 개발하지 않고 DRF가 제공하는 serializer class를 사용
    - 유효성 검사 예시
        - content 필드가 누락됐을 때 반환 결과 확인
        
        ![]()
    

### DELETE
1. 게시글 데이터 삭제하기
    - 요청에 대한 데이터 삭제가 성공했을 경우 204 No content 응답

        ![]()
    
2. DELETE `http://127.0.0.:8000/api/v1/articles/1/` 응답확인

### PUT
1. 게시글 데이터 수정하기
    - 요청에 대한 데이터 수정이 성공했을 경우는 200 OK 응답

2. PUT `http://127.0.0.:8000/api/v1/articles/5/` 응답확인

3. GET `http://127.0.0.:8000/api/v1/articles/5/` 수정된 데이터 확인

- `partial` argument

    ![]()
    - 부분 업데이트를 허용하기 위한 인자
    - 예를 들어, partial 인자 값이 False일 경우 게시글 title만을 수정하려고 해도 반드시 content값도 요청 시 함께 전송해야 함
    - 기본적으로 serializer는 모든 필수 필드에 대한 값을 전달 받기 때문
        - 즉, 수정하지 않는 다른 필드 데이터도 모두 전송해야 하며, 그렇지 않으면 유효성 검사에서 오류 발생


## 참고
- 데이터베이스 초기화


- Migrations 기타 명령어
    - `python manage.py showmigrations`
        - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
        - [X] 표시가 있으면 migrate가 완료되었음을 의미
    - `python manage.py sqlmigrate articles 0001`
        - 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어
    
- 첫 migrate 시 출력 내용이 많은 이유는?
    - Django 프로젝트가 동작하기 위해 미리 작성되어있는 기본 내장 app들에 대한 migration 파일들이 함께 migrate 되기 때문

- SQLite
    - DB관리 시스템 중 하나이며 Django의 기본 데이터베이스로 사용됨
    - 파일로 존재하며, 가볍고 호환성이 좋음

- ORM, QuerySET API를 사용하는 이유
    - DB 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 됨
    - DB와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움

- `raise_exception` (꼭 기억하기!!)
    - `is_valie()`의 선택 인자
    - 유효성 검사를 통과하지 못할 경우 **ValidationError** 예외를 발생시킴
    - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며, 기본적으로 HTTP 400 응답을 반환
