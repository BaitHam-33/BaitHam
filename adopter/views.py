from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Animal.models import animal


def home(request):
    animals = animal.objects.all()
    return render(request, 'adopter/home.html', {'animals': animals})

def reports(request):
    return render(request,'adopter/reports.html')

def admin ():
    return HttpResponseRedirect(reverse('admin:index'))