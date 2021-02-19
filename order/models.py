from django.db import models
from django.db.models import Avg, Sum, F, ExpressionWrapper, FloatField
from consumer.models import Product, CustomUser


class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Item: {self.item.name}, Quantity: {self.quantity}'


class Cart(models.Model):
    """
    A Cart is a holder of cart items.

    At one time, a customer can holed only one cart.
    Once an order is placed, cart items are converted into order items.
    The cart should be now empty.
    """
    consumer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cart_item = models.ManyToManyField(CartItem)

    def __str__(self):
        return f'Cart_{self.consumer.username}'

    def cart_total(self):
        """Calculate cart total.

        :return:
        """
        # Get all products in cart with quantity.
        cart_details = self.cart_item.all().aggregate(Sum('item__price'), Sum('quantity'))
        return cart_details

    def cart_each_item_total(self):
        amount_each_item = self.cart_item.filter().annotate(
            unit_total=ExpressionWrapper(Sum(F('item__price') * F('quantity')), output_field=FloatField()))

        total_bill = amount_each_item.aggregate(Sum('unit_total'))
        return amount_each_item, total_bill

