from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),

    # menu
    path('products/', views.menu, name='menu'),

    # product
    path('product/', views.product, name='product'),

    # cart
    path('cart/', views.cart, name='cart'),

    # register
    path('register/', views.register, name='register'),

    # profile
    path('profile/', views.profile, name='profile'),
]