from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.aboutPage, name='blog-about'),
    path('contact/', views.aboutPage, name='blog-contact'),
]