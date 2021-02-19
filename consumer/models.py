from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    location = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField()
    default = models.BooleanField(default=False)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    perishable = "PR"
    non_perishable = "NPR"
    CHOICES = [
        (perishable, 'Perishable'),
        (non_perishable, 'NonPerishable'),
               ]
    life = models.CharField(
        max_length=3,
        choices=CHOICES,
        default=non_perishable
    )

    class Meta:
        verbose_name_plural = "ProductCategories"

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=7, decimal_places=2, default=0)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name
