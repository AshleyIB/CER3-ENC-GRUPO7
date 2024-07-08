from django.apps import AppConfig


class ProduccionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produccion'

    def ready(self):
        import produccion.signals  
