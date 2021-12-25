from django.db import models
from django.contrib.auth.models import User
from datetime import date

class list_task(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    status=models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


