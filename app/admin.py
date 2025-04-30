from django.contrib import admin
from . import models
from .models import Stylist
from .models import Appointment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'user']

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Order._meta.get_fields()]
    list_filter = ['status']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)

@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'category')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'stylist', 'appointment_date')