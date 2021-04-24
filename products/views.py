from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)  # will need 'context' since we need to send some things back to the template


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
