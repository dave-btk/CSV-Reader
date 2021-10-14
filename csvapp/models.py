from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    purchase_date = models.TextField()
