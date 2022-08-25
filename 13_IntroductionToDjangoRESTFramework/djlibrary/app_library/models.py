from django.db import models


class Author(models.Model):
    """ Модель Автор """
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=50, verbose_name='last name')
    birth_year = models.DateField(verbose_name='birth year')


class Book(models.Model):
    """ Модель Книга """
    title = models.CharField(max_length=50, verbose_name='title')
    isbn = models.IntegerField(max_length=30, verbose_name='isbn')
    year = models.DateField(verbose_name='year')
    pages = models.IntegerField(verbose_name='pages')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='author')
