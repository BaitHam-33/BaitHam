from django.urls import path
from django.conf.urls import url
from .views import all_task, task_detail

app_name = 'Taskboard'

urlpatterns = [

    path('', all_task, name='all_task'),#View all tasks
    path('task_detail/<int:id>', task_detail, name='task_detail')
]