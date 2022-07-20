from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=1500)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(
        verbose_name='количество промотров', default=0)
    status = models.ForeignKey(
        'AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE, related_name='advertisements')
    type_of_ad = models.ForeignKey(
        'AdvertisementType', default=None, null=True, on_delete=models.CASCADE, related_name='advertisements'
    )
    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


class AdvertisementType(models.Model):
    type_name = models.CharField(max_length=100)
