import datetime
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    entrance_time = models.TimeField()
    leaving_time = models.TimeField(default=datetime.datetime.now)
