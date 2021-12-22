from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import AttendanceForm


def logoutuser(request):
    """function for disconnecting the user from the system"""
    if request.method == 'POST':
        logout(request)
    return redirect('volunteer:loginuser')


def loginuser(request):
    """function for connecting the user to the system"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # check if the details is valid
            user = form.get_user()
            login(request, user)  # connect the user to the system
            return redirect('home')  # refer to the homepage
        else:
            # if the username or password are invalid, a message will appear accordingly
            return render(request, 'volunteer/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'username and password did not match'})
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
    return render(request, 'volunteer/loginuser.html', context)


def update(request):
    if request.method == 'GET':
        return render(request,'volunteer/update.html',{'form':AttendanceForm()})
    else:
        form=AttendanceForm(request.POST)
        new_attend=form.save(commit=False)
        new_attend.user=request.user
        new_attend.save()
        return redirect('home')
