from django.db import models

class Donations(models.Model):
    name = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)

    def __str__(self):
        return f"Name:{self.name} Credit:{self.credit}"
