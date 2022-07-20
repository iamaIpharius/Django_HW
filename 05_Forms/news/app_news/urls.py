from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView
from app_news.views import NewsFormView, NewsEditFormView


urlpatterns = [
    path("", NewsListView.as_view()),
    path("<int:news_id>/", NewsDetailView.as_view()),
    path("create", NewsFormView.as_view()),
    path("<int:news_id>/edit", NewsEditFormView.as_view())
]
