from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Address, Product, Valoration, Cart, Image, Allergen, ProductAllergen
from django.contrib.auth import login, authenticate, logout ,get_user_model
from .forms import RegisterForm, AddressForm, ValorationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
    response = redirect('home')  # Redirigir a la página deseada
    response.delete_cookie('sessionid')
    return response
  # Asegúrate de que el usuario esté autenticado
def add_valoration(request, product_id):
    producto = get_object_or_404(Product, product_id=product_id)
    #perfil = get_object_or_404(Profile, user=request.user)  # Obtener el perfil del usuario autenticado

    if request.method == 'POST':
        form = ValorationForm(request.POST)
        if form.is_valid():
            valoracion = form.save(commit=False)  # No guardar todavía en la base de datos
            valoracion.product = producto         # Asignar el producto actual
            valoracion.profile = request.user           # Asignar el perfil del usuario autenticado
            valoracion.save()                     # Guardar en la base de datos
            return redirect('product', product_id=producto.product_id)
    else:
        form = ValorationForm()

    return render(request, 'onlybites_web/add-address.html', {'form': form})
def add_rating(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)  # Obtén el producto
    if request.method == 'POST':
        # Recoge el rating y el mensaje desde request.POST
        rating_value = float(request.POST.get('rating', 0))  # Obtiene el valor de la valoración
        message = request.POST.get('message', '')  # Obtiene el mensaje de la valoración
        
        # Crea la valoración
        valoration = Valoration(
            profile=request.user,  # Asumiendo que tienes una relación con Profile
            product=product,
            value=rating_value,
            message=message
        )
        valoration.save()  # Guarda la valoración en la base de datos
        
        return redirect('product', product_id=product_id)  # Redirige al detalle del producto

    # Renderiza el template con el formulario
    return render(request, 'onlybites_web/add-rating.html', {
        'product': product,
    })