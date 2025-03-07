from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="img")
    category = models.CharField(max_length=100, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    level = models.IntegerField(default=4)

    def __str__(self):
        return self.product_name

