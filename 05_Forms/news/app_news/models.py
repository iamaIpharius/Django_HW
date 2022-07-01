from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Commentary(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    text = models.TextField(max_length=1000, verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)
    related_news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                                     verbose_name='Новость')
    class Meta:
        ordering = ['created_at']
