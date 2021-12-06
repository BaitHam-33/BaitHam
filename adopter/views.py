from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponseRedirect

from Animal.models import animal


def home(request):
    animals = animal.objects.all()
    return render(request, 'adopter/home.html', {'animals': animals})

