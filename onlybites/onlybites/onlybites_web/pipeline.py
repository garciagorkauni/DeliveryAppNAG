from django.conf import settings
from social_core.exceptions import AuthCanceled
from social_core.pipeline.partial import partial
from .models import Profile

@partial
def get_user_details(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        # Obtén el nombre y apellido de la respuesta de Google
        name = response.get('name')
        given_name = response.get('given_name')  # Nombre
        family_name = response.get('family_name')  # Apellido

        # Si el usuario ya existe, actualiza sus detalles
        if user and not Profile.objects.filter(email=user.email).exists():
            # Crea un nuevo Profile
            Profile.objects.create(
                email=user.email,
                name=given_name,
                surname=family_name,
                is_active=True,  # O cualquier otra lógica que necesites
            )
        else:
            # Actualiza el Profile existente
            profile = Profile.objects.get(email=user.email)
            profile.name = given_name
            profile.surname = family_name
            profile.save()
