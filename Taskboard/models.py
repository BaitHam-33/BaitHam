from django.db import models
from django.contrib.auth.models import User
from datetime import date


class list_task(models.Model):
    date = models.DateField(default=date.today)
    name = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=5000, blank=False)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "לוח מטלות"