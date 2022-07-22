from django.contrib import admin
from .models import BlogEntry


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


admin.site.register(BlogEntry, BlogAdmin)
