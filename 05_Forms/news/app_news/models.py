from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    STATUS_CHOICES = [
        (True, 'Active'),
        (False, 'Inactive')
    ]
    title = models.CharField(max_length=1500, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(choices=STATUS_CHOICES, default=False)
    tag = models.ForeignKey('Tag', default=None, null=True, on_delete=models.CASCADE,
                            verbose_name='Тэг')

    class Meta:
        ordering = ['created_at']
        permissions = (('can_approve', 'Одобрение новости'),)

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.active}'


class Commentary(models.Model):
    DELETE_CHOICE = [('delete', 'Удалено администратором')]
    name = models.CharField(max_length=100, verbose_name='Имя')
    text = models.TextField(
        max_length=1000, verbose_name='Текст комментария', choices=DELETE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    related_news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                                     verbose_name='Новость')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name}, {self.created_at}, {self.text[:15]}'


class Tag(models.Model):
    name = models.CharField(max_length=36, verbose_name='Тэг')

    def __str__(self):
        return f'{self.name}'
