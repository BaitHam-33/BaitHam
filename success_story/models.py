from django.db import models
from datetime import date


class story(models.Model):
    date = models.DateField(default=date.today, verbose_name='תאריך')
    name = models.CharField(max_length=100, verbose_name='שם')
    text = models.TextField(blank=True, verbose_name='תיאור')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "stories"
