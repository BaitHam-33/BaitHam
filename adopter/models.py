from django.db import models




class stories(models.Model):
    Name = models.CharField(max_length=200)
    story = models.TextField(max_length=5000)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

