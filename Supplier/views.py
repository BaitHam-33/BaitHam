from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import SupplierRegistration
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
import xlwt

def export_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # creat a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    pdfmetrics.registerFont(TTFont('Tahoma', 'Tahoma.ttf'))
    textob.setFont("Tahoma", 14)

    suppliers = SupplierRegistration.objects.all()  # designate the model
    lines = []  # creat blank link

    for supplier in suppliers:
        lines.append('Supplier: ' + supplier.Supplier_name)
        lines.append('Owner: ' + supplier.owner_name)
        lines.append('Address: ' + supplier.address)
        lines.append('Phone number: ' + supplier.phone_number)
        lines.append('    ')
        lines.append('----------------------------------')
        lines.append('    ')



    textob.textLine("Suppliers report of the 'Bait Ham' association:")
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='suppliers.pdf')


def export_excel(request):
    response = HttpResponse(content_type='suppliers/excel')
    response['Content-Disposition'] = 'attachment; filename=suppliers' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('suppliers')  # give a name to the sheet
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write(0, 0, 'Suppliers report of the "Bait Ham" association:', font_style)

    columns = ['Supplier', 'Owner', 'Address','Phone number']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    rows = SupplierRegistration.objects.all().values_list('Supplier_name', 'owner_name', 'address','phone_number')

    font_style = xlwt.XFStyle()

    suppliers = SupplierRegistration.objects.all()


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    wb.save(response)

    return response
