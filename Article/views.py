from django.shortcuts import render

def articles_dog(request):
    return render(request, 'Article/articles_dog.html')

def articles_cat(request):
    return render(request, 'Article/articles_cat.html')

def articles(request):
    return render(request, 'Article/articles.html')