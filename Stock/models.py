from django.db import models


class stock(models.Model):
    item = models.CharField(max_length=100)  # the name of the item
    amount = models.DecimalField(max_digits=6,decimal_places=2)  # the quantity of the item

    def __str__(self):
        return self.item
