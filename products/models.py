from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    qty = models.IntegerField()
    price = models.FloatField()
    desc = models.CharField(max_length=255)
    barcode = models.CharField(max_length=34)

    class Meta:
        db_table = "PRODUCT_MASTER"
