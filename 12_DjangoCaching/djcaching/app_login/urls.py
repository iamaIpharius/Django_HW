from django.urls import path, include
from .views import LoginView, LogoutView, register_view, account_view, account_edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('edit/', account_edit, name='edit_account'),
    path('i18n', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
