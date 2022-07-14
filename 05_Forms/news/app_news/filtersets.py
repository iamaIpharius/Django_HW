import django_filters
from app_news.models import News


class NewsFilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = ['tag', 'created_at']
