from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Animal.models import animal


def home(request):
    if request.user.is_authenticated:
        animals = animal.objects.all()
    else:
        animals = animal.objects.filter(Adoption='Y')
    return render(request, 'adopter/home.html', {'animals': animals})

def admin (request):
    return HttpResponseRedirect(reverse('admin:index'))