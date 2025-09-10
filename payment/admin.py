from django.contrib import admin
from .models import shippingAddress, Order, OrderItem


# Register your models here.
admin.site.register(shippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Payment)  