from django.shortcuts import render, redirect
from .forms import storyForm
from .models import story


def create_story(request):
    if request.method == 'GET':
        return render(request, 'success_story/create_story.html', {'form': storyForm()})
    else:
        form = storyForm(request.POST)
        new_story = form.save()
        new_story.save()
        return redirect('success_story:all_stories')


def all_stories(request):
    stories = story.objects.all()
    return render(request, 'success_story/all_stories.html', {'stories': stories})
