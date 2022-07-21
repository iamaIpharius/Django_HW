from django.urls import path
from app_login.views import LoginView, LogoutView, register_view, account_view, account_edit


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('edit/', account_edit, name='account'),
]
