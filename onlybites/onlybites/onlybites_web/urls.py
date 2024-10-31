from django.urls import path
from . import views

urlpatterns = [
    # home
    path('', views.home, name='home'),

    # menu
    path('products/', views.menu, name='menu'),

    # product
    path('product/<int:product_id>/', views.product, name='product'),

    # cart
    path('cart/', views.cart, name='cart'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),

    # profile
    path('profile/', views.profile, name='profile'),
    path('add-address/', views.add_address, name='add_address'),
    path('edit-address/<int:productid>/', views.edit_address, name='edit_address'),

    # Profile authentication management
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]