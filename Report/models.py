from django.db import models


class report(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name
