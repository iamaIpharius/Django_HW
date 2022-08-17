from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import LoginForm, LogoutForm, RegisterForm, ChangeForm
from .models import Profile
from django.contrib.auth import logout, login, authenticate
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache


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
            Profile.objects.create(user=user, sales='none', proposals={'good': '', 'price': 0},
                                   history={'purchase': ['good', 'price', 'date']})
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'app_login/register.html', {'form': form})


def account_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name

        sales_cache_key = f'sales:{username}'
        proposals_cache_key = f"proposals:{username}"
        sales = request.user.profile.sales
        proposals = request.user.profile.proposals

        cache.get_or_set(sales_cache_key, sales, 30*60)
        cache.get_or_set(proposals_cache_key, proposals, 30 * 60)

        balance = request.user.profile.balance

        history = request.user.profile.history
        return render(request, 'app_login/account.html',
                      {'username': username,
                       'first_name': first_name,
                       'last_name': last_name,
                       'sales': sales,
                       'balance': balance,
                       'proposals': proposals,
                       'history': history,
                       })
    else:
        answer = _("You're not authorized")
        return render(request, 'app_login/account.html', {'answer': answer})


def account_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = ChangeForm(request.POST, instance=request.user)

            if form.is_valid():
                user = form.save()

                return redirect('/account/')
        else:
            form = ChangeForm(instance=request.user)
        return render(request, 'app_login/edit.html', {'form': form})


    else:
        answer = _("You're not authorized")
        return render(request, 'app_login/account.html', {'answer': answer})
