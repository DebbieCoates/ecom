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
        
        
