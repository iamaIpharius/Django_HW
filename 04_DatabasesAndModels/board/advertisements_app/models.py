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
    category = models.ForeignKey('AdvertisementCategory', default=None, null=True,
                                  on_delete=models.CASCADE, related_name='advertisements', verbose_name='Категория')

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']
        
    def __str__(self):
        return self.title


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    phone = models.IntegerField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name



class AdvertisementForm(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()