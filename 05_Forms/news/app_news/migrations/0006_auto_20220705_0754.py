# Generated by Django 2.2 on 2022-07-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_auto_20220705_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='active',
            field=models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=False),
        ),
    ]
