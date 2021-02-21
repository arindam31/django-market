"""Urls for Consumer App"""

from django.urls import path

from consumer.views import views_product, views_seller, views_user

app_name = 'consumer'
urlpatterns = [
    path('product/<int:pk>', views_product.ProductDetails.as_view(), name='product_details'),
    path('productcategory/<int:product_category_id>',
         views_product.product_category_all_products,
         name='product_by_category'),
    path('seller/<int:seller_id>/products', views_product.product_by_seller, name='productBySeller'),
    path('seller/all', views_seller.SellerListView.as_view(), name="allSellers"),
    path('signup/', views_user.SignUpView.as_view(), name='register'),
    path('customer/<slug:pk>/', views_user.UserDetailsView.as_view(), name='profile'),
    path('search/', views_product.search_product, name='search_product'),
    path('addAddress/<int:user_id>', views_user.AddressCreateView.as_view(), name='add_address'),
]
