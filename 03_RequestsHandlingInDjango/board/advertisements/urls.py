from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    # path('advertisements/', views.Advertisements.as_view()),
    path('advertisements/', views.advertisements_list, name='advertisements_list'),
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
]
