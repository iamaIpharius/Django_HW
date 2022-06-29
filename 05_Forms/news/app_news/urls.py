from django.urls import path
from . import views
from .views import NewsListView, NewsDetailedView
from app_news.views import NewsFormView


urlpatterns = [
    path("news/", NewsListView.as_view()),
    path("news/<int:pk>", NewsDetailedView.as_view()),
    path("news/create", NewsFormView.as_view())
]
