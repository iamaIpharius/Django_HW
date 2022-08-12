from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogEntry, Image
from django.views import View
from .forms import BlogForm, UploadForm
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from csv import reader


class BlogListView(ListView):
    model = BlogEntry
    template_name = "app_blog/blog_list.html"
    context_object_name = 'blog_list'


class BlogDeatailView(View):
    def get(self, request, blogentry_id):
        blog = BlogEntry.objects.get(id=blogentry_id)
        title = blog.title
        content = blog.content
        images = blog.image_set.all()
        return render(request, 'app_blog/blog_detail.html', context={'title': title, 'content': content, 'images': images})



    # model = BlogEntry
    # template_name = "app_blog/blog_detail.html"
    # context_object_name = 'blog_detail'


class BlogFormView(View):

    def get(self, request):

        blog_form = BlogForm()
        return render(request, 'app_blog/create.html', context={'blog_form': blog_form})

    def post(self, request):

        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            new_blog = BlogEntry.objects.create(
                user=request.user, **blog_form.cleaned_data)
            images = request.FILES.getlist('image')
            for i in images:
                Image.objects.create(image=i, blog=new_blog)
            return HttpResponseRedirect('/blog')
        return render(request, 'app_blog/create.html', context={'blog_form': blog_form})


def upload_posts(request):
    if request.method == 'POST':
        upload_file_form = UploadForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            print(upload_file_form.cleaned_data)
            posts_file = upload_file_form.cleaned_data['file'].read()
            posts_str = posts_file.decode('utf-8').split('\n')
            csv_reader = reader(posts_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                BlogEntry.objects.create(
                    user=request.user, title=row[0], content=row[1])
            return HttpResponse(content='Посты загружены', status=200)
    else:
        upload_file_form = UploadForm()

    context = {
        'form': upload_file_form
    }

    return render(request, 'app_blog/upload.html', context=context)
