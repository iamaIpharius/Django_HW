from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import logout, login, authenticate

from blog.forms import LoginForm, LogoutForm, RegisterForm
from blog.models import Profile

# Create your views here.
class LoginView(LoginView):
    template_name = "blog/login.html"


class LogoutView(LogoutView):
    template_name = 'blog/logout.html'


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def account_view(request):
    if request.user.is_authenticated:
        usermane = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        print(request.user.profile)
        about = request.user.profile.about
        return render(request, 'app_login/account.html',
                      {'username': usermane,
                       'first_name': first_name,
                       'last_name': last_name,
                       'about': about,
                       })
    else:
        answer = 'Вы не авторизованы'
        return render(request, 'blog/account.html', {'answer': answer})