from django.urls import path

from order.views import views_cart

app_name = 'order'

urlpatterns = [
    path('cart', views_cart.get_cart, name='user_cart'),
    path('add_to_cart/<int:product_id>', views_cart.add_to_cart, name='add_to_cart'),
]