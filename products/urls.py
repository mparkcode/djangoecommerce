from django.urls import path
from .views import index, add_to_cart


urlpatterns = [
    path('', index, name='index'),
    path('cart/add', add_to_cart, name='add_to_cart')
]