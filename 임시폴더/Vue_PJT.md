# Vue with DRF

# INDEX
- 프로젝트 개요
  - DRF 프로젝트 안내
  - Vue 프로젝트 안내
- 메인 페이지 구현
  - 게시글 목록 출력
  - DRF와의 요청과 응답
- CORS Policy
  - CORS Policy
  - CORS Headers 설정
- Article CR 구현
  - 전체 게시글 조회

# DRF 프로젝트 안내

## DRF 프로젝트 안내
- 스켈레톤 프로젝트 django-pjt 제공
- 외부 패키지 및 라이브러리는 requirements.txt에 작성되어 있음
> DRF 프로젝트는 "주석을 해제"하며 진행

# 프로젝트 개요

## Skeleton code 살펴보기 (1/11)
- Model 클래스 확인

```py
# articles/models.py
class Article(models.Model):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    # )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```py
# accounts/models.py
class User(AbstractUser):
    pass
```

## Skeleton code 살펴보기 (2/11)
- URL 확인

```py
# my_api/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    # path('accounts/', include('dj_rest_auth.urls')),
    # path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```

```py
# articles/urls.py
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
```

## Skeleton code 살펴보기 (3/11)
- Serializers 확인

```py
# articles/serializers.py
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('user',)
```

## Skeleton code 살펴보기 (4/11)
- views.py의 import 부분 확인

```py
# articles/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article
```

## Skeleton code 살펴보기 (5/11)
- View 함수 확인

```py
# articles/views.py
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

```py
# articles/views.py
@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    # print(serializer.data)
    return Response(serializer.data)
```

## Skeleton code 살펴보기 (6/11)
- settings.py 확인

```py
# settings.py
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    # 'rest_framework.authtoken',
    # 'dj_rest_auth',
    # 'corsheaders',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# SITE_ID = 1

# REST_FRAMEWORK = {
#     # Authentication
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
#     # permission
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ],
# }
```

## Skeleton code 살펴보기 (7/11)
- settings.py 확인

```py
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:5173',
#     'http://localhost:5173',
# ]
```

## Skeleton code 살펴보기 (8/11)
- Fixtures 확인

```json
[
  {
    "model": "articles.article",
    "pk": 1,
    "fields": {
      "title": "title",
      "content": "content",
      "created_at": "2023-07-04T08:21:53.976Z",
      "updated_at": "2023-07-04T08:21:53.976Z"
    }
  },
  {
    "model": "articles.article",
    "pk": 2,
    "fields": {
      "title": "제목",
      "content": "내용",
      "created_at": "2023-07-04T12:59:07.671Z",
      "updated_at": "2023-07-04T12:59:07.671Z"
    }
  }
  // ...
]
```

## Skeleton code 살펴보기 (9/11)
- 가상 환경 생성 및 활성화

```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

- 패키지 설치

```bash
$ pip install -r requirements.txt
```

## Skeleton code 살펴보기 (10/11)
- Migration 진행

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- Fixtures 데이터 로드

```bash
$ python manage.py loaddata articles.json
```

## Skeleton code 살펴보기 (11/11)
- Django 서버 실행 후, 전체 게시글 조회 요청
  - http://127.0.0.1:8000/api/v1/articles/

# Vue 프로젝트 안내

## Vue 프로젝트 안내 (1/3)
- 스켈레톤 프로젝트 vue-pjt 제공
- Vite를 사용해 Pinia 및 Vue Router가 추가 되어있음
- pinia-plugin-persistedstate

## Vue 프로젝트 안내 (2/3)
- 컴포넌트 구조

## Vue 프로젝트 안내 (3/3)
- 프로젝트 구조

# 프로젝트 개요

## Skeleton code 살펴보기 (1/8)
- App 컴포넌트

```vue
<!-- App.vue -->
<template>
  <header>
    <nav>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style scoped>
</style>
```

## Skeleton code 살펴보기 (2/8)
- route에 등록된 컴포넌트 (Article, Create, Detail, LogIn, SignUp)

```vue
<!-- views/….vue -->
<template>
  <div>
  </div>
</template>

<script setup>
</script>

<style>
</style>
```

## Skeleton code 살펴보기 (3/8)
- ArticleList 컴포넌트

