from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Address, Product, Valoration, Cart, Image, Allergen, ProductAllergen
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, AddressForm
# View for home
def home(request):
    return render(request, 'onlybites_web/home.html', locals())

# View for menu
def menu(request):
    allProducts = Product.objects.all()
    return render(request, 'onlybites_web/menu.html', locals())

# View for product
def product(request, product_id):
    product = Product.objects.get(product_id=product_id)

    images = Image.objects.filter(product=product)

    allergen_ids = ProductAllergen.objects.filter(product=product).values_list('allergen')
    allergens = []
    for allergen_id in allergen_ids:
        allergens.append(Allergen.objects.get(allergen_id=allergen_id[0]))

    valorations = Valoration.objects.filter(product=product)
    return render(request, 'onlybites_web/product.html', locals())

# View for cart
def cart(request):
    profile = Profile.objects.get(profile_id=1)

    products_id = Cart.objects.filter(profile=profile).values_list('product')
    products = []
    for product_id in products_id:
        products.append(Product.objects.get(product_id=product_id[0]))

    addresses = Address.objects.filter(profile=profile)
    return render(request, 'onlybites_web/cart.html', locals())

# View for profile
def profile(request):
    profile = Profile.objects.get(profile_id=request.user.profile_id)
    
    addresses = Address.objects.filter(profile=profile)

    return render(request, 'onlybites_web/profile.html', locals())

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.profile = request.user
            address.save()
            return redirect('profile')
    else:
        form = AddressForm()

    return render(request, 'onlybites_web/add-address.html', {'form': form})

def edit_address(request, id):
    address = get_object_or_404(Address, address_id=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddressForm(instance=address)

    return render(request, 'onlybites_web/add-address.html', {'form': form, 'address': address})

# View for profile session management
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save()
            login(request, profile)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'onlybites_web/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        profile = authenticate(request, email=email, password=password)
        if profile is not None:
            login(request, profile)
            return redirect('home')
        else:
            return render(request, 'onlybites_web/login.html', {'error': 'Invalid email or password'})
    return render(request, 'onlybites_web/login.html')

def logout_view(request):
    logout(request)
    response = redirect('home')  
    response.delete_cookie('sessionid')
    return response
 

def add_rating(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)

    # Busca si ya existe una valoración de este usuario para este producto
    valoration = Valoration.objects.filter(profile=request.user, product=product).first()

    if request.method == 'POST':
        rating_value = float(request.POST.get('rating', 0))
        message = request.POST.get('message', '')

        if valoration:
            # Actualiza la valoración existente
            valoration.value = rating_value
            valoration.message = message
            valoration.save()
            messages.success(request, 'Tu valoración ha sido actualizada con éxito.')
        else:
            # Crea una nueva valoración si no existe
            valoration = Valoration(
                profile=request.user,
                product=product,
                value=rating_value,
                message=message
            )
            valoration.save()
            messages.success(request, 'Tu valoración ha sido creada con éxito.')

        return redirect('product', product_id=product_id)

    # Renderiza el template con el formulario y la valoración existente (si la hay)
    return render(request, 'onlybites_web/add-rating.html', {
        'product': product,
        'existing_valoration': valoration,
    })