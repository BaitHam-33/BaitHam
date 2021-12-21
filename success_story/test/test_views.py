
from django.test import TestCase,Client
from django.urls import revers
from success_story.models import story
import json


class TestViews(TestCase):
    def setup(self):
        self.client=Client()
        self.all_stories_url= revers('all_stories')
        self.create_story_url = revers('create_story')




    def test_all_stories_GET(self):
        response=self.client.get(self.all_stories_url)
        self.assertEquals(response.status_cod,200)
        self.assertTemplatUsed(response,'Tsuccess_story/all_stories.html')

