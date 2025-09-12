from django.db import models
from django.contrib.auth.models import User
from  store.models import Product
from django.db.models.signals import post_save

# Create your models here.
class shippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shipping_fullname = models.CharField(max_length=100)
    shipping_email = models.EmailField()
    shipping_address1 = models.CharField(max_length=255, blank=True, null=True)
    shipping_address2 = models.CharField(max_length=255, blank=True, null=True)
    shipping_city = models.CharField(max_length=255, blank=True, null=True)
    shipping_county = models.CharField(max_length=255, blank=True, null=True)
    shipping_postcode = models.CharField(max_length=255, blank=True, null=True)
    shipping_country = models.CharField(max_length=255, blank=True, null=True)

   #Dont pluralise address to addresses
    class Meta:
        verbose_name_plural = 'Shipping Address'
        
    def __str__(self):
        return f'Shipping Address for ID : {str(self.id)} - {self.shipping_fullname}'

# Create a shipping address by default when a user signs up
def create_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = shippingAddress(user=instance)
        user_shipping.save()

# Automate the profile creation
post_save.connect(create_shipping, sender=User)



#Create Order Model
class Order(models.Model):
    #foreight key to user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField() 
    shipping_address = models.TextField(max_length=15000)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)  # New field to store the amount paid
    date_ordered = models.DateTimeField(auto_now_add=True)

def __str__(self):
    if self.user:
        return f"Order by {self.user.username}"
    return "Order by guest"
    
# Create OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price at the time of order

    def __str__(self):
        return f'OrderItem - {self.id} for Order - {self.order.id}'
