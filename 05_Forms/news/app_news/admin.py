from django.contrib import admin
from app_news.models import News, Commentary

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass