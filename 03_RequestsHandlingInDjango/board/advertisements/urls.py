from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
]
