from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import AttendanceForm
from .models import attendance
from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt


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
        return render(request, 'volunteer/update.html', {'form': AttendanceForm()})
    else:
        form = AttendanceForm(request.POST)
        new_attend = form.save(commit=False)
        new_attend.user = request.user
        new_attend.save()
        return redirect('home')


def export_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # creat a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)

    Attendance = attendance.objects.filter(user=request.user)  # designate the model

    lines = []  # creat blank link
    for obj in Attendance:
        lines.append('Date: ' + str(obj.date))
        lines.append('Entrance time: ' + str(obj.entrance_time))
        lines.append('Leaving time ' + str(obj.leaving_time))
        lines.append('_____________________________________________')
        lines.append('    ')

    name = request.user.first_name
    textob.textLine("Attendance report for last month, for the volunteer: " + name)
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='attendance.pdf')


def export_excel(request):
    response = HttpResponse(content_type='attendance/excel')
    response['Content-Disposition'] = 'attachment; filename=attendance' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('attendance')  # give a name to the sheet
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    name = request.user.first_name
    ws.write(0, 0, 'Attendance report for last month, for the volunteer: '+name, font_style)

    columns = ['Date', 'Entrance time', 'Leaving time']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    rows = attendance.objects.filter(user=request.user).values_list('date', 'entrance_time', 'leaving_time')

    font_style = xlwt.XFStyle()

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    wb.save(response)

    return response
