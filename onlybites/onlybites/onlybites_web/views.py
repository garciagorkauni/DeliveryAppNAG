from django.shortcuts import render

# View for home
def home(request):
    return render(request, 'onlybites_web/home.html', locals())

# View for menu
def menu(request):
    return render(request, 'onlybites_web/menu.html', locals())

# View for product
def product(request):
    return render(request, 'onlybites_web/product.html', locals())

# View for cart
def cart(request):
    return render(request, 'onlybites_web/cart.html', locals())

# View for register
def register(request):
    return render(request, 'onlybites_web/register.html', locals())

# View for profile
def profile(request):
    return render(request, 'onlybites_web/profile.html', locals())