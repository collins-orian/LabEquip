# This file configures our views, and trigger urls by connecting views to urls

from django.urls import path
from . import views

urlpatterns = [

    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>', views.getProduct, name='product'),
]
