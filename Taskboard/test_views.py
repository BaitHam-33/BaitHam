from django.test import TestCase, Client
from django.urls import reverse
from budget.models import list_task,task
import jeson

class TestViews(TestCase):
    def setup(self):
        self.client =Client()
        self.all_task_url = reverse('all_task')
        seslf.task_detail_url=reverse('task_detail')
    def test_all_task_GET(self):
        response = self.client.get(reverse('task'))
        self.assertEquals(respons.status_code,200)
        self.assertTemplateeUsed(response,'budget/all_task.html')

    def test_task_detail_GET(self):
        response = self.client.get(reverse('task_detail_url'))
        self.assertEquals(respons.status_code, 200)
        self.assertTemplateeUsed(response, 'budget/task_detail.html')
