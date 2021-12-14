from django.db import models
from datetime import date


# create a new model for report app

class report(models.Model):
    date = models.DateField(default=date.today)  # date of the report
    name = models.CharField(max_length=100)  # name of the reporter
    text = models.TextField(blank=True)  # the content of the report

    def __str__(self):
        return self.name
