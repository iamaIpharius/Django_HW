import os.path

from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

c = Client()

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='testuser2', first_name='john2', last_name='pongo',
                                    password='fiuhsdufhsd22')
        Profile.objects.create(user=test_user, balance=0, sales='', proposals='', history='')

    def test_main_page(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_register_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_login/register.html')

        response = c.post('/register/',
                          {'username': 'testuser',
                           'first_name': 'john',
                           'last_name': 'johnson',
                           'password1': 'jignjdshuu2133',
                           'password2': 'jignjdshuu2133'}, follow=True)
        print(response.redirect_chain)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_login/login.html')

        pongo = User.objects.get(last_name='pongo')
        c.force_login(pongo)
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_login/logout.html')

    def test_account_page(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_login/account.html')

        pongo = User.objects.get(last_name='pongo')
        c.force_login(pongo)
        response = c.get('/account/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, pongo.username)

    def test_edit_account_page(self):
        url = reverse('edit_account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)