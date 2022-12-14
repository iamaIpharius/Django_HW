from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from app_login.forms import LoginForm, LogoutForm, RegisterForm
from app_login.models import Profile
from django.contrib.auth import logout, login, authenticate

# Create your views here.


class LoginView(LoginView):
    template_name = "app_login/login.html"


class LogoutView(LogoutView):
    template_name = 'app_login/logout.html'


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(user=user, city=city,
                                   date_of_birth=date_of_birth,
                                   news_published=0,
                                   verification=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_login/register.html', {'form': form})


def account_view(request):
    if request.user.is_authenticated:
        usermane = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        print(request.user.profile)
        city = request.user.profile.city
        news_published = request.user.profile.news_published
        verification = request.user.profile.verification
        return render(request, 'app_login/account.html',
                      {'username': usermane,
                       'first_name': first_name,
                       'last_name': last_name,
                       'city': city,
                       'news_published': news_published,
                       'verification': verification})
    else:
        answer = '???? ???? ????????????????????????'
        return render(request, 'app_login/account.html', {'answer': answer})
