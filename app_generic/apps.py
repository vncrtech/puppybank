from django.apps import AppConfig


class AppGenericConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_generic'