```vue
<!-- components/ArticleList.vue -->
<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem />
  </div>
</template>

<script setup>
import ArticleListItem from '@/components/ArticleListItem.vue'
</script>
```

## Skeleton code 살펴보기 (4/8)
- ArticleListItem 컴포넌트

```vue
<!-- components/ArticleListItem.vue -->
<template>
  <div>
  </div>
</template>

<script setup>
</script>
```

## Skeleton code 살펴보기 (5/8)
- routes 현황

```js
// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
// import ArticleView from '@/views/ArticleView.vue'
// import DetailView from '@/views/DetailView.vue'
// import CreateView from '@/views/CreateView.vue'
// import SignUpView from '@/views/SignUpView.vue'
// import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   name: 'ArticleView',
    //   component: ArticleView
    // },
  ]
})
```

## Skeleton code 살펴보기 (6/8)
- store 현황

```js
// store/counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  return {}
}, { persist: true })
```

## Skeleton code 살펴보기 (7/8)
- main.js 현황

```js
// src/main.js
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)

app.mount('#app')
```

## Skeleton code 살펴보기 (8/8)
- 패키지 설치

```bash
$ npm install
```

- 서버 실행

```bash
$ npm run dev
```

# 메인 페이지 구현

# 게시글 목록 출력

## 개요
- ArticleView 컴포넌트에 ArticleList 컴포넌트와 ArticleListItem 컴포넌트 등록 및 출력하기
- ArticleList와 ArticleListItem은 각각 게시글 출력을 담당

# 메인 페이지 구현

## 게시글 목록 출력 (1/7)
- ArticleView의 route 관련 코드 주석 해제

```js
// router/index.js
import ArticleView from '@/views/ArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView,
    },
  ]
})
```

## 게시글 목록 출력 (2/7)
- App 컴포넌트에 ArticleView 컴포넌트로 이동하는 RouterLink 작성

```vue
<!-- App.vue -->
<template>
  <header>
    <nav>
      <RouterLink :to="{ name:'ArticleView' }">Articles</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>
```

## 게시글 목록 출력 (3/7)
- ArticleView 컴포넌트에 ArticleList 컴포넌트 등록

```vue
<!-- views/ArticleView.vue -->
<template>
  <div>
    <h1>Article Page</h1>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
</script>
```

## 게시글 목록 출력 (4/7)
- store에 임시 데이터 articles 배열 작성하기

```js
// store/counter.js
export const useCounterStore = defineStore('counter', () => {
  const articles = ref([
    { id: 1, title: 'Article 1', content: 'Content of article 1' },
    { id: 2, title: 'Article 2', content: 'Content of article 2' }
  ])
  return { articles }
}, { persist: true })
```

## 게시글 목록 출력 (5/7)
- ArticleList 컴포넌트에서 게시글 목록 출력  
- store의 articles 데이터 참조  
- v-for를 활용하여 하위 컴포넌트에서 사용  
- article 단일 객체 정보를 props로 전달

```vue
<!-- components/ArticleList.vue -->
<template>
  <div>
    <h3>Article List</h3>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
</script>
```

## 게시글 목록 출력 (6/7)
- ArticleListItem 컴포넌트는 내려 받은 props를 정의 후 출력

```vue
<!-- components/ArticleListItem.vue -->
<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  article: Object
})
</script>
```

## 게시글 목록 출력 (7/7)
- 메인 페이지에서 게시글 목록 출력 확인

# DRF와의 요청과 응답

## DRF로 부터 응답 데이터 받기
- 이제는 임시 데이터가 아닌 DRF 서버에 요청하여 데이터를 응답 받아 store에 저장 후 출력하기

## DRF와의 요청과 응답 (1/6)
- DRF 서버로의 AJAX 요청을 위한 axios 설치 및 관련 코드 작성  

```bash
$ npm install axios
```

```js
// store/counter.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
}, { persist: true })
```

---

## DRF와의 요청과 응답 (2/6)
- DRF 서버로 요청을 보내고 응답 데이터를 처리하는 getArticles 함수  

```js
// store/counter.js
const getArticles = function () {
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/articles/`
  })
  .then(res => {
    console.log(res)
    console.log(res.data)
  })
  .catch(err => console.log(err))
}

