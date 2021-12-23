from django.urls import path
from .views import all_task, task_detail, createTask,export_pdf,export_excel

app_name = 'Taskboard'

urlpatterns = [
    path('', all_task, name='all_task'),  # View all tasks
    path('task_detail/<int:id>', task_detail, name='task_detail'),
    path('createTask/', createTask, name='createTask'),
    path('export_pdf',export_pdf,name='export_pdf'),
    path('export_excel',export_excel,name='export_excel'),
]
