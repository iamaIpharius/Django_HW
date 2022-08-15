from django.shortcuts import render
from django.views.generic import ListView
from .models import Shop

class ShopsListView(ListView):
    model = Shop
    template_name = "shops/shops_list.html"
    context_object_name = 'shops_list'