return { articles, API_URL, getArticles }, { persist: true }
```

---

## DRF와의 요청과 응답 (3/6)
- ArticleView 컴포넌트가 마운트 될 때 getArticles 함수가 실행되도록 함  
- 해당 컴포넌트가 렌더링 될 때 항상 최신 게시글 목록을 불러오기 위함  

```vue
<!-- views/ArticleView.vue -->
<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
</script>
```

---

## DRF와의 요청과 응답 (4/6)
- Vue와 DRF 서버를 모두 실행한 후 응답 데이터 확인  
- 에러 발생

---

## DRF와의 요청과 응답 (5/6)
- 그런데 DRF 서버 측에서는 문제 없이 응답했음 (200 OK)  
- 서버는 응답했으나 브라우저 측에서 거절한 것

---

## DRF와의 요청과 응답 (6/6)
- 브라우저가 거절한 이유  
- ‘localhost:5173’에서 ‘127.0.0.1:8000/api/v1/articles/’의 XMLHttpRequest에 대한 접근이 CORS policy에 의해 차단되었다.

# CORS Policy

## SOP
- (Same-origin policy)
- 동일 출처 정책

- 어떤 출처(Origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호 작용하는 것을 제한하는 보안 방식
> "다른 곳에서 가져온 자료는 일단 막는다."
> 웹 애플리케이션의 도메인이 다른 도메인의 리소스에 접근하는 것을 제어하여 사용자의 개인 정보와 데이터의 보안을 보호하고, 잠재적인 보안 위협을 방지
> 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임

## Origin (출처) (1/2)
- URL의 Protocol, Host, Port를 모두 포함하여 "출처"라고 부름
- Same Originm 예시
  - 아래 세 영역이 일치하는 경우에만 동일 출처(Same-origin)로 인정

## Origin (출처) (2/2)
- Same Origin 예시
  - 기준: `http://localhost:3000/articles/3/` 을 기준으로 동일 출처 여부 비교

| URL | 결과 | 이유 |
|------|------|------|
| http://localhost:3000/articles/ | 성공 | Path만 다름 |
| http://localhost:3000/comments/3/ | 성공 | Path만 다름 |
| https://localhost:3000/articles/3/ | 실패 | Protocol 다름 |
| http://localhost:80/articles/3/ | 실패 | Port 다름 |
| http://yahuhua:3000/articles/3/ | 실패 | Host 다름 |

## CORS policy의 등장
- 기본적으로 웹 브라우저는 같은 출처에서만 요청하는 것을 허용하며, 다른 출처로의 요청은 보안상의 이유로 차단됨
  - SOP에 의해 다른 출처의 리소스와 상호작용 하는 것이 기본적으로 제한되기 때문
- 하지만 현대 웹 애플리케이션은 다양한 출처로부터 리소스를 요청하는 경우가 많기 때문에 CORS 정책이 필요하게 되었음
> CORS는 웹 서버가 리소스에 대한민국 서로 다른 출처 간 접근을 허용하도록 선택할 수 있는 기능을 제공

## CORS
- (Cross-Oirign Resource Sharing)
- 교차 출처 리소스 공유

- 특정 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제
> 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함
> "CORS policy (교차 출처 리소스 공유 정책)"

## CORS Plicy
- (Cross-Origin Resource Sharing Plicy)
- 교차 출처 리소스 공유 정책

- 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
- 서버에서 결정되며, 브라우저가 해당 정책을 확인하여 요청이 허용되는지 여부를 결정
> 다른 출처의 리소스를 불러오러면 그 다른 출처에서 올바른 CORS header를 포함한 응답을 반환해야 함

## CORS 적용 방법

## CORS policy 정리
- 웹 애플리케이션이 다른 도메인에 있는 리소스에 안전하게 접근할 수 있도록 허용 또는 차단하는 보안 메커니즘
- 서버가 약속된 CORS Header를 포함하여 응답한다면 브라우저는 해당 요청을 허용
> 서버에서 CORS Header를 만들어야 한다.

# CORS Headers 설정

## CORS Headers 설정하기
- Django에서는 django-cors-headers 라이브러리 활용
> 손쉽게 응답 객체에 CORS header를 추가해주는 라이브러리

