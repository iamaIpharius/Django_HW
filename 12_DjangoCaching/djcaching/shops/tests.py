import os.path

from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Shop
from app_login.models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

c = Client()

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='testuser2', first_name='john2', last_name='pongo',
                                    password='fiuhsdufhsd22')
        Profile.objects.create(user=test_user, balance=0, sales='', proposals='', history='')

    def test_blog_list(self):
        url = reverse('shops')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/shops_list.html')