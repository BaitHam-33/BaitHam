from django.forms import ModelForm
from django import forms
from .models import stories


class storiesform(forms.ModelForm):
   class Meta:
       model = stories
       fields = ["Name", 'title', 'story']
       #labels = {'Name': 'Name: ', 'title': 'Title: ', 'story': 'your story: '}


