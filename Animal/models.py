from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animal/images')

    def __str__(self):
        return self.name
