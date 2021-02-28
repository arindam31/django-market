from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from order.models import Cart, CartItem
from consumer.models import Product
from order.forms import EditCartItemForm
from django.views.generic import UpdateView


def get_cart(request):
    user = request.user
    template_name = 'order/cart.html'

    if not user.is_authenticated:
        redirect('login')

    if request.method == 'GET':
        cart = Cart.objects.get(consumer=user)
        amount_each_item, total_bill = cart.cart_each_item_total()
        if amount_each_item:
            return render(request,
                          template_name=template_name,
                          context={'cart': amount_each_item, 'cart_total': total_bill})
        else:
            return render(request,
                          template_name=template_name,
                          context={'message': 'No items. Please add some items.'})


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


def remove_cart_item(request, cart_item_id):
    """Add items to Cart.

    :param request: django request
    :param cart_item_id: Id of Cart Item.
    """
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('order:user_cart')


class EditCartItem(UpdateView):
    model = CartItem
    template_name = 'order/cart_edit.html'
    form_class = EditCartItemForm

    def get_success_url(self):
        return reverse_lazy('order:user_cart')

