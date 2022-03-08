from django.urls import path

from . import views

# import built-in  Login Function (view)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='api-index'),
    path('posts/', views.posts, name='api-posts'),
    path('posts/<int:post_id>/', views.individualPost, name='api-individualpost'),
    path('posts/create/', views.createPost, name='api-createpost'),
    path('posts/update/<int:post_id>/', views.updatePost, name='api-updatepost'),
    path('posts/delete/<int:post_id>/', views.deletePost, name='api-deletepost'),
    path('products/', views.products, name='api-products'),
    path('products/<int:product_id>/', views.individualProduct, name='api-individualproduct'),
    path('login/', obtain_auth_token, name='api-login'),
    path('register/', views.registerUser, name='api-register'),

    path('cart/get/', views.getCart, name='api-getcart'),
    path('cart/add/', views.addToCart, name='api-addcart'),
    path('cart/delete/', views.removeFromCart, name='api-deletecart'),
    path('cart/empty/', views.emptyCart, name='api-emptycart'),

    path('test/', views.testAPI, name='api-test'),
]