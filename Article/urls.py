from django.urls import path
from . import views


app_name = 'Article'

urlpatterns = [

    path('article_cat/', views.articles_cat, name='article_cat'),
    path('article_dog/', views.articles_dog, name='article_dog'),

    path('articles/', views.articles, name='articles'),

]