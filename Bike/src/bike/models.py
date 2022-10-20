import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from login.models import CustomUser


class Type(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True)

    class Meta:
        db_table = "type"

    def __str__(self):
        return self.name


class Bike(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255)
    type = models.ForeignKey(Type, related_name="bike", on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        _("Image"), upload_to="bike/", blank=True, null=True
    )
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "bike"

    def __str__(self):
        if self.status:
            status = 'True'
        else:
            status = 'False'
        return self.name + ' | ' + status

    def get_absolute_url(self):
        return reverse('bike_admin')


class Evaluate(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    content = models.TextField(blank=True)
    starts = models.IntegerField(blank=True)
    bike = models.ForeignKey(Bike, related_name="bike", on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(CustomUser, related_name="bike", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "evaluate"


