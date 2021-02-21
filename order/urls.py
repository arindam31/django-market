from django.urls import path

from order.views import views_cart

app_name = 'order'

urlpatterns = [
    path('cart', views_cart.get_cart, name='user_cart'),
    path('edit_cart_item/<int:pk>', views_cart.EditCartItem.as_view(), name='edit_cart_item'),
    path('remove_cart_item/<int:cart_item_id>', views_cart.remove_cart_item, name='remove_cart_item'),
    path('add_to_cart/<int:product_id>', views_cart.add_to_cart, name='add_to_cart'),
]