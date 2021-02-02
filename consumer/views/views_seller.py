from django.shortcuts import render
from django.views.generic import ListView

from consumer.models import Product, Seller


def product_by_seller(request, seller_id):
    """
    Get all products from a seller
    :param request: Request
    :param seller_id: Id of seller
    :return: response
    """
    products = Product.objects.filter(seller=seller_id)
    return render(request, template_name='consumer/all_products.html', context={'products': products})

class SellerListView(ListView):
    model = Seller
    template_name = 'consumer/all_sellers.html'
