from django.contrib import admin
from app_news.models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass