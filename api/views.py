from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# import models
from django.apps import apps

Post = apps.get_model('blog', 'Post')
from .models import Cart, Product
from rest_framework.authtoken.models import Token

# import serializers
from .serializers import CartSerializer, CreatePostSerializer, PostSerializer, ProductSerializer, RegistrationSerializer


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
@permission_classes((IsAuthenticated,))
def createPost(request):
    user = request.user
    post = Post(author=user)
    serializer = CreatePostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def updatePost(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permission to edit that."})
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def deletePost(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permission to delete that."})
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
def registerUser(request):
    serializer = RegistrationSerializer(data = request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key
        data = {
            'response': "Successfully registered a new user.",
            'email': account.email,
            'username': account.username,
            'token': token,
        }
    else:
        data = serializer.errors
    return Response(data)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getCart(request):
    user = request.user
    cart = Cart.objects.all().filter(user=user)
    products = [item.product for item in cart]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def addToCart(request):
    user = request.user
    product = Product.objects.get(id=request.data['id'])
    cart = Cart(user=user, product=product)
    serializer = CartSerializer(cart, data={"user": user.id, "product":product.id}, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def removeFromCart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).filter(product=request.data['id'])[0]
    if cart:
        cart.delete()
        return Response({'response': "Successfully removed item from cart."})
    return Response({'response': "You don't have that item in your cart."})
    
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def emptyCart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    if cart:
        cart.delete()
        return Response({'response': "Successfully removed all items from cart."})
    return Response({'response': "You don't have any items to remove from your cart."})


def testAPI(request):
    return Response(
        {
            "name": "Legends-2",
            "personel": [
                {
                    "first_name": 'Shoha',
                    "last_name": "T"
                },
                {
                    "first_name": 'Kaile',
                    "last_name": "W"
                },
                {
                    "first_name": 'Christian',
                    "last_name": "V"
                },
                {
                    "first_name": 'Ivan',
                    "last_name": "W"
                },
                {
                    "first_name": 'Shinha',
                    "last_name": "T"
                }
            ],
        }
    )