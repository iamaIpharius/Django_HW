from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(
        verbose_name='количество промотров', default=0)
    status = models.ForeignKey(
        'AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE, related_name='advertisements',
        verbose_name='Статус')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements',
                               verbose_name='Автор')

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone = models.IntegerField(max_length=100, verbose_name='Номер телефона')

class AdvertisementCategory(models.Model):
    pass