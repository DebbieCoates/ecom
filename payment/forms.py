from django import forms
from .models import shippingAddress 

class ShippingAddressForm(forms.ModelForm):

    shipping_fullname = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email address'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 1'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address Line 2'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=True)
    shipping_county = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'County'}), required=False)
    shipping_postcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postcode'}), required=True)
    shipping_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=True)

    class Meta:
        model = shippingAddress
        fields = ['shipping_fullname', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_county', 'shipping_postcode', 'shipping_country']
        
        exclude = ['user',]