from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Product(models.Model):
    class Meta:
        db_table = "my_product"

    product_types = (
        ('HD', '후드티'),
        ('JN', '청바지'),
        ('SO', '양말'),
        ('HT', '모자'),
    )
    product_type = models.CharField(choices=product_types, max_length=2, default='type')

    product_codes = (
        ('HD001', 'hood-001'),
        ('HD002', 'hood-002'),
        ('HD003', 'hood-003'),
        ('JN001', 'jean-001'),
        ('SO001', 'socks-001'),
        ('HT001', 'hat-001'),
    )
    product_code = models.CharField(choices=product_codes, max_length=5, default='N/A')

    product_sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    product_size = models.CharField(choices=product_sizes, max_length=1, default='N/A')

    product_name = models.CharField(max_length=15)
    product_price = models.CharField(max_length=10)
    product_desc = models.TextField()
    product_quantity = models.IntegerField(default=0)


class Inbound(Product):
    inbound_quantity = models.IntegerField(default=0)
    inbound_date = models.DateTimeField(auto_now_add=True)


class Outbound(Product):
    outbound_quantity = models.IntegerField(default=0)
    outbound_date = models.DateTimeField(auto_now_add=True)
