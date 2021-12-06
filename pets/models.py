# from django.db import models
#
#
# class pets(models.Model):
#     Sex_Choice = [('M', 'Male'), ('F', 'Female')]
#     Species_choice = [('dog', 'Dog'), ('cat', 'Cat')]
#     name = models.CharField(max_length=100)  # Name of the Pet
#     submitter = models.CharField(max_length=100)  # Name of Submitter
#     species = models.CharField(max_length=30, choices=Species_choice,blank=False)  # What is the Pet species? (dog, cat)
#     breed = models.CharField(max_length=30, blank=True)  # Pet's breed (can leave empty)
#     description = models.TextField(blank=True)  # Description like where was found etc...
#     sex = models.CharField(max_length=1, choices=Sex_Choice, blank=True)  # Gender (can leave empty)
#     submission_date = models.DateTimeField()  # Date submitted to shelter
#     vaccinations = models.ManyToManyField('Vaccine', blank=True)  # What vaccination it received
#
#
#     def __str__(self):
#         return self.name, self.species
#
#
# class Vaccine(models.Model):
#     name = models.CharField(max_length=50)  # Name of Vaccination
#
#     def __str__(self):
#         return self.name
