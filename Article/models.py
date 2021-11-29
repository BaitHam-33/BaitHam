from django.db import models


class articles(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    type = models.CharField(max_length=10, choices=[("cat", "Cat"), ("dog", "Dog")])

    def __str__(self):
        return f'name: {self.name}\n type: {self.type}'
