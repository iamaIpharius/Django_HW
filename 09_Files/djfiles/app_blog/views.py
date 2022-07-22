from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogEntry
from django.views import View
from .forms import BlogForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect


class BlogListView(ListView):
    model = BlogEntry
    template_name = "app_blog/blog_list.html"
    context_object_name = 'blog_list'


class BlogFormView(View):

    def get(self, request):

        blog_form = BlogForm()
        return render(request, 'app_blog/create.html', context={'blog_form': blog_form})

    def post(self, request):

        blog_form = BlogForm(request.POST)

        if blog_form.is_valid():
            BlogEntry.objects.create(**blog_form.cleaned_data)
            return HttpResponseRedirect('/blog')
        return render(request, 'app_blog/create.html', context={'blog_form': blog_form})
