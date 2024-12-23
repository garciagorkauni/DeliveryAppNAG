from django.apps import AppConfig


class OnlybitesWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlybites_web'

    def ready(self):
        import onlybites_web.signals
