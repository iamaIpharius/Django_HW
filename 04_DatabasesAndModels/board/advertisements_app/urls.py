from django.urls import path
from . import views
from .views import AdvertisementListView


urlpatterns = [
    path('advertisements/', AdvertisementListView.as_view(), name='advertisement'),
]
