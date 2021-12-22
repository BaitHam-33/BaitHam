from django.test import SimpleTestCase
from django.urls import revers,resolve
from Taskboard.views import all_task,task_detail

class TestUrls(SimpleTestCase):

     def test_all_task_url_is_resolved(self):
       url = revers('all_task')
       self.assertEquals(resolve(url).func,all_task)

     def test_task_detail_url_is_resolved(self):
         url = revers('task_detail')
         self.assertEquals(resolve(url).func, task_detail)


