from django.apps import AppConfig


class PersonaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'persona'

    def ready(self):
        # Ensure that the signals are imported when the app is ready
        # This will ensure that the signal handlers are connected
        # when the app is loaded.
        import persona.signals