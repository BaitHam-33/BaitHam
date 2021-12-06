# from django.shortcuts import render, redirect
# from animal.forms import add_pet_Form
# from .models import pets
#
#
# def all_Pets(request):
#     pet_obj = pets.objects.all()
#     return render(request, 'pets/all_Pets.html', {'pets': pet_obj})
#
# def add_pet_view(request):
#     if request.method == 'GET':
#         return render(request, 'pets/add_Animal.html', {'form': add_pet_Form()})
#     else:
#         form = add_pet_Form(request.POST)
#         new_animal = form.save(commit=False)
#         new_animal.save()
#         return redirect('pets:all_Pets')

