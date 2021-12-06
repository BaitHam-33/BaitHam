
from django.forms import ModelForm

from .models import animal


class Add_Animal_Form(ModelForm):
    class Meta:
        model = animal
        fields = ['name', 'submitter', 'species', 'breed', 'description', 'sex', 'submission_date', 'image']