from django.test import TestCase, Client
from django.urls import reverse
from Taskboard.models import list_task


class TestViews(TestCase):
    def setup(self):
        self.client = Client()

    def test_all_task_GET(self):
        response = self.client.get(reverse('Taskboard:all_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskboard/all_task.html')

    def test_task_detail_GET(self):
        obj = list_task.objects.create(
                                       date='2021-11-10',
                                       name='name'
                                       )
        response = self.client.get(reverse('Taskboard:task_detail', args=[obj.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskboard/task_detail.html')
        self.assertTemplateUsed(response, 'adopter/Base.html')
