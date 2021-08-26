from rest_framework import serializers

# import models
from django.apps import apps
Post = apps.get_model('blog', 'Post')
from .models import Product

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'