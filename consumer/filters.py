import django_filters
from consumer.models import Product


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ['product_category', 'seller', 'brand']