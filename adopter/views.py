from django.shortcuts import render, get_object_or_404, redirect
from Animal.models import Animal

def home(request):
    animals = Animal.objects.all()
    return render(request, 'adopter/home.html', {'animals': animals})

def articles(request):
    return render(request, 'adopter/articles.html')

