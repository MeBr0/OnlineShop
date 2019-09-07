from django.contrib import admin

from order.models import Order


# admin registration for model Order
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'product', 'status', 'owner', )
