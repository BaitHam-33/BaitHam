from django.db import models
from datetime import date

class list_task(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name


class task(models.Model):
    name = models.CharField(max_length=100)  # Name of the task
    description = models.TextField(blank=True)  # Describe the task

    def __str__(self):
        return self.name
