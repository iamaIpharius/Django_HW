# Generated by Django 4.0.6 on 2022-07-15 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_auto_20220714_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