## django-cors-headers 사용하기 (1/3)
- 설치 (requirements.txt.로 인해 사전에 설치되어 있음)
```
$ pip install django-cors-headers
```

## django-cors-headers 사용하기 (2/3)
- 관련 코드 주석 해제  

```python
# settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
```

---

## django-cors-headers 사용하기 (3/3)
- CORS를 허용할 Vue 프로젝트의 Domain 등록  

```python
# settings.py

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]
```

## CORS 처리 결과 (1/3)

## CORS 처리 결과 (2/3)
- 메인 페이지에서 DRF 응답 데이터 재확인

```js
// store/counter.js
export const useCounterStore = defineStore('counter', () => {
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
    .then(res => {
      console.log(res)
      console.log(res.data)
    })
    .catch(err => console.log(err))
  }

  return { articles, getArticles }, { persist: true }
})
```

## CORS 처리 결과 (3/3)
- 응답 객체에서 'Access-Control-Allow-Origin' Header 확인
  - 개발자도구 - Network - Fetch/XHR

# Article Read 구현

# 전체 게시글 조회

## 전체 게시글 목록 출력 (1/3)
- 응답 받은 데이터에서 각 게시글의 데이터 구성 확인 (id, title, content)

# Article Read 구현

## 전체 게시글 목록 저장 및 출력 (2/3)
- store에 게시글 목록 데이터 저장  

```js
// store/counter.js
export const useCounterStore = defineStore('counter', () => {
  ...
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }
  return { articles, getArticles }
}, { persist: true })
```

---

## 전체 게시글 목록 저장 및 출력 (3/3)
- store에 저장된 게시글 목록 출력 확인  
  - pinia-plugin-persistedstate에 의해 브라우저 Local Storage에 저장됨  

# 참고

# 인증 with Vue

## 시작하기 전에 (1/2)
1. DRF에서 인증 관련 코드를 미리 주석 해제 혹은 작성 완료 후 진행
  1. dj-rest-auth[with-social]을 활용한 회원 관련 기능은 DRF 수업 내용 참고
2. Article과 User 간의 N:1 관계 형성 주석 해제 및 migrate 작업 진행
  1. Article Serializer, Article save 로직 등 점검
3. DB 초기화
  - db.sqlite3 삭제
4. Migration 과정 재 진행
5. 관리자 계정 생성 후, 게시글 1개 이상 작성
  - 기존 fixtures 데이터는 user 정보가 없으므로 사용 불가능.

## 시작하기 전에 (2/2)
- 정상 작동하던 게시글 전체 조회가 작동하지 않음
  - 401 status code 확인
> 게시글 조회 요청 시 인증에 필요한 수단(token)을 보내지 않고 있으므로 게시글 조회가 불가능해진 것

# 회원가입

# 인증 with Vue

## 회원가입 로직 구현 (1/10)
- `SignUpView` route 관련 코드 주석 해제  

```js
// router/index.js
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    }
  ]
})
```

---

## 회원가입 로직 구현 (2/10)
- `App` 컴포넌트에 `SignUpView` 컴포넌트로 이동하는 RouterLink 작성  

```vue
// App.vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

---

## 회원가입 로직 구현 (3/10)
- `views/SignUpView.vue` 회원가입 form 작성  

```vue
<template>
  <div>
    <h1>Sign Up Page</h1>
    <form>
      <label for="username">username :</label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password1">password :</label>
      <input type="password" id="password1" v-model.trim="password1"><br>

      <label for="password2">password confirmation :</label>
      <input type="password" id="password2" v-model.trim="password2">

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>
```

---

## 회원가입 로직 구현 (4/10)
- 사용자 입력 데이터와 바인딩될 반응형 변수 작성  

```vue
<!-- views/SignUpView.vue -->
<script setup>
import { ref } from 'vue'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
</script>
```

---

## 회원가입 로직 구현 (5/10)
- `SignUpView` 컴포넌트 출력 확인  
  - 브라우저에서 `/signup` 페이지로 이동 시 form 렌더링 확인

---

## 회원가입 로직 구현 (6/10)
- 회원가입 요청을 보내기 위한 `signUp` 함수가 해야 할 일  
  1. 사용자 입력 데이터를 받아  
  2. 서버로 회원가입 요청을 보냄  

```js
// stores/accounts.js
export const useAccountStore = defineStore('account', () => {
  const signUp = function () {
    …
  }
  return { signUp }
}, { persist: true })
```

---

## 회원가입 로직 구현 (7/10)
- 컴포넌트에 사용자 입력 데이터를 저장 후  
  store의 `signUp` 함수를 호출하는 함수 작성  

```vue
// views/SignUpView.vue
import { useAccountStore } from '@/stores/account'

