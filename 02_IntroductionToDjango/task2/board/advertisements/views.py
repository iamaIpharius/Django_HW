from django.shortcuts import render
from django.http import HttpResponse


def advertisements_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisements_list.html', {})


def java_page(request, *args, **kwargs):
    return render(request, 'advertisements/Java.html', {})


def js_page(request, *args, **kwargs):
    return render(request, 'advertisements/JS.html', {})


def kotlin_page(request, *args, **kwargs):
    return render(request, 'advertisements/Kotlin.html', {})


def php_page(request, *args, **kwargs):
    return render(request, 'advertisements/PHP.html', {})


def python_page(request, *args, **kwargs):
    return render(request, 'advertisements/Python.html', {})


def web_page(request, *args, **kwargs):
    return render(request, 'advertisements/WEB.html', {})
