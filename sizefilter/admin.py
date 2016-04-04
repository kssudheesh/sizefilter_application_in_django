from django.contrib import admin

from .models import Product, Product_Variants

admin.site.register(Product)
admin.site.register(Product_Variants)
