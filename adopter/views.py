from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Animal.models import animal


def home(request):
    animals = animal.objects.all()
    return render(request, 'adopter/home.html', {'animals': animals})

def admin ():
    return HttpResponseRedirect(reverse('admin:index'))

def contact_us(request):
    return render(request, 'adopter/contact_us.html')