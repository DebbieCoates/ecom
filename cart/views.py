from django.shortcuts import render

# Create your views here.
def cart_summary(request):
    return render(request, 'cart_summary.html', {})        

def cart_add(request, product_id):
    return render(request, 'cart_add.html', {})

def cart_delete(request, product_id):
    return render(request, 'cart_delete.html', {})

def cart_update(request, product_id):
    return render(request, 'cart_update.html', {})