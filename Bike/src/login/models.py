from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    gender = models.IntegerField(default=0)
    phone = models.CharField(max_length=15, blank=True)
    cmnd = models.CharField(max_length=15, blank=True)
    birthday = models.DateTimeField(default=datetime.now, null=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['last_name']
