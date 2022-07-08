from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from app_login.forms import LoginForm, LogoutForm
from django.contrib.auth import logout
# Create your views here.


class LoginView(LoginView):
	template_name = "app_login/login.html"


class LogoutView(LogoutView):
	template_name = 'app_login/logout.html'

