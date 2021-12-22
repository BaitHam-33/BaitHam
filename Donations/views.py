from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import Donations
from .forms import Donations_Form
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


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


def Thankyou(request):
    return render(request, 'Donations/Thankyou.html', {})


def submit(request):
    name = request.POST['name']
    credit = request.POST['credit']
    donates = Donations(name=name, credit=credit)
    donates.save()
    Donors = Donations.objects.all()
    return render(request, 'Donations/index.html', {'Donors': Donors})


def all_Donors(request):
    Donors = Donations.objects.all()
    if not Donors:
        Donors = {}
    return render(request, 'Donations/index.html', {'Donors': Donors})


def export_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # creat a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    pdfmetrics.registerFont(TTFont('Tahoma', 'Tahoma.ttf'))
    textob.setFont("Tahoma", 14)

    donations = Donations.objects.all()  # designate the model
    lines = []  # creat blank link
    sum = 0
    for donation in donations:
        sum += int(donation.amount)

    for donation in donations:
        lines.append('Donor name: ' + donation.name)
        lines.append('Donor ID: ' + donation.id_number)
        lines.append('Amount: ' + donation.amount + '₪')
        lines.append('    ')
        lines.append('----------------------------------')
        lines.append('    ')

    lines.append('Total:' + str(sum) + '₪')
    # loop
    textob.textLine("Revenue report of the 'Bait Ham' association:")
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='donations.pdf')


def export_excel(request):
    response = HttpResponse(content_type='donations/excel')
    response['Content-Disposition'] = 'attachment; filename=donations' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('donations')  # give a name to the sheet
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write(0, 0, 'Revenue report of the "Bait Ham" association:', font_style)

    columns = ['Name', 'ID Number', 'Amount']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    rows = Donations.objects.all().values_list('name', 'id_number', 'amount')

    font_style = xlwt.XFStyle()

    donations = Donations.objects.all()
    sum = 0
    for donation in donations:
        sum += int(donation.amount)

    count = 0
    for donation in donations:
        count += 1

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ws.write(count + 3, 1, 'Total:', font_style)
    ws.write(count + 3, 2, str(sum) + '₪', font_style)

    wb.save(response)

    return response
