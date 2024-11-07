from django.contrib import admin
from .models import Profile, Address, Product, Valoration, Cart, Order, Image, Allergen, ProductAllergen

admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Valoration)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Image)
admin.site.register(Allergen)
admin.site.register(ProductAllergen)
