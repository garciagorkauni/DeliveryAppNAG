from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Address, Product, Valoration, Cart, Image, Allergen, ProductAllergen
from django.contrib.auth import login, authenticate, logout ,get_user_model
from .forms import RegisterForm, AddressForm
from django.contrib.auth.models import User
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

# View for register
def register(request):
    return render(request, 'onlybites_web/register.html', locals())

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

def custom_create_user(backend, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        # Obtén información del usuario
        email = response.get('email')
        name = response.get('name')  # Obtén el nombre completo
        surname = response.get('family_name')  # Obtén el apellido

        # Crea o recupera el usuario de Django
        user = Profile.objects.get_or_create(
            email=email,
            defaults={
                'name': name,
                'surname': surname,
                # Puedes agregar otros campos aquí si es necesario
            }
        )

        return {'user': user}
""" User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        try:
            # Obtener la cuenta social asociada
            social_account = SocialAccount.objects.get(user=instance)

            # Obtener el correo y nombre del usuario de Google
            email = social_account.extra_data.get('email')
            name = social_account.extra_data.get('name')

            # Crear el perfil usando el correo y nombre
            Profile.objects.create(
                email=email,
                name=name,
                surname='',  # Ajusta según tus necesidades
                birthdate=None,  # Ajusta según tus necesidades
                telephone='',  # Ajusta según tus necesidades
                is_active=True,
                is_staff=False,
                is_superuser=False
            )
        except SocialAccount.DoesNotExist:
            # Manejar el caso donde no hay cuenta social asociada
            print("No se encontró una cuenta social para este usuario.") """

def logout_view(request):
    logout(request)
    response = redirect('home')  # Redirigir a la página deseada
    response.delete_cookie('sessionid')
    return response