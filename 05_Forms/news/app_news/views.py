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


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news_detail'

class CommentaryView(View):
    def get(self, request):
        commentary_form = CommentaryForm()
        return render(request, 'app_news/news_detail.html', context={'commentary_form': commentary_form})


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/create.html', context={'news_form': news_form})

    def post(self, request):

        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news')
        return render(request, 'app_news/create.html', context={'news_form': news_form})


class NewsEditFormView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})