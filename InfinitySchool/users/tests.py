from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegistrationForm
from users.models import User

class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:register')
        self.data = {
            'first_name': 'Oleg',
            'last_name': 'Ivanov',
            'username': 'Olezha',
            'email': 'oleg@mail.ru',
            'password1': 'OlezhaIvan123987',
            'password2': 'OlezhaIvan123987'
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], UserRegistrationForm)

    def test_user_registration_post_success(self):
        response = self.client.post(self.path, self.data)
        username = self.data['username']
        # self.assertFalse(User.objects.filter(username=username).exists())
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

