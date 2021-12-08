from django.urls import path
from . import views


app_name = 'Article'

urlpatterns = [

    path('articles_cat/', views.articles_cat, name='article_cat'),
    path('articles_dog/', views.articles_dog, name='article_dog'),

    path('articles/', views.articles, name='articles'),

]