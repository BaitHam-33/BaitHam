from django.urls import reverse
from django.test import TestCase, Client
from volunteer.models import attendance
from volunteer.views import *

class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('volunteer:loginuser')
        self.user = {
            'username': 'username',
            'password': 'password' }
        return super().setUp()

class LoginTest(BaseTest):
    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
