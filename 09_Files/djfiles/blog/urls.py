from django.urls import path
from blog.views import LoginView, LogoutView, register_view, account_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account')
]
