from django.contrib import admin

from .models import UM, Producto
# Register your models here.

admin.site.register(Producto)
admin.site.register(UM)

