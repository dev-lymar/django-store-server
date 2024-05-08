from http import HTTPStatus

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.test import TestCase
from django.urls import reverse

from .models import User


class BaseTestCase(TestCase):
    def setUp(self):
        self.social_app = SocialApp.objects.create(
            provider='github',
            name='Test Social App',
            client_id='test',
            secret='test',
        )
        self.social_app.sites.add(Site.objects.get_current())


class UserLoginViewTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.path = reverse('users:login')

    def test_user_login_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Autorization')
        self.assertTemplateUsed(response, 'users/login.html')


class UserRegistrationViewTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.data = {
            'first_name': 'testuser',
            'last_name': 'testuser',
            'username': 'testuser',
            'email': 'test@mail.com',
            'password1': 'Gfhjkm1234',
            'password2': 'Gfhjkm1234',
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Registration')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'A user with that username already exists.', html=True)


class UserProfileViewTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.test_user = User.objects.create_user(username='test_user', password='testpass1122')
        self.client.login(username='test_user', password='testpass1122')
        self.path = reverse('users:profile', args=[self.test_user.pk])

    def test_user_profile_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Profile')
        self.assertTemplateUsed(response, 'users/profile.html')