const accountStore = useAccountStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  accountStore.signUp(payload)
}
```

```vue
<!-- views/SignUpView.vue -->
<form @submit.prevent="signUp">
  ...
</form>
```

---

## 회원가입 로직 구현 (8/10)
- 실제 회원가입 요청을 보내는 `store`의 `signUp` 함수 작성  

```js
// stores/accounts.js
const signUp = function (payload) {
  const username = payload.username
  const password1 = payload.password1
  const password2 = payload.password2
  // const { username, password1, password2 } = payload

  axios({
    method: 'post',
    url: `${API_URL}/accounts/signup/`,
    data: {
      username, password1, password2
    }
  })
  .then(res => {
    console.log('회원가입이 완료되었습니다.')
  })
  .catch(err => console.log(err))
}
```

## 회원가입 로직 구현 (9/10)
- 회원가입 테스트

## 회원가입 로직 구현 (10/10)
- Django DB 확인

# 로그인

## 로그인 로직 구현 (1/9)
- LogInView route 관련 코드 주석 해제  

```js
// router/index.js
import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView,
    }
  ]
})
```

---

## 로그인 로직 구현 (2/9)
- App 컴포넌트에 `LogInView` 컴포넌트로 이동하는 RouterLink 작성  

```vue
// App.vue
<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
      <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
      <RouterLink :to="{ name: 'LogInView' }">LogInPage</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>
```

---

## 로그인 로직 구현 (3/9)
- 로그인 form 작성

```vue
<!-- views/LogInView.vue -->
<template>
  <div>
    <h1>LogIn Page</h1>
    <form>
      <label for="username">username :</label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">password :</label>
      <input type="password" id="password" v-model.trim="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>
```

---

## 로그인 로직 구현 (4/9)
- 사용자 입력 데이터와 바인딩 될 반응형 변수 작성

```vue
<!-- views/LogInView.vue -->
<script setup>
import { ref } from 'vue'

const username = ref(null)
const password = ref(null)
</script>
```

## 로그인 로직 구현 (5/9)
- LogInView 컴포넌트 출력 확인

## 로그인 로직 구현 (6/9)
- 로그인 요청을 보내기 위한 `logIn` 함수가 해야 할 일  
  1. 사용자 입력 데이터를 받아  
  2. 서버로 로그인 요청 및 응답 받은 토큰 저장

```js
// stores/accounts.js
export const useAccountStore = defineStore('account', () => {
  const logIn = function () {
    …
  }
  return { signUp, logIn }
}, { persist: true })
```

---

## 로그인 로직 구현 (7/9)
- 컴포넌트에 사용자 입력 데이터를 저장 후 store의 `logIn` 함수를 호출하는 함수 작성

```vue
// views/LoginView.vue
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  accountStore.logIn(payload)
}
```

```vue
<!-- views/LoginView.vue -->
<form @submit.prevent="logIn">
  …
