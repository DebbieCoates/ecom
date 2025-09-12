from urllib import request
from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingAddressForm, PaymentForm
from payment.models import shippingAddress
from django.contrib import messages
from payment.models import Order, OrderItem
from django.contrib.auth.models import User

def orders(request, id):
	if request.user.is_authenticated and request.user.is_superuser:
		# Get the order
		order = Order.objects.get(id=id)
		# Get the order items
		items = OrderItem.objects.filter(order_id=id)
		return render(request, "payment/orders.html", {'order': order, 'items': items})
	else:
		messages.success(request, 'Order Placed.')
		return redirect('home')

#  not_shipped_dashnot shipped dashboard
def not_shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
     
		orders = Order.objects.filter(shipped = False)
		return render(request, "payment/not_shipped_dash.html", {'orders': orders})
	else:    
		messages.success(request, 'Order Placed.')
		return redirect('home')

# shipped_dash shipped dashboard
def shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
	 
		orders = Order.objects.filter(shipped = True)
		return render(request, "payment/shipped_dash.html", {'orders': orders})
	else:    
		messages.success(request, 'Order Placed.')
		return redirect('home')



def process_order(request):
	if request.POST:

		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()

		payment_form = PaymentForm(request.POST or None)
		# Get shipping session data
		my_shipping = request.session.get('my_shipping')

		# Gather order info
		full_name = my_shipping['shipping_fullname']
		email = my_shipping['shipping_email']
		#  Create the shipping address
		shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_county']}\n{my_shipping['shipping_postcode']}\n{my_shipping['shipping_country']}"
		amount_paid = totals

		# Create an order
		if request.user.is_authenticated:
			# user is logged in
			user = request.user
			create_order = Order.objects.create(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()
   
  			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price
				if product.is_sale:
					price = product.sale_price
				else:
					price = product.price

				# Get quantity
				for key,value in quantities().items():
					if int(key) == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
						create_order_item.save()
      
      
			for key in list(request.session.keys()):
				if key == 'session_key':
					del request.session[key]

			messages.success(request, 'Order Placed.')
			return redirect('home')
		else:
			# user is not logged in
			create_order = Order.objects.create(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()
   
     			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price
				if product.is_sale:
					price = product.sale_price
				else:
					price = product.price

				# Get quantity
				for key,value in quantities().items():
					if int(key) == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id,  quantity=value, price=price)
						create_order_item.save()

			for key in list(request.session.keys()):
				if key == 'session_key':
					del request.session[key]
      
			messages.success(request, 'Order Placed.')
			return redirect('home')

	else:
		messages.success(request, 'Access denied.')
		return redirect('home')
	 



def billing_info(request):
	if request.POST:
     
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()
  
		#crete a shipping session
		my_shipping = request.POST
		my_shipping = request.session['my_shipping'] = my_shipping

		# Check to see if user is logged in
		if request.user.is_authenticated:
			# Get the billing form 
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
		else:
			# NOT LOGGED IN    
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})

	else:
		messages.success(request, 'Access denied.')
		return redirect('home')

def checkout(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()

	if request.user.is_authenticated:
		#checkout as logged in user
		#shipping user
		shipping_user = shippingAddress.objects.get(user__id=request.user.id)
		#Shipping form
		shipping_form = ShippingAddressForm(request.POST or None, instance=shipping_user)
		return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
	else:
		#checkout as guest
		shipping_form = ShippingAddressForm(request.POST or None)
		return render(request, "payment/checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})



def payment_success(request):
    return render(request, 'payment/payment_success.html', {})  