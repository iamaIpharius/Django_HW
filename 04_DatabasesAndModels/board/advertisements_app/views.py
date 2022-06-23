from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views.generic import ListView

class AdvertisementListView(ListView):
    model = Advertisement
    template_name = "advertisement_list"
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]
