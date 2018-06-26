from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {'products': products})
    
def add_to_cart(request):
    product = request.POST.get('product_id')
    product = get_object_or_404(Product, pk=product)
    return HttpResponse(product)