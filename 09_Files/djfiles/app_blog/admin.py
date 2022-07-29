from django.contrib import admin
from .models import BlogEntry, Image


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

class ImageAdmin(admin.ModelAdmin):
    list_display = ['blog']

admin.site.register(BlogEntry, BlogAdmin)
admin.site.register(Image, ImageAdmin)