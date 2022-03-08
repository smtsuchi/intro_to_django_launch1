from django.contrib import admin

# import Post
from .models import Product, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)