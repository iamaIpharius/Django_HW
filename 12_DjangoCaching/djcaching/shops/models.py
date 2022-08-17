from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    category = models.CharField(max_length=30, verbose_name=_('category'))

    class Meta:
        verbose_name_plural = _('shops')
        verbose_name = _("shop")
