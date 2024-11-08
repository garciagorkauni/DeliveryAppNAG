from django.urls import path
from . import views

urlpatterns = [
    #admin
    path('stats/', views.stats_view, name='admin_stats'),

    # home
    path('', views.home, name='home'),

    # menu
    path('products/', views.menu, name='menu'),
    path('update-product-list/', views.update_product_list, name='update_product_list'),

    # product
    path('product/<int:product_id>/', views.product, name='product'),
    
    # valoration
    path('add-rating/<int:product_id>/', views.add_rating, name='add_rating'),

    # cart
    path('cart/', views.cart, name='cart'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete-cart/<int:cart_id>/', views.delete_cart, name='delete_cart'),
    path('reduce-cart/<int:product_id>/', views.reduce_cart, name='reduce_cart'),
    path('payment/', views.payment, name='payment'),
    
    # profile
    path('profile/', views.profile, name='profile'),
    path('add-address/', views.add_address, name='add_address'),
    path('edit-address/<int:id>/', views.edit_address, name='edit_address'),
    path("update-address-list/", views.update_address_list, name="update_address_list"),

    # Profile authentication management
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/delete', views.delete_profile, name='delete_profile'),

    # address
    path('address_delete/<int:address_id>/', views.delete_address, name='delete_address'),
    #Rest
    path('v1/product', views.Product_APIView.as_view()),
    path('v1/product/<int:pk>/', views.Product_APIView_Detail.as_view())
]