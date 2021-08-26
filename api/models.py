from django.db import models

# Auth Token Model Set up


# Create your models here.
class Product(models.Model):   
    product_name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_name + ' | ' + str(self.price)

