from django.db import models

class Donations(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    credit_number = models.CharField(max_length=100)
    cvc = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.amount}"
