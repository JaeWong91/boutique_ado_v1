from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)  # will need 'context' since we need to send some things back to the template
