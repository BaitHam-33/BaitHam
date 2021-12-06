from django.shortcuts import render, redirect

from Animal.forms import Add_Animal_Form
from .models import animal



def all_animals(request):
    animals = animal.objects.all()
    return render(request, 'Animal/all_animals.html', {'animals': animals})


def add_Animal(request):
    if request.method == 'GET':
        return render(request, 'Animal/add_Animal.html', {'form': Add_Animal_Form()})
    else:
        form = Add_Animal_Form(request.POST or None)
        context = { "form": form }
        if form.is_valid():
            context['form'] = Add_Animal_Form()
            new_animal = form.save()
            new_animal.save()
        else:
            print(form.errors) # incase of errors in validation
        return redirect('Animal:all_animals')

def Animal_detail(request, id=None):
    animal_obj = None
    if id is not None:
        animal_obj = animal.objects.get(id=id)
    context = {
        "object": animal_obj
    }
    return render(request, 'Animal/animal_detail.html', context=context)
