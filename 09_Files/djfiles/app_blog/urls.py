from django.urls import path
from .views import BlogListView, BlogFormView, BlogDeatailView, upload_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogFormView.as_view(), name='create'),
    path("<int:pk>/", BlogDeatailView.as_view()),
    path("upload/", upload_posts, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
