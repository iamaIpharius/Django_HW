from django.shortcuts import render
from django.http import HttpResponse


def advertisements_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisements_list.html', {})