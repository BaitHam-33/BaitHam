from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import storiesform
from Animal.models import Animal


def home(request):
    animals = Animal.objects.all()
    return render(request, 'adopter/home.html', {'animals': animals})

def articles(request):
    return render(request, 'adopter/articles.html')


def stories(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = storiesform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            note = "hey %s your story: %s been added to our stories page, thanks for sharing" % (
                form.cleaned_data['Name'], form.cleaned_data['title'])
            return render(request, 'adopter/stories.html', {'form': form, 'note': note})

        # if a GET (or any other method) we'll create a blank form
    else:
        form = storiesform()
        return render(request, 'adopter/stories.html', {'form': form})

