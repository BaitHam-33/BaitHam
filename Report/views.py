from django.shortcuts import render, redirect
from .models import report
from .forms import ReportForm


def createReport(request):
    if request.method == 'GET':
        return render(request, 'Report/createReport.html', {'form': ReportForm()})
    else:
        form = ReportForm(request.POST)
        new_report = form.save(commit=False)
        new_report.save()
        return redirect('Report:all_reports')


def all_reports(request):
    reports = report.objects.order_by('-date')
    return render(request, 'Report/all_reports.html', {'reports': reports})


