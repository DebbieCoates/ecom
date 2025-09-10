from django.db import models
from django.contrib.auth.models import User

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
        return f'Shipping Address for {str(self.id)} - {self.shipping_fullname}'


