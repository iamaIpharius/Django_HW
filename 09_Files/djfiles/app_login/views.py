from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from app_login.forms import LoginForm, LogoutForm, RegisterForm, ChangeForm, ChangeProfileForm
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
            about = form.cleaned_data.get('about')
            Profile.objects.create(user=user, city=city,
                                   date_of_birth=date_of_birth,
                                   about=about)
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
        about = request.user.profile.about
        return render(request, 'app_login/account.html',
                      {'username': usermane,
                       'first_name': first_name,
                       'last_name': last_name,
                       'city': city,
                       'about': about})
    else:
        answer = 'Вы не авторизованы'
        return render(request, 'app_login/account.html', {'answer': answer})

def account_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            
            form = ChangeForm(request.POST, instance=request.user)
            profile_form = ChangeProfileForm(request.POST, instance=request.user.profile)

            if form.is_valid() and profile_form.is_valid():
                user = form.save()
                profile_form.save()

                return redirect('/account/')
        else:
            form = ChangeForm(instance=request.user)
            profile_form = ChangeProfileForm(instance=request.user.profile)
        return render(request, 'app_login/edit.html', {'form': form, 'profile_form': profile_form})


    else:
        answer = 'Вы не авторизованы'
        return render(request, 'app_login/account.html', {'answer': answer})
