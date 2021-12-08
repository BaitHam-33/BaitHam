from django.shortcuts import render
from django.http import HttpResponse
from .models import Donations

def donates_from(request):
    return render(request,'donates/index.html',{})


def submit(request):
    name=request.POST['name']
    credit=request.POST['credit']
    donates=Donations(name=name,credit=credit)
    donates.save()
    Donors=Donations.object.all()
    return render(request,'alldonates/index.html',{'Donors':Donors})


def all_Donors(request):
    Donors = Donations.object.all()
    if not Donors:
        Donors={}
    return render(request,'alldonates/index.html',{'Donors':Donors})