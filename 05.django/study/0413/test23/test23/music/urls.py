from django.urls import path
from . import views

# 앱 네임이나 url 네임은 굳이 필요 없음
# json 파일로 만드는 거라 굳이 안써도 된다함

urlpatterns = [
    path('music/', views.music_list), # 모든 음악 정보 조회
    path('music/<int:pk>', views.music_detail), # 모든 음악 정보 조회
]