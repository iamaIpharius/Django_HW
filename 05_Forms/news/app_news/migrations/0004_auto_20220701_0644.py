# Generated by Django 2.2 on 2022-07-01 06:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_auto_20220629_0848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentary',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='commentary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='commentary',
            name='related_news',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.News', verbose_name='Новость'),
        ),
    ]
