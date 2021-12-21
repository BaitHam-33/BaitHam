from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Donations
import jeson

class TestViews(TestCase):
    class TestViews(TestCase):
        def test_all_Donors_GET(self):
            client = Client()
            response = client.get(reverse('Donors'))
            self.assertEquals(respons.status_code,200)
            self.assertTemplateeUsed(response,'budget/index.html')



