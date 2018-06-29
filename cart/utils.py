#  cart/utils
from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):
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
    return {'cart': cart_items, 'total': cart_total}