from django.db import models
from django.utils import timezone


class animal(models.Model):
    Sex_Choice = [('M', 'Male'), ('F', 'Female')]
    Species_choice = [('dog', 'Dog'), ('cat', 'Cat')]
    Adoption_ready = [('N', 'No'), ('Y', 'Yes')]
    name = models.CharField(max_length=100, verbose_name="שם")  # Name of the Pet
    submitter = models.CharField(max_length=100, null=True, verbose_name="הוכנס על ידי")  # Name of Submitter
    species = models.CharField(max_length=30, choices=Species_choice, blank=False,
                               default='Dog' , verbose_name="סוג")  # What is the Pet species? (dog, cat)
    breed = models.CharField(max_length=30, blank=True, verbose_name="גזע")  # Pet's breed (can leave empty)
    description = models.TextField(blank=True, verbose_name="תיאור")  # Description like where was found etc...
    sex = models.CharField(max_length=30, choices=Sex_Choice, blank=True, verbose_name="מין")  # Gender (can leave empty)
    submission_date = models.DateTimeField(default=timezone.now,verbose_name="תאריך קליטה")  # Date submitted to shelter
    image = models.ImageField(upload_to='Animal', blank=True, default='default.png', verbose_name="העלאת תמונה")  # for animal images
    Adoption = models.CharField(max_length=30, choices=Adoption_ready, blank=False, default='No',verbose_name="מוכן לאימוץ")

    def __str__(self):
        return self.name
