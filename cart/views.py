from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
from decimal import Decimal




# Create your views here.
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_total = 0
    cart_items = []
    for p in cart:
        product = get_object_or_404(Product, pk=p)
        cart_item = {
            'product' : product,
            'quantity' : cart[p],
            'total': Decimal(product.price * cart[p])
        }
        cart_items.append(cart_item)
        cart_total += cart_item['total']

    
    return render(request, "cart/cart.html", {'cart': cart_items, 'total': cart_total})
    
def add_to_cart(request):
    
    #  Get the product we're adding
    id = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=id)
    
    #  Get the current cart
    cart = request.session.get('cart', {})
    
    
    #  Update the cart
    cart[id] = cart.get(id, 0) + 1
    
    #  Save the cart back to the session
    request.session['cart'] = cart 
    
    #  Redirect somewhere
    return HttpResponse(cart[id])
    
def remove_from_cart(request):
    
    #  Get the product we're removing
    id = request.POST.get('product_id')
    # product = get_object_or_404(Product, pk=id)
    
    #  Get the current cart
    cart = request.session.get('cart', {})
    
    
    #  Update the cart
    if cart[id] > 1:
        cart[id] = cart.get(id, 0) - 1
    else:
        del cart[id]
    
    #  Save the cart back to the session
    request.session['cart'] = cart 
    
    #  Redirect somewhere
    return redirect('view_cart')