from django.forms import ModelForm
from .models import report

# create a form for report app

class ReportForm(ModelForm):
    class Meta:
        model = report
        fields = ['date', 'name', 'text']