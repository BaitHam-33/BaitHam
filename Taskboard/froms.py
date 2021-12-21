from django.forms import ModelForm
from django import forms
from .models import list_task
from .models import task


class TaskForm(ModelForm):
    class Meta:
        model = list_task
        fields = ['date', 'name', 'text']

class Add_Animal_Form(ModelForm):
            class Meta:
                model = task
                fields = ['name', 'description']