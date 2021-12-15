from django.forms import ModelForm
from .models import event


class EventForm(ModelForm):
    class Meta:
        model = event
        fields = ['name', 'date', 'text','image']