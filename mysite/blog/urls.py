from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.aboutPage, name='blog-about'),
    path('lol/', views.aboutPage, name='blog-about'),
    path('posts/', views.posts, name='blog-posts'),
    path('posts/create', views.createPost, name='blog-createpost'),
    path('register/', views.registerPage, name='blog-register'),
    path('login/', views.loginPage, name='blog-login'),
    path('logout/', views.logoutUser, name='blog-logout'),
]