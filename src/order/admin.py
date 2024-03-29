from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.BookInCart)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    """Registration and representation of the model Order in the admin."""

    list_display = ('cart', 'create_date', 'update_date')
    list_filter = ('create_date', 'update_date')
    search_fields = ('cart', 'create_date')

@admin.register(models.OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    """Registration and representation of the model OrderStatus in the admin."""

    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title',)
