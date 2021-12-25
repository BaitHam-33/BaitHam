from django.shortcuts import render
from .models import articlesModel


def all_articles(request):
    articles = articlesModel.objects.all()
    context = {'articles': articles}
    return render(request, 'Article/articles.html', context)
