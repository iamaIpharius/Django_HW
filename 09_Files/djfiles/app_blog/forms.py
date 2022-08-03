from django import forms
from .models import BlogEntry


class BlogForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UploadForm(forms.Form):
    file = forms.FileField()