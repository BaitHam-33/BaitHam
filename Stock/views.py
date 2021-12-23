from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import stock
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
    pdfmetrics.registerFont(TTFont('David', 'David.ttf'))
    textob.setFont("David", 14)

    stocks = stock.objects.all()  # designate the model
    lines = []  # creat blank link

    for st in stocks:
        lines.append('Item: ' + st.item)
        lines.append('Amount: ' + str(st.amount))
        lines.append('_______________________________________')


    textob.textLine("Stock report of the 'Bait Ham' association:")
    textob.textLine("    ")
    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='stock.pdf')


def export_excel(request):
    response = HttpResponse(content_type='stock/excel')
    response['Content-Disposition'] = 'attachment; filename=stock' + str(datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('stock')  # give a name to the sheet
    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    ws.write(0, 0, 'Stock report of the "Bait Ham" association:', font_style)

    columns = ['Item', 'Amount']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    rows = stock.objects.all().values_list('item', 'amount')

    font_style = xlwt.XFStyle()


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    font_style = xlwt.XFStyle()
    font_style.font.bold = True


    wb.save(response)

    return response
