from django import forms
from .models import BlogEntry


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = '__all__'
