from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    balance = models.FloatField(default=0, blank=True, verbose_name=_('balance'))
    sales = models.CharField(max_length=36, blank=True, verbose_name=_('sales'))
    proposals = models.JSONField()
    history = models.JSONField()

    class Meta:
        permissions = (
            ('can_verify', 'Может верифицировать'),
        )
