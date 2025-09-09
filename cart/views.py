from django.shortcuts import render, get_object_or_404, redirect    
from .cart import Cart
from  store.models import Product
from django.http import JsonResponse


# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'cart_summary.html', {'cart_products': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = cart.__len__()

        #response = JsonResponse({'Product name': product.name, 'cart_quantity': cart_quantity})
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request, product_id):
    return render(request, 'cart_delete.html', {})

def cart_update(request, product_id):
    return render(request, 'cart_update.html', {})