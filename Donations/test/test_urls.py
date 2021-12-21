from django.test import SimpleTestCase
from django.urls import revers,resolve
from success_story.views import new,Thankyou,submit,all_Donors

class TestUrls(SimpleTestCase):

     def test_new_url_is_resolved(self):
       url = revers('new')
       self.assertEquals(resolve(url).func,new)

     def test_Thankyou_url_is_resolved(self):
         url = revers('Thankyou')
         self.assertEquals(resolve(url).func, Thankyou)

     def test_submit_url_is_resolved(self):
         url = revers('submit')
         self.assertEquals(resolve(url).func, submit)

     def test_all_Donors_url_is_resolved(self):
         url = revers('all_Donors')
         self.assertEquals(resolve(url).func, all_Donors)
