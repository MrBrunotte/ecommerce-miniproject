from django.shortcuts import render
from .models import Product

# Create your views here.
"""
So the first view we're going to create is all_products.
In this case, we take products.
And that's going to be product.objects.all, which will return all the products that are in the database.
And we're going to render a products.html page, which we have yet to write.
And within that page, we will have access to all products.
"""

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
