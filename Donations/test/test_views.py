
from django.test import TestCase,Client
from django.urls import revers
from Taskboard.models import Project,Category,Expense
import json


class TestViews(TestCase):
    def setup(self):
        self.client=Client()
        self.submit_url= revers('submit')




    def test_submit_GET(self):
        response=self.client.get(self.submit_url)
        self.assertEquals(response.status_cod,200)
        self.assertTemplatUsed(response,'alldonates/index.html')

