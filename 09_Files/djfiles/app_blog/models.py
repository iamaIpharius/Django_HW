from django.db import models
from django.contrib.auth.models import User

class BlogEntry(models.Model):

    title = models.CharField(max_length=1500, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    image = models.ImageField(upload_to='blog_images/')


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}, {self.created_at}'