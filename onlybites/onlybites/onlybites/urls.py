# onlybites/urls.py (archivo principal)

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('i18n/', include('django.conf.urls.i18n')),  # Añadir esto para habilitar el cambio de idioma
]

# Usa i18n_patterns para incluir las rutas de la app
urlpatterns += i18n_patterns(
    path('', include('onlybites_web.urls')),  # Incluye las rutas de la app en el patrón i18n
)
