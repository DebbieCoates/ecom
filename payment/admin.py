from django.contrib import admin
from .models import shippingAddress, Order, OrderItem
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(shippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Payment)  


#create an order iteminline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

#Extend out the order admin
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ('date_ordered',)
    fields = ('user', 'full_name', 'email', 'shipping_address', 'amount_paid', 'date_ordered', 'shipped', 'date_shipped')
    inlines = [OrderItemInline]

#unregister
admin.site.unregister(Order)

#re-regegister
admin.site.register(Order, OrderAdmin)

