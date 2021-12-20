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
        form = Add_Animal_Form(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            submitter = form.cleaned_data.get("submitter")
            species = form.cleaned_data.get("species")
            breed = form.cleaned_data.get("breed")
            description = form.cleaned_data.get("description")
            sex = form.cleaned_data.get("sex")
            Adoption = form.cleaned_data.get("Adoption")
            submission_date = form.cleaned_data.get("submission_date")
            image = form.cleaned_data.get("image")
            obj = animal.objects.create(
                name=name,
                submitter=submitter,
                species=species,
                breed=breed,
                description=description,
                sex=sex,
                Adoption=Adoption,
                submission_date=submission_date,
                image=image
            )
            obj.save()
        else:
            print(form.errors)  # in case of errors in validation
        return redirect('Animal:all_animals')


def Animal_detail(request, id):
    animal_obj = None
    if id is not None:
        animal_obj = animal.objects.get(id=id)
    context = {"object": animal_obj}
    return render(request, 'Animal/animal_detail.html', context=context)


def editAnimal(request, id=None):
    if id is not None:
        animal_up = animal.objects.get(id=id)
        form = Add_Animal_Form(instance=animal_up)
        if request.method == 'POST':
            form = Add_Animal_Form(request.POST, request.FILES, instance=animal_up)
            if form.is_valid():
                form.save()
                return redirect('Animal:all_animals')
        context = {"form": form}
        return render(request, 'Animal/add_Animal.html', context=context)

    return redirect('Animal:all_animals')


def deleteAnimal(requset, id):
    animal_obj = animal.objects.get(id=id)
    if requset.method == 'POST':
        if animal_obj.image and animal_obj.image != 'default.png':
            print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            animal_obj.image.delete()
        animal_obj.delete()
        return redirect('Animal:all_animals')

    context = {'animal': animal_obj}
    return render(requset, 'Animal/DeleteAnimal.html', context)
