# Generated by Django 2.2 on 2022-06-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_auto_20220620_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
    ]
