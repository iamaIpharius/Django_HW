import os.path

from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from app_login.models import Profile
from app_blog.models import BlogEntry, Image
from django.core.files.uploadedfile import SimpleUploadedFile

c = Client()
BLOGS = 10


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pongo = User.objects.create(username='testuser2', first_name='john2', last_name='pongo',
                                    password='fiuhsdufhsd22')
        Profile.objects.create(user=pongo, city='london', date_of_birth='1991-11-11', about='test pongo')

        for blog in range(BLOGS):
            BlogEntry.objects.create(title=f'{blog} title', content=f'{blog} content', user=pongo)

    def test_blog_list(self):
        url = reverse('blog')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/blog_list.html')

        response = c.get('/blog/')
        self.assertTrue(len(response.context['blog_list']) == BLOGS)

    def test_blog_detail(self):
        blogs = BlogEntry.objects.all()
        for blog in blogs:
            response = c.get(f'/blog/{blog.id}/')
            self.assertTemplateUsed(response, 'app_blog/blog_detail.html')

    def test_blog_create(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/create.html')

        create = c.post(url, title='something', content='somethingsomething', follow=True)
        self.assertEqual(create.status_code, 200)

    def test_blog_upload(self):
        url = reverse('upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/upload.html')

        # file = SimpleUploadedFile('media/blogs.csv', b'file_content', content_type='csv')
        file = os.path.abspath('C:\PROJECTS\Django_HW\python_django\09_Files\djfiles\media\blogs.csv')
        upload = c.post(url, {'file': file})
        self.assertEqual(upload.status_code, 200)

    def test_blog_create_with_images(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_blog/create.html')

        create = c.post(url, title='something', content='somethingsomething', image='media/blog_images/cat.jpg',
                        follow=True)
        self.assertEqual(create.status_code, 200)
