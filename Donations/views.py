from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Donations
from .forms import Donations_Form


def donates_form(request):
    if request.method == 'GET':
        return render(request, 'Donations/index.html', {'form': Donations_Form()})
    else:
        form = Donations_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            id_number = form.cleaned_data.get("id_number")
            credit_number = form.cleaned_data.get("credit_number")
            cvc = form.cleaned_data.get("cvc")
            amount = form.cleaned_data.get("amount")

            obj = Donations.objects.create(
                name=name,
                id_number=id_number,
                credit_number=credit_number,
                cvc=cvc,
                amount=amount,
            )
            obj.save()
        else:
            print(form.errors)  # in case of errors in validation
        return redirect('Donations:Thankyou')

    return render(request, 'Donations/index.html', {})

def Thankyou(request):
    return render(request, 'Donations/Thankyou.html', {})


def submit(request):
    name = request.POST['name']
    credit = request.POST['credit']
    donates = Donations(name=name, credit=credit)
    donates.save()
    Donors = Donations.object.all()
    return render(request, 'alldonates/index.html', {'Donors': Donors})


def all_Donors(request):
    Donors = Donations.object.all()
    if not Donors:
        Donors = {}
    return render(request, 'alldonates/index.html', {'Donors': Donors})
