from django.shortcuts import render, redirect
from .models import list_task
from .forms import TaskForm

def all_task(request):
   tasks = list_task.objects.all()
   return render(request, 'Taskboard/all_task.html', {'tasks': tasks})

def task_detail(request, id=None):
    task_obj = None
    if id is not None:
        task_obj = animal.objects.get(id=id)
    context = {"object": task_obj}
    return render(request, 'Taskboard/task_detail.html', context=context)
