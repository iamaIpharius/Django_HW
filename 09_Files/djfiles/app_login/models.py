from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    about = models.TextField(max_length=200, blank=True)
    class Meta:
        permissions = (
            ('can_verify', 'Может верифицировать'),
        )