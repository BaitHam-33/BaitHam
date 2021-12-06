from django.forms import ModelForm
from django import forms
from .models import report


class ReportForm(ModelForm):
    class Meta:
        model = report
        fields = ['date', 'name', 'text']