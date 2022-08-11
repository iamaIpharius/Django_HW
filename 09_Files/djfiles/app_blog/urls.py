from django.urls import path, include
from .views import BlogListView, BlogFormView, BlogDeatailView, upload_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogFormView.as_view(), name='create'),
    path("blog/<int:blogentry_id>/", BlogDeatailView.as_view(), name='blog_detail'),
    path("blog/upload/", upload_posts, name='upload'),
    path('i18n', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
