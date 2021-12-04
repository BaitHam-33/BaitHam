from django.shortcuts import render


def articles(request):
    return render(request, 'Article/articles.html')
