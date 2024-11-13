from django.contrib import admin
from django.utils.translation import get_language
from .models import Profile, Address, Product, Valoration, Cart, Order, Image, Allergen, ProductAllergen

admin.site.index_template = "admin/admin_index.html" 

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
    lang = get_language()
    if lang == 'es':
        list_display = ('name_es', 'description_es', 'stock', 'price')
    elif lang == 'en':
        list_display = ('name_en', 'description_en', 'stock', 'price')
    elif lang == 'eu':
        list_display = ('name_eus', 'description_eus', 'stock', 'price')
    list_filter = ('vegan', 'celiac', 'stock')
    search_fields = ('name_es', 'name_en', 'name_eu', 'description_es', 'description_en', 'description_eu')

@admin.register(Valoration)
class ValorationAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'message', 'value')
    list_filter = ('value',)
    search_fields = ('profile__email', 'product__name_es', 'product__name_en', 'product__name_eu')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'quantity')
    search_fields = ('profile__email', 'product__name_es', 'product__name_en', 'product__name_eu')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('profile', 'product', 'address', 'quantity', 'date')
    list_filter = ('date',)
    search_fields = ('profile__email', 'product__name_es', 'product__name_en', 'product__name_eu')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'path')
    search_fields = ('product__name_es', 'product__name_en', 'product__name_eu')

@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    lang = get_language()
    if lang == 'es':
        list_display = ('name_es', 'description_es')
    elif lang == 'en':
        list_display = ('name_en', 'description_en')
    elif lang == 'eu':
        list_display = ('name_eus', 'description_eus')
    search_fields = ('name_es', 'name_en', 'name_eu', 'description_es', 'description_en', 'description_eu')

@admin.register(ProductAllergen)
class ProductAllergenAdmin(admin.ModelAdmin):
    list_display = ('product', 'allergen')
    search_fields = ('product__name_es', 'product__name_en', 'product__name_eu', 'allergen__name_es', 'allergen__name_en', 'allergen__name_eu')
