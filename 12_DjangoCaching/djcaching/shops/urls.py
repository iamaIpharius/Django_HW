from django.urls import path, include
from .views import ShopsListView

urlpatterns = [
    path('shops/', ShopsListView.as_view(), name='shops'),
]