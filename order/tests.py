"""Test for Order app"""
from decimal import Decimal

# 3rd party imports
from django.test import TestCase

from model_mommy import mommy


from order.models import CartItem, Cart
from consumer.models import Product, ProductCategory, Brand, Seller


class CartItemTest(TestCase):

    def setUp(self):
        self.product_category = mommy.make(ProductCategory)
        self.seller = Seller.objects.create(name='FavDukaan', address='Gali_no_1', phone=1234567890)
        self.brand = mommy.make(Brand)
        self.product = Product.objects.create(name='GoodProd',
                                              brand=self.brand,
                                              description='',
                                              product_category=self.product_category,
                                              seller=self.seller,
                                              price=100.0)

        self.product_1 = Product.objects.create(name='AnotherGoodProd',
                                                brand=self.brand,
                                                description='',
                                                product_category=self.product_category,
                                                seller=self.seller,
                                                price=150.0)

        self.cart = mommy.make(Cart)
        cart_item = CartItem.objects.create(item=self.product, quantity=10)
        cart_item_1 = CartItem.objects.create(item=self.product_1, quantity=5)
        self.cart.cart_item.add(cart_item)
        self.cart.cart_item.add(cart_item_1)

    def test_cart_total(self):
        result = self.cart.cart_total()
        assert result['item__price__sum'] == Decimal('250')
        assert result['quantity__sum'] == Decimal(15)