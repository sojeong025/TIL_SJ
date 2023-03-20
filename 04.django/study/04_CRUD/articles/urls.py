from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    # variable routing
    path('<int:article_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # variable routing
    path('edit/<int:article_pk>/', views.edit, name='edit'),
    path('update/<int:article_pk>/', views.update, name='update'),
    # variable routing
    path('delete/<int:article_pk>/', views.delete, name='delete'),
]
