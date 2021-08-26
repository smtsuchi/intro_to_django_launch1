from rest_framework.decorators import api_view
from rest_framework.response import Response

# import models
from django.apps import apps
Post = apps.get_model('blog', 'Post')
from .models import Product

# import serializers
from .serializers import PostSerializer, ProductSerializer

# Create your views here.
@api_view(["GET"])
def index(request):
    return Response({'hello': 'there'})

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def individualPost(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def updatePost(request, post_id):
    post = Post.objects.get(id=post_id)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return Response({"messages": "Successfully deleted the post."})

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def individualProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def loginUser(request):
    print(request.data)
    return Response({"message": "We received the login credentials!"})

@api_view(["POST"])
def registerUser(request):
    print(request.data)
    return Response({"message": "We received the new user's credentials!"})