
from django.test import TestCase,Client
from django.urls import revers
from Taskboard.models import Project,Category,Expense
import json


class TestViews(TestCase):
    def setup(self):
        self.client=Client()
        self.all_task_url= revers('all_task')
        self.task_detail_url=revers('detail_url')



    def test_all_task_GET(self):
        response=self.client.get(self.all_task_url)
        self.assertEquals(response.status_cod,200)
        self.assertTemplatUsed(response,'Taskboard/all_task.html')

    def test_task_detail_GET(self):
        response = self.client.get(self.task_detail_url)
        self.assertEquals(response.status_cod, 200)
        self.assertTemplatUsed(response, 'Taskboard/task_detail.html')task_detail