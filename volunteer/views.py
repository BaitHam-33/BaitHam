from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "volunteer/loginuser.html", context)


    # if request.method == 'GET':
    #     return render(request, 'volunteer/loginuser.html', {'form': AuthenticationForm()})
