from django.urls import path

from .views import all_animals, add_Animal, Animal_detail, editAnimal, deleteAnimal

app_name = 'Animal'

urlpatterns = [
    path('', all_animals, name='all_animals'),
    path('add_Animal/', add_Animal, name='add_Animal'),
    path('animal_detail/<int:id>', Animal_detail, name='animal_detail'),
    path('editAnimal/<str:id>', editAnimal, name='editAnimal'),
    path('deleteAnimal/<str:id>', deleteAnimal, name='deleteAnimal'),
]
