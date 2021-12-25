from django.shortcuts import render, redirect
from Animal.forms import Add_Animal_Form
from .models import animal, Stats
from .filters import animalFilter
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt

def all_animals(request):
    if request.user.is_authenticated:
        animals = animal.objects.all()
    else:
        animals = animal.objects.filter(Adoption='Y')

    myfilter = animalFilter(request.GET, queryset=animals)
    animals = myfilter.qs
    context = {'animals': animals, 'myfilter': myfilter}

    return render(request, 'Animal/all_animals.html', context)


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
            stat = Stats.objects.last()
            stat.created += 1
            stat.current = animal.objects.count()
            stat.save()
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
            animal_obj.image.delete()
        animal_obj.delete()

        stat = Stats.objects.last()
        stat.deleted += 1
        stat.current = animal.objects.count()
        stat.save()
        return redirect('Animal:all_animals')

    context = {'animal': animal_obj}
    return render(requset, 'Animal/DeleteAnimal.html', context)

def export_pdf(request):
    """Function for exporting a pdf document from the system"""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)  # creat a new page
    textob = c.beginText()  # creat a text object
    textob.setTextOrigin(inch, inch)  # set the sizes of the text
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)  # set the font of the text

    stats = Stats.objects.all()  # designate the model
    lines = []  # creat a new list for the objects

    # print all data we need
    for stat in stats:
        lines.append('Month number:' + str(stat.month))
        lines.append('Entered the hoard: ' + str(stat.created))
        lines.append('Current amount: ' + str(stat.current))
        lines.append('Animals adopted: ' + str(stat.deleted))
        lines.append('    ')
        lines.append('_______________________________________')
        lines.append('    ')

    textob.textLine("Association Status Report (Changes in Quantities) for 2021")  # the title of the file
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()  # save the file
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='status.pdf')


def export_excel(request):
    """Function for exporting an excel document from the system"""
    response = HttpResponse(content_type='status/excel')
    response['Content-Disposition'] = 'attachment; filename=status' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('status')  # give a name to the sheet
    row_num = 2  # initial row for objects
    font_style = xlwt.XFStyle()  # set the font of the text
    font_style.font.bold = True

    ws.write(0, 0, 'Association Status Report (Changes in Quantities) for 2021', font_style)  # the title of the file

    columns = ['Month number', 'Entered the hoard', 'Current amount', 'Animals adopted']  # the columns in the table

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # save all the data we need from database
    rows = Stats.objects.all().values_list('month', 'created', 'current', 'deleted')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)  # enter all the data to the table

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)  # save the file

    return response
