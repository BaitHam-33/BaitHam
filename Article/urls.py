from django.urls import path
from . import views


app_name = 'Article'

urlpatterns = [
    path('articles/', views.articles, name='articles'),
]