from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from app_news.models import News, Commentary
from app_news.forms import NewsForm, CommentaryForm, CommentaryAuthForm
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django_filters.views import FilterView
from app_news.filtersets import NewsFilter


class NewsListView(ListView):
    model = News
    template_name = "news_list.html"
    context_object_name = 'news_list'
    queryset = News.objects.all()


class NewsDetailView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        template_name = "app_news/news_detail.html"
        comments = news.commentary_set.all()
        new_commentary = None
        commentary_form = CommentaryForm()
        return render(request, template_name, context={'news': news,
                                                       'comments': comments,
                                                       'new_commentary': new_commentary,
                                                       'commentary_form': commentary_form,
                                                       'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        template_name = "app_news/news_detail.html"
        comments = news.commentary_set.all()
        new_commentary = None

        if request.user.is_authenticated:
            commentary_form = CommentaryAuthForm(request.POST)
            if commentary_form.is_valid():
                Commentary.objects.create(
                    related_news=news, name=request.user, user=request.user, **commentary_form.cleaned_data)
                request.user.news_published += 1
                return HttpResponseRedirect(f'/news/{news_id}')

        else:
            commentary_form = CommentaryForm(request.POST)
            if commentary_form.is_valid():
                Commentary.objects.create(
                    related_news=news, **commentary_form.cleaned_data)
                return HttpResponseRedirect(f'/news/{news_id}')

        return render(request, template_name, context={'news': news,
                                                       'comments': comments,
                                                       'new_commentary': new_commentary,
                                                       'commentary_form': commentary_form,
                                                       'news_id': news_id})


class NewsFormView(View):

    def get(self, request):
        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied()
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
        if not request.user.has_perm('app_news.edit_news'):
            raise PermissionDenied()
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})
            

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/edit.html', context={'news_form': news_form, 'news_id': news_id})
