from django.shortcuts import render, redirect

from order.models import Cart, CartItem
from consumer.models import Product


def get_cart(request):
    user = request.user
    if not user.is_authenticated:
        redirect('login')

    if request.method == 'GET':
        cart = Cart.objects.get(consumer=user)
        amount_each_item, total_bill = cart.cart_each_item_total()
        return render(request,
                      template_name='order/cart.html',
                      context={'cart': amount_each_item, 'cart_total': total_bill})


def add_to_cart(request, product_id):
    """Add items to Cart.

    :param request: django request
    :param product_id: Id of Product.
    """
    if request.user.is_anonymous:
        return redirect('consumer:register')

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(consumer=request.user)
        if cart.cart_item.filter(item=product).exists():
            _cart_item = CartItem.objects.get(item=product)
            _cart_item.quantity += 1
            _cart_item.save()
        else:
            _cart_item = CartItem.objects.create(item=product, quantity=1)
            cart.cart_item.add(_cart_item)
        return redirect('order:user_cart')