</form>
```

---

## 로그인 로직 구현 (8/9)
- 실제 로그인 요청을 보내는 store의 `logIn` 함수 작성  

```js
// stores/accounts.js
const logIn = function (payload) {
  const username = payload.username
  const password = payload.password
  axios({
    method: 'post',
    url: `${API_URL}/accounts/login/`,
    data: {
      username, password
    }
  })
  .then(res => {
    console.log('로그인이 완료되었습니다.')
    console.log(res.data)
  })
  .catch(err => console.log(err))
}
```

## 로그인 로직 구현 (9/9)
- 로그인 테스트
- 응답 객체 안에 Django가 발급한 Token이 함께 온 것을 확인

# 요청과 토큰

## Token을 store에 저장하여 인증이 필요한 요청마다 함께 보낸다.

## 토큰 저장 로직 구현 (1/2)
- 반응형 변수 token 선언 및 토큰 저장

```js
// stores/accounts.js
export const useAccountStore = defineStore('account', () => {
  const token = ref(null)

  const logIn = function (payload) {
    ...
    .then(res => {
      token.value = res.data.key
    })
    .catch(err => console.log(err))
  }

  return { signUp, logIn, token }
}, { persist: true })
```

## 토큰 저장 로직 구현 (2/2)
- 다시 로그인 요청 후 store에 저장된 토큰 확인

## 토큰이 필요한 요청
1. 게시글 전체 목록 조회 시
2. 게시글 작성 시

## 게시글 전체 목록 조회 with token (1/2)
- 게시글 전체 목록 조회 요청 함수 getArticles에 token 추가

```js
// stores/articles.js
import { useAccountStore } from './accounts'

export const useArticleStore = defineStore('article', () => {
  const accountStore = useAccountStore()

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        'Authorization': `Token ${accountStore.token}`
      }
    })
    ...
  }
})
```

## 게시글 전체 목록 조회 with token (2/2)
- 401 상태 코드가 사라지고 게시글이 정상적으로 출력되는 것을 확인

## 게시글 생성 with token (1/2)
- 게시글 생성 요청 함수 createArticle에 token 추가

```js
<!-- views/CreateView.vue -->
import { useAccountStore } from '@/stores/accounts'

const accountStore = useAccountStore()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      ...
    },
    headers: {
      'Authorization': `Token ${accountStore.token}`
    }
  })
}
```

## 게시글 생성 with token (1/2)
- 게시글 작성 확인

# 인증 여부 확인

## 사용자의 인증(로그인) 여부에 따른 추가 기능 구현
1. 인증 되지 않은 사용자
  > 메인 페이지 접근 제한

2. 인증 된 사용자
  > 회원가입 및 로그인 페이지에 접근 제한

## 인증 상태 여부를 나타낼 속성 값 지정
- token 소유 여부에 따라 로그인 상태를 나타낼 isLogin 변수 작성
- 그리고 computed를 활용해 token 값이 변할 때만 상태를 계산하도록 함

```js
// stores/accounts.js
export const useAccountStore = defineStore('account', () => {
  const isLogin = computed(() => {
    return token.value ? true : false
  })

  return { signUp, logIn, token, isLogin }
}, { persist: true })
```

## 1. 인증 되지 않은 사용자는 메인 페이지 접근 제한 (1/2)
- 전역 네비게이션 가드 beforeEach를 활용해 다른 주소에서 메인 페이지로 이동 시 인증 되지 않은 사용자라면 로그인 페이지로 이동시키기

```js
// router/index.js
import { useAccountStore } from '@/stores/accounts'

const router = createRouter({ … })

router.beforeEach((to, from) => {
  const accountStore = useAccountStore()
  if (to.name === 'ArticleView' && !accountStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
})
```

## 1. 인증 되지 않은 사용자는 메인 페이지 접근 제한 (2/2)
- 브라우저 local storage에서 token을 삭제 후 메인 페이지 접속 시도

## 2. 인증 된 사용자는 회원가입과 로그인 페이지에 접근 제한 (1/2)
- 다른 주소에서 회원가입 또는 로그인 페이지로 이동 시 이미 인증 된 사용자라면 메인 페이지로 이동시키기

```js
// router/index.js
router.beforeEach((to, from) => {
  const accountStore = useAccountStore()

  if (to.name === 'ArticleView' && !accountStore.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }

  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (accountStore.isLogin)) {
    window.alert('이미 로그인 되어 있습니다.')
    return { name: 'ArticleView' }
  }
})
```

## 2. 인증 된 사용자는 회원가입과 로그인 페이지에 접근 제한 (2/2)
- 로그인 후 회원가입, 로그인 페이지 접속 시도

# 03 PJT

# Vue를 활용한 SPA 구성

## 03 PJT 도전 과제
- 목표
  - pjt03 vue 프로젝트 생성
    - SFC 프로젝트 구성 필수
  - API에서 받아온 데이터로 프로젝트 구성
    - TMDB API
    - YouTube API
  - [도전] Django API 활용