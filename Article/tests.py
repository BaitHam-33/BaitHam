from django.test import TestCase

from django.test import RequestFactory, TestCase

import Report
import success_story
from adopter.views import home


def __str__(self):
    return '%s' % (self.name)

def test_home(self):
    request = self.factory.get('home')
    response = home(request)
    self.assertEqual(response.status_code, 200)
    self.assertNotEqual(response.status_code, 404)

def test_setUp(self):
    Report.objects.create(date='2-2-2021', name='topaz', text='saw a dog wondering')
    success_story.objects.create(name='david',date='1-10-2020',text='david love cats')

