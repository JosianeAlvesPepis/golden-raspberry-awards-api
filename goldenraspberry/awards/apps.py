from django.apps import AppConfig

class AwardsConfig(AppConfig):
    """
    Configuração da aplicação Awards.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awards'

    def ready(self):
        """
        Função chamada quando a aplicação está pronta.
        Importa os sinais da aplicação awards.
        """
        import awards.signals
