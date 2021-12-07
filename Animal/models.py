from datetime import date
from django.db import models


class animal(models.Model):
    Sex_Choice = [('M', 'Male'), ('F', 'Female')]
    Species_choice = [('dog', 'Dog'), ('cat', 'Cat')]
    name = models.CharField(max_length=100)  # Name of the Pet
    submitter = models.CharField(max_length=100, null=True)  # Name of Submitter
    species = models.CharField(max_length=30, choices=Species_choice, blank=False, default='Dog')  # What is the Pet species? (dog, cat)
    breed = models.CharField(max_length=30, blank=True)  # Pet's breed (can leave empty)
    description = models.TextField(blank=True)  # Description like where was found etc...
    sex = models.CharField(max_length= 30 ,choices=Sex_Choice, blank=True)  # Gender (can leave empty)
    submission_date = models.DateTimeField(default=date.today)  # Date submitted to shelter
    image = models.ImageField(upload_to='media/Animal', blank=True) # for animal images

    def __str__(self):
        return self.name

