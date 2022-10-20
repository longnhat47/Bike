# Register your models here.
from django.contrib import admin

from bike.models import Bike, Type, Evaluate

admin.site.register(Bike)
admin.site.register(Type)
admin.site.register(Evaluate)
