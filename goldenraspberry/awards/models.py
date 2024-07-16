from django.db import models

class Filme(models.Model):
    """
    Modelo para representar um filme.
    """
    titulo = models.CharField(max_length=255)
    produtor = models.CharField(max_length=255)
    ano = models.IntegerField()
    vencedor = models.BooleanField()

    def __str__(self):
        """
        Retorna a representação em string do objeto Filme.
        """
        return self.titulo
