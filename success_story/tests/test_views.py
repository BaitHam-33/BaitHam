from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setup(self):
        self.client = Client()
        self.create_story_url = reverse('success_story:create_story')

    def test_all_stories_GET(self):
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')
