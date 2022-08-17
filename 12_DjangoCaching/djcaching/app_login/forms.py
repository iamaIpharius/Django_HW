from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class LogoutForm(forms.Form):
    pass


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Фамилия')
    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')

class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name')

