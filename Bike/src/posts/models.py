import uuid
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(unique=True)
    content = models.TextField(default="")
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_admin')
