from django import forms
from app_news.models import News, Commentary


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class CommentaryForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField()

class CommentaryAuthForm(forms.Form):
    text = forms.CharField()