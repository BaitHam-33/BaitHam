from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Taskboard.views import export_pdf, export_excel


class TestUrls(SimpleTestCase):
    def test_export_pdf_url_is_resolved(self):
        url = reverse(' export_pdf')
        print(resolve(url))
