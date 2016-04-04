from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_id = models.IntegerField(default=0, unique=True)
    price = models.IntegerField(default=0)
    url = models.URLField()

    def __str__(self):
        return self.product_name

class Product_Variants(models.Model):
    product = models.ForeignKey(Product)
    sku_code = models.CharField(max_length=200)  
    size = models.CharField(max_length=20)    
        
    def __str__(self):
        return self.sku_code


