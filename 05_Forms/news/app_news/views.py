from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from app_news.models import News, Commentary
from app_news.forms import NewsForm
from django.http import HttpResponseRedirect

class NewsListView(ListView):
    model = News
    template_name = "news_list.html"
    context_object_name = 'news_list'
    queryset = News.objects.all()[:5]


class NewsDetailedView(DetailView):
    model = News


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/create.html', context={'news_form': news_form})

    def post(self, request):

        news_form = NewsForm()

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_news/create.html', context={'news_form': news_form})
