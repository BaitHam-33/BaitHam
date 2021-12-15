from django.db import models
from datetime import date

class event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='Event', blank=True)

    def __str__(self):
        return self.name
