from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from consumer.models import Brand, CustomUser, Product, ProductCategory, Seller
from consumer.models import Currency, Address


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['username', 'email', 'age', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', )}),
    )


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['name', 'product_category', 'seller', 'brand', 'price']

    fields = ('name', 'price', 'description', 'product_category', 'seller', 'brand')
    search_fields = ('name', )


class AddressAdmin(admin.ModelAdmin):
    model = Address

    list_display = ['location', 'consumer', 'default']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Seller)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brand)
admin.site.register(Currency)
admin.site.register(Address, AddressAdmin)

