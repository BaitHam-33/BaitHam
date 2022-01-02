from django.urls import reverse
from django.test import TestCase, Client
from forum.models import forum


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = forum.objects.create( name='avigail',
                                         email='avigails90@gmail.com',
                                         topic='test',
                                         description='help my',)

    def test_home_GET(self):
        response = self.client.get(reverse('forum:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'forum/home.html')

    def test_addInForum_POST_Valid(self):
        forumcount = forum.objects.count()
        response = self.client.post(reverse('forum:addInForum'), { 'name':'avigail',
                                                                   'email':'avigails90@gmail.com',
                                                                   'topic':'test',
                                                                   'description':'help my',})


        self.assertEqual(response.status_code, 302)




    def test_addInForum_POST_NOT_Valid(self):
        response = self.client.post(reverse('forum:addInForum'), { 'name':'',
                                                                   'email':'',
                                                                   'topic':'',
                                                                   'description':''})


        self.assertEqual(response.status_code, 200)
