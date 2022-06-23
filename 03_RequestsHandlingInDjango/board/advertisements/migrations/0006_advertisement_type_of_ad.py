# Generated by Django 2.2 on 2022-06-20 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0005_advertisementtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='type_of_ad',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.AdvertisementType'),
        ),
    ]