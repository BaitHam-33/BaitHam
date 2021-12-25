from django.db import models


class articlesModel(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    type = models.CharField(max_length=10, choices=[("cat", "Cat"), ("dog", "Dog")])
    genre = models.CharField(max_length=200,
                             choices=[("adoption", "Adoption"), ("info", "Info"), ("training", "Training"),
                                      ("other", "Other")], default="other")
    link = models.CharField(max_length=2000, default=None)

    def __str__(self):
        return f'name: {self.name}\n type: {self.type}'
