from django.shortcuts import render
from .models import Category, Product, Order, Customer

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
