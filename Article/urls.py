from django.urls import path
from .views import articles_dog, articles_cat


app_name = 'Article'

urlpatterns = [

    path('articles_cat/', articles_cat, name='article_cat'),
    path('articles_dog/', articles_dog, name='article_dog'),

    #path('articles/', articles, name='articles'),
]