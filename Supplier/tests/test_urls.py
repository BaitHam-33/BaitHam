from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Taskboard.views import export_pdf, export_excel


class TestUrls(SimpleTestCase):
    def test_export_pdf_url_resolves(self):
        url = reverse(' export_pdf')
        self.assertEquals(resolve(url).func.view_class,export_pdf)

    def test_export_excel_url_resolves(self):
        url = reverse('  export_excel')
        self.assertEquals(resolve(url).func.view_class, export_excel)
