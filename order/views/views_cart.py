from django.shortcuts import render

from order.models import Cart, CartItem
from consumer.models import CustomUser, Product


def get_cart(request):
    user = request.user
    if request.method == 'GET':
        cart = Cart.objects.get(consumer=user)
        return render(request, template_name='order/cart.html', context={'cart': cart})


def add_to_cart(request, product_id):
    user = request.user
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(consumer=user)
        if cart.cart_item.filter(item=product).exists():
            _cart_item = CartItem.objects.get(item=product)
            _cart_item.quantity += 1
            _cart_item.save()
        else:
            _cart_item = CartItem.objects.create(item=product, quantity=1)
            cart.cart_item.add(_cart_item)
        return render(request, template_name='order/cart.html', context={'cart': cart})

