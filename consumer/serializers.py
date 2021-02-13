"""Serializers for Consumer app"""

# 3rd party imports
from rest_framework import serializers, viewsets

# Local imports
from consumer.models import Brand, CustomUser, Product, ProductCategory, Seller


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User Serializer"""
    class Meta:
        """Meta Class"""
        model = CustomUser
        fields = ['url', 'username', 'email', 'age', 'is_staff']


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer"""
    class Meta:
        """Meta Class"""
        model = Product
        fields = ['url', 'name', 'description', 'product_category', 'seller', 'brand']


class ProductCategorySerializer(serializers.ModelSerializer):
    """ProductCategory Serializer"""
    class Meta:
        """Meta Class"""
        model = ProductCategory
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    """Brand Serializer"""
    class Meta:
        """Meta Class"""
        model = Brand
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    """Seller Serializer"""
    class Meta:
        """Meta Class"""
        model = Seller
        fields = '__all__'


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """User Viewset"""
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Product Viewset"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """ProductCategory Viewset"""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class SellerViewSet(viewsets.ModelViewSet):
    """Seller Viewset"""
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """Brand Viewset"""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
