from django.contrib import admin
from .models import Book, Genre
# Register your models here.

# 책, 장르 M:N 관계고
# 둘다 정보 있어야 하니까 둘다 관리자 사이트에 등록
admin.site.register([Book, Genre])
