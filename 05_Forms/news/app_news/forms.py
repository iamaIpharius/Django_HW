from django import forms
from app_news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
