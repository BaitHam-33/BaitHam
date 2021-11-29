from django.shortcuts import render

def animals(request):
    return render(request, 'Animal/animals.html')
