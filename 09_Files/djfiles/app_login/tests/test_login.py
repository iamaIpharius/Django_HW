from django.test import TestCase
from django.urls import reverse


class AppLoginTest(TestCase):
    def test_main_page(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_account_page(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_edit_account_page(self):
        url = reverse('edit_account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)