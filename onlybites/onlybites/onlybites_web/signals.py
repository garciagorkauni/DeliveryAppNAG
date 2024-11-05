from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile,Valoration
from django.db.models import Avg

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Intenta obtener la cuenta social asociada
        try:
            social_account = SocialAccount.objects.get(user=instance)

            # Obtener el correo y nombre del usuario de Google
            email = social_account.extra_data.get('email')
            name = social_account.extra_data.get('name')
            surname = social_account.extra_data.get('surname')

            # Crear el perfil usando el correo y nombre
            Profile.objects.create(
                email=email,
                name=name,
                surname=surname,
                birthdate=None,  
                telephone='',  
                is_active=True,
                is_staff=False,
                is_superuser=False
            )
        except SocialAccount.DoesNotExist:
            print("No se encontró una cuenta social para este usuario.")
@receiver(post_save, sender=Valoration)
def update_product_valoration_avg(sender, instance, **kwargs):
    # Obtén el producto asociado a la valoración
    product = instance.product

    # Calcula la media de todas las valoraciones para el producto
    avg_valoration = Valoration.objects.filter(product=product).aggregate(Avg('value'))['value__avg']

    # Actualiza el campo valoration_avg del producto
    product.valoration_avg = avg_valoration if avg_valoration is not None else 0
    product.save()