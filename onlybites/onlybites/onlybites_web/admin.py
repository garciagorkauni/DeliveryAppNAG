from django.contrib import admin
from .models import Profile, Address, Product, Valoration, Cart, Order, Image, Allergen, ProductAllergen

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'birthdate', 'telephone', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('email', 'name', 'surname')
    ordering = ('email',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('profile', 'country', 'city', 'postal_code', 'address1')
    list_filter = ('country', 'city')
    search_fields = ('country', 'city', 'postal_code', 'address1')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock', 'price')
    list_filter = ('vegan', 'celiac', 'stock')
    search_fields = ('name', 'description')

@admin.register(Valoration)
class ValorationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'message', 'value')
    list_filter = ('value',)
    search_fields = ('profile__email', 'product__name')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'quantity')
    search_fields = ('profile__email', 'product__name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'address', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('profile__email', 'product__name')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'path')
    search_fields = ('product__name',)

@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(ProductAllergen)
class ProductAllergenAdmin(admin.ModelAdmin):
    list_display = ('product', 'allergen')
    search_fields = ('product__name', 'allergen__name')
