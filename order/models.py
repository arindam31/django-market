from django.db import models
from consumer.models import Product, CustomUser


class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    """
    A Cart is a holder of cart items.

    At one time, a customer can holed only one cart.
    Once an order is placed, cart items are converted into order items.
    The cart should be now empty.
    """
    consumer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart_{self.consumer.username}'
