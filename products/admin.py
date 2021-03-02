from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Products)
admin.site.register(Tags)
admin.site.register(Shopcart)
admin.site.register(Address)
admin.site.register(Ordered)
