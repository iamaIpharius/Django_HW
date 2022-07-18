import django_filters
from django import forms
from app_news.models import News


class NewsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(filed_name='date', widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}), lookup_expr='exact', label='Date')

    class Meta:
        model = News
        fields = ['tag', 'date']
