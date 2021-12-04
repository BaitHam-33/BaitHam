from django.db import models
from datetime import date

class report(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
