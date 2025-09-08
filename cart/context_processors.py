from  .cart import Cart

#Create Context Processor so our cart is available on all pages
def cart(request):
    #return default data from our cart
    return {'cart': Cart(request)}