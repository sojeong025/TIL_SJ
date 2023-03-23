# articles/urls.py

from django.urls import path
from . import views

# 변수명 app_name은 꼭 지켜야 한다
app_name = 'articles'

urlpatterns = [
    # URL mapping -> include
    # Naming URL patterns
    path('index/', views.index, name='index'),
    # http://127.0.0.1:8000/articles/create/
    path('create/', views.create, name='create'),
    path('<int:age>/', views.info, name='info'),
    # 1. 문자열인 곳은 항상 제일 뒤로 만들기
    # 2. 경로 profile 명시해두기
    path('<name>/profile/', views.profile, name='profile'),
]