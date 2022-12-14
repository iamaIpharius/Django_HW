# Generated by Django 4.0.6 on 2022-07-26 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='blogentry',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
