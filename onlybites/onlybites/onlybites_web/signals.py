from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

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
            print("No se encontró una cuenta social para este usuario.")
