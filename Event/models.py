from django.db import models
from datetime import date


# create a new model for event app

class event(models.Model):
    name = models.CharField(max_length=100)  # the name of the event
    date = models.DateField(default=date.today)  # the date of the event
    text = models.TextField(blank=True)  # the content of the event
    image = models.ImageField(upload_to='Event', blank=True)  # photo of the event

    def __str__(self):
        return self.name
