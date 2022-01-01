from django.urls import reverse
from django.test import TestCase, Client
from volunteer.models import attendance
from volunteer.views import *
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('volunteer:loginuser')
        self.user = {
            'username': 'username',
            'password': 'password'}
        return super().setUp()


class LoginTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'volunteer/loginuser.html')

    def test_login_success(self):
        self.client.get(self.login_url, self.user, format='text/html')
        user = User.objects.filter(password=self.user['password'])
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cantlogin_with_no_username(self):
        response = self.client.post(self.login_url, {'password': 'vdjkfkv'}, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,302)

    def test_cantlogin_with_no_password(self):
        response = self.client.post(self.login_url, {'username': 'vjdkfvb'}, format='text/html')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code,302)
