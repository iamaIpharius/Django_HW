# Generated by Django 2.2 on 2022-07-14 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0008_commentary_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at'], 'permissions': (('can_approve', 'Одобрение новости'),)},
        ),
    ]