from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views.generic import ListView, DetailView


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = "advertisement_list.html"
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(DetailView):
    model = Advertisement

