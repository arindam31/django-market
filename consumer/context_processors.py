"""
Custom context processors.
"""

from .models import ProductCategory


def get_all_product_category(request):
    """
    Get all product categories for out product category drop down.

    :param request:
    :return: All product categories.
    """

    product_categories = ProductCategory.objects.all()
    return {
        'categories': product_categories,
    }
