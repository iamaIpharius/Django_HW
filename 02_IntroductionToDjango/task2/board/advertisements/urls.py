from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisements_list, name='advertisements_list'),
    path("Java/", views.java_page, name='java_page'),
    path("JS/", views.js_page, name='js_page'),
    path("Kotlin/", views.kotlin_page, name='kotlin_page'),
    path("PHP/", views.php_page, name='php_page'),
    path("Python/", views.python_page, name='python_page'),
    path("WEB/", views.web_page, name='web_page')
]