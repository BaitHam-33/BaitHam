from django.urls import reverse
from django.test import TestCase, Client
from Report.models import report


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = report.objects.create(id=1,
                                        name='report number 1',
                                        date='2021-11-24',
                                        text='help the dog!')

    def test_all_reports_GET(self):
        response = self.client.get(reverse('Report:all_reports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Report/all_reports.html')


    def test_create_report_GET(self):
        response = self.client.get(reverse('Report:createReport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Report/createReport.html')

    def test_create_report_POST_Valid(self):
        report_count = report.objects.count()
        response = self.client.post(reverse('Report:createReport'), {'name': 'report number 1',
                                                                   'date': '2021-11-24',
                                                                   'text': 'help the dog!'})

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(report.objects.count(), report_count+1)  # all fields are in place

    def test_create_report_POST_Not_Valid(self):
        response = self.client.post(reverse('Report:createReport'),
                                                        {'name': 'report number 1',
                                                         'date': '2021-11-24',
                                                         'text': 'help the dog!'})
        self.assertEqual(response.status_code, 302)  # means redirection works in case of a bad form

    def test_delete_report_GET(self):
        response = self.client.get(reverse('Report:deleteReport', args=[1]))
        self.assertEqual(response.status_code, 302)


    def test_delete_report_POST(self):
        report_count = report.objects.count()
        response = self.client.get(reverse('Report:deleteReport', args=[1]), {'name': 'report number 1',
                                                                             'date': '2021-11-24',
                                                                             'text': 'help the dog!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(report.objects.count(), report_count-1)
