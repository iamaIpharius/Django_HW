from django.contrib import admin
from app_news.models import News, Commentary, Tag


class CommentaryInLine(admin.TabularInline):
    model = Commentary


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'active']
    list_filter = ['active']
    inlines = [CommentaryInLine]

    actions = ['set_active', 'set_inactive']

    def set_active(self, request, queryset):
        queryset.update(active=True)

    def set_inactive(self, request, queryset):
        queryset.update(active=False)

    set_active.short_description = 'Make Active'
    set_inactive.short_description = 'Make Inactive'

class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['name', 
                    lambda x: x.text if len(x.text) < 15 else x.text[:15] + '...',
                    'created_at', 'related_news']

    list_filter = ['name']

    actions = ['delete_comment']

    def delete_comment(self, request, queryset):
        queryset.update(text='Удалено администратором')

    delete_comment.short_description = 'Удалить комментарий'


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']





admin.site.register(News, NewsAdmin)
admin.site.register(Commentary, CommentaryAdmin)
admin.site.register(Tag, TagAdmin)

