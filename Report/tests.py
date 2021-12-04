from django.test import TestCase


from .models import report


class ReportmodelTest():

    def setUpTestData():
        Report.objects.create(date='2-2-2021', name='topaz', text='saw a dog wondering')


