from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('hello/<str:name>/', views.hello, name='hello'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
