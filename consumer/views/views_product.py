"""
Views for Product.
"""

from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from consumer.models import Product, ProductCategory


def last_updated_products(request):
    """
    Get last 10 products by updated_at field.

    :param request:
    :return: All products
    """
    products = Product.objects.all().order_by('-updated_at')[:10]
    return render(request, template_name='consumer/all_products.html', context={'products': products})


def product_category_all_products(request, product_category_id):
    """Get all products.

       :param request:
       :param product_category_id: Id of ProductCategory
       :return: All products
       """
    product_category = ProductCategory.objects.get(id=product_category_id)
    _all_products = Product.objects.filter(product_category=product_category)
    return render(request, template_name='consumer/all_products.html', context={'products': _all_products})


def product_by_seller(request, seller_id):
    """Get products of seller

    :param request:
    :param seller_id:
    :return:
    """
    products = Product.objects.filter(seller=seller_id)
    return render(request, template_name='consumer/all_products.html', context={'products': products})


def search_product(request):
    """Search for keyword in name or description.

    :param request:
    :return:
    """
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        products = Product.objects.filter(
            Q(name__icontains=keyword) | Q(description__icontains=keyword)).order_by('name')
        return render(request, template_name='consumer/all_products.html', context={'products': products})


class HomeView(TemplateView):
    """Home View class.

    """
    template_name = 'home.html'


class ProductDetails(DetailView):
    """
    Product view class.
    """
    model = Product
    template_name = 'consumer/product_details.html'
