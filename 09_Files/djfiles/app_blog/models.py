from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class BlogEntry(models.Model):
    title = models.CharField(max_length=1500, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    date = models.DateField(auto_now_add=True, verbose_name=_('date'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('uploaded at'))
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE,
                             verbose_name=_('user'))

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = _('blog entry')
        verbose_name = _("blog entry's")

    def __str__(self):
        return f'{self.title}, {self.created_at}'


class Image(models.Model):
    image = models.ImageField(upload_to='blog_images/', verbose_name=_('image'))
    blog = models.ForeignKey(BlogEntry, on_delete=models.CASCADE, verbose_name=_('blog'))

    class Meta:
        verbose_name_plural = _('images')
        verbose_name = _('image')
