"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# 3rd part imports.
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from consumer.views.views_product import last_updated_products
from consumer.serializers import UserViewSet, ProductViewSet, ProductCategoryViewSet
from consumer.serializers import SellerViewSet, BrandViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productcategories', ProductCategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'sellers', SellerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumer/', include('django.contrib.auth.urls')),
    path('order/', include('order.urls')),  # All urls in consumer url file will start with this.
    path('consumer/', include('consumer.urls', namespace='consumer')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/consumer/', include(router.urls)),
    path('', last_updated_products, name='home'),
]
