from django.urls import path
from .views import BlogListView, BlogFormView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogFormView.as_view(), name='create'),
]
