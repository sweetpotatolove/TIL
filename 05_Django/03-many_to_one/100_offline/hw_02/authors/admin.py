from django.contrib import admin
from .models import Author
# Register your models here.

# 관리자 사이트에 등록 (저자 정보)
admin.site.register(Author)
