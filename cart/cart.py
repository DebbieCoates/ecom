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

    def add(self, product):
        product_id = str(product.id)

        #logic to add product to cart   
        if product_id in self.cart:
           pass
        else:
            self.cart[product_id]= {'price': str(product.price)}
            
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
