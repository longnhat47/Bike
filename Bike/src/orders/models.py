from datetime import datetime

from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from bike.models import Bike
from login.models import CustomUser


class RentType(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "rent_type"



class Orders(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    bike = models.ForeignKey(Bike, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    rent_day_start = models.DateTimeField(verbose_name="Ngày thuê")
    rent_day_end = models.DateTimeField(verbose_name="Ngày trả")
    type_rent = models.ForeignKey(RentType, on_delete=models.SET_NULL, null=True, verbose_name="Loại thuê")
    price = models.IntegerField(blank=True)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "orders"
        ordering = ['-create_at']

    def __str__(self):
        return self.bike.name + '|' + self.customer.last_name + self.customer.first_name

    def get_absolute_url(self):
        return reverse('order-admin')


