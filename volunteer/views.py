from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

"""
def homeVolunteer(request):
    return render(request,'volunteer/homeVolunteer.html')"""

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('volunteer:loginuser')

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request,'volunteer/loginuser.html',{'form':AuthenticationForm(),'error':'username and password did not match'})
    else:
        form = AuthenticationForm(request)
        context = {'form': form}
    return render(request, 'volunteer/loginuser.html',context)
