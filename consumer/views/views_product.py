"""
Views for Product.
"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from consumer.models import Product, ProductCategory
from consumer.filters import ProductFilter


def home(request):
    """
    Get last 10 products by updated_at field.

    :param request:
    :return: All products
    """
    products_all = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products_all)
    page = request.GET.get('page', 1)
    paginator = Paginator(product_filter.qs, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, template_name='consumer/all_products.html',
                  context={'products': products, 'filter': product_filter})


def product_category_all_products(request, product_category_id):
    """Get all products.

       :param request:
       :param product_category_id: Id of ProductCategory
       :return: All products
       """
    product_category = ProductCategory.objects.get(id=product_category_id)
    _all_products = Product.objects.filter(product_category=product_category)
    product_filter = ProductFilter(request.GET, queryset=_all_products)
    return render(request, template_name='consumer/all_products.html', context={'filter': product_filter})


def product_by_seller(request, seller_id):
    """Get products of seller

    :param request:
    :param seller_id:
    :return:
    """
    products = Product.objects.filter(seller=seller_id)
    product_filter = ProductFilter(request.GET, queryset=products)
    return render(request, template_name='consumer/all_products.html', context={'filter': product_filter})


def search_product(request):
    """Search for keyword in name or description.

    :param request:
    :return:
    """
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        products = Product.objects.filter(
            Q(name__icontains=keyword) | Q(description__icontains=keyword)).order_by('name')
        product_filter = ProductFilter(request.GET, queryset=products)
        return render(request, template_name='consumer/all_products.html', context={'filter': product_filter})


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
