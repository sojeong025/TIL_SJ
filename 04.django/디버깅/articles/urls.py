from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name="index"),
    path('<int:pk>',views.detail, name="detail"),
    path('<int:pk>/delete',views.delete, name="delete"),
    path('create',views.create, name="create"),
]
