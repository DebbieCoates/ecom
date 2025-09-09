from itertools import product
from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        
        # get the current session key if it exists
        cart = self.session.get('session_key')
        
        ## if the user is new, no session key, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure cart is available on all pages
        self.cart = cart


    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
		# Logic
        if product_id in self.cart:
            pass
        else:
			#self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        #get id's from cart
        Product_ids = self.cart.keys()
        #use id's to look up products in db model
        products = Product.objects.filter(id__in=Product_ids)
        #return the products looked up
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #get cart
        ourcart = self.cart
        #update quantity
        ourcart[product_id] = product_qty
        #save to session    
        self.session.modified = True
        
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        #delete item
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True